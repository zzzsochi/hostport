import pytest

import hostport


def test_hostport():
    assert hostport.parse('host:30') == hostport.HostPort(host='host', port=30)


def test_default_host():
    _hp = hostport.parse('30', default_host='host')
    assert _hp == hostport.HostPort(host='host', port=30)


def test_default_port():
    _hp = hostport.parse('host', default_port=30)
    assert _hp == hostport.HostPort(host='host', port=30)


def test_default():
    _hp = hostport.parse(default_host='host', default_port=30)
    assert _hp == hostport.HostPort(host='host', port=30)


def test_no_default_port():
    _hp = hostport.parse('host')
    assert _hp == hostport.HostPort(host='host', port=None)


def test_no_default_host():
    _hp = hostport.parse('30')
    assert _hp == hostport.HostPort(host=None, port=30)


def test_no_default():
    _hp = hostport.parse()
    assert _hp == hostport.HostPort(host=None, port=None)


def test_colon_port():
    _hp = hostport.parse(':30')
    assert _hp == hostport.HostPort(host=None, port=30)


def test_bad_port():
    with pytest.raises(ValueError):
        hostport.parse('host:bad')


def test_bad_colon_port():
    with pytest.raises(ValueError):
        hostport.parse(':bad')


def test_negative_port():
    with pytest.raises(ValueError):
        hostport.parse('host:-1')
