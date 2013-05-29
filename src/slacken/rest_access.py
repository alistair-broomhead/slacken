""" Accessors for REST endpoints """

from slacken.xml_accessor import XMLAccessor

__author__ = 'Alistair Broomhead'


class RESTaccess(object):
    """
    An accessor for REST endpoints

    rest_hub should be something like 'http://www.integration.moshi/services/rest'
    """
    rest_hub = ''

    @staticmethod
    def _get_raw(url, params=None, credentials=None):
        import requests
        if params is None:
            return requests.get(url, auth=credentials)
        else:
            return requests.post(url, data=params, auth=credentials)

    @staticmethod
    def _parse_json(raw):
        from json import load
        return load(raw)

    @staticmethod
    def _get_json(url, params=None, credentials=None):
        return RESTaccess._parse_json(
            RESTaccess._get_raw(url, params, credentials)
        )

    @staticmethod
    def _parse_xml(raw):
        from xml.dom.minidom import parse
        dom = parse(raw)
        return XMLAccessor(dom)

    @staticmethod
    def _get_xml(url, params=None, credentials=None):
        return RESTaccess._parse_xml(
            RESTaccess._get_raw(url, params, credentials)
        )

    def __init__(self, rest_hub, username=None, password=None):
        self.rest_hub = rest_hub
        self._credentials = {}
        if username is not None:
            self._credentials["username"] = username
            if password is not None:
                self._credentials["password"] = password

    def __repr__(self):
        return 'RESTaccess(%r)' % self.rest_hub

    def url(self, endpoint):
        """ Gives the full url of the given endpoint """
        return '/'.join(
            (self.rest_hub.rstrip('/'), endpoint.lstrip('/'))).rstrip('/')

    def auth(self,
             username=None,
             password=None,
             # auth_url=None
    ):
        if username is None:
            username = self._credentials["username"]
        if password is None and "password" in self._credentials:
            password = self._credentials["password"]
        return username, password

    def __call__(self, endpoint, params=None, username=None, password=None):
        """
        GETs the enpoint unless params is passed, in which case it POSTs params
        """
        url_ = self.url(endpoint)
        credentials = self.auth(username=username, password=password)
        content = self._get_raw(url_, params, credentials)
        subtype = content.headers.subtype.lower().strip()
        assert isinstance(subtype, str)

        if subtype == 'json':
            return self._parse_json(content)
        elif subtype == 'xml':
            return self._parse_xml(content)
        else:
            return content
