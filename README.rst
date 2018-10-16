========
hostport
========

.. image:: https://travis-ci.org/zzzsochi/hostport.svg?branch=master
    :target: https://travis-ci.org/zzzsochi/hostport

.. image:: https://coveralls.io/repos/github/zzzsochi/hostport/badge.svg?branch=master
    :target: https://coveralls.io/github/zzzsochi/hostport?branch=master


Simple parser strings like as ``grpchost:50051``.


Installation
============

.. code:: bash

    $ pip install hostport


Usage
=====

.. code:: python

    >>> import hostport
    >>> hostport.parse('host:30')
    HostPort(host='host', port=30)
    >>> hostport.parse('host:30').host
    'host'
    >>> hostport.parse('host:30').port
    30
    >>> hostport.parse('host', default_port=30)
    HostPort(host='host', port=30)
    >>> hostport.parse('30', default_host='host')
    HostPort(host='host', port=30)
    >>> hostport.parse('host.production:50051', default_host='host', default_port=30)
    HostPort(host='host.production', port=50051)
    >>> hostport.parse('host.production')
    HostPort(host='host.production', port=None)
    >>> hostport.parse('50051')
    HostPort(host=None, port=50051)

It's all.
