=====================================
slacken - Tools for working with REST
=====================================

------------
Introduction
------------

Contains the RESTAccess class for calling endpoints including tools for
accessing both json and xml data. Also included are tools for accessing this
information as an AttrDict (attribute dictionary) - a dictionary where keys can
also be accessed as attributes, in javascript style - accessing a value of this
class of type dict will return another AttrDict, however the original object is
always accessible by calling ._as_dict() on an AttrDict object

-------------------------
Installation Requirements
-------------------------

The following modules are required:

- None currently


------------
Installation
------------

Just run the following command at the command prompt:

.. code-block:: bash

    $ sudo pip install slacken


-----
Usage
-----

.. code-block:: python

    from slacken import RESTaccess, XMLAccessor, AttrDict
    rest_accessor = RESTaccess(rest_root)
    response_data = rest_accessor(endpoint)
    response_dict = response_data.to_dict()\
                        if isinstance(response_data, XMLAccessor) else\
                    AttrDict(response_data)



-------
License
-------

The MIT License (MIT)

Copyright (c) 2013 Alistair Broomhead

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
