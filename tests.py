import pytest

import hostport


@pytest.mark.parametrize('raw, host, port', [
    ('testhost:30', 'testhost', 30),
    ('testhost', 'testhost', None),
    ('[fe80::95f3]:30', 'fe80::95f3', 30),
    ('[fe80::95f3]', 'fe80::95f3', None),
    ('30', None, 30),
    (':30', None, 30),
])
def test_no_default(raw, host, port):
    assert hostport.parse(raw) == hostport.HostPort(host=host, port=port)


def test_default_host():
    _hp = hostport.parse('30', default_host='host')
    assert _hp == hostport.HostPort(host='host', port=30)


def test_default_port():
    _hp = hostport.parse('host', default_port=30)
    assert _hp == hostport.HostPort(host='host', port=30)


def test_default_host_port():
    _hp = hostport.parse(default_host='host', default_port=30)
    assert _hp == hostport.HostPort(host='host', port=30)


@pytest.mark.parametrize('raw', ['host:bad', '[fe80::95f3]:bad]'])
def test_bad_port(raw):
    with pytest.raises(ValueError):
        hostport.parse(raw)


def test_bad_colon_port():
    with pytest.raises(ValueError):
        hostport.parse(':bad')


@pytest.mark.parametrize('raw', ['host:-1', '[fe80::95f3]:-1'])
def test_negative_port(raw):
    with pytest.raises(ValueError):
        hostport.parse(raw)
