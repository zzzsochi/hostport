from typing import NamedTuple, Optional


class HostPort(NamedTuple):
    host: Optional[str]
    port: Optional[int]


def parse(hostport: str = '', *,
          default_host: Optional[str] = None,
          default_port: Optional[int] = None) -> HostPort:
    """ Parse host:port strings like as 'localhost:8080'.
    """
    if hostport.startswith('[') and ']:' in hostport:
        # [fe80::fc25:d99d:f94a:95f3]:8080
        host, port_str = hostport.rsplit(']:', 1)
        host = host[1:]
        try:
            port = int(port_str)
        except ValueError:
            raise ValueError(f"Bad port: {port_str!r}")
        else:
            if port >= 0:
                return HostPort(host=host or default_host,
                                port=port)
            else:
                raise ValueError(f"Bad port: '{port}'")

    elif hostport.startswith('[') and hostport.endswith(']'):
        # [fe80::fc25:d99d:f94a:95f3]
        return HostPort(host=hostport[1:-1], port=default_port)

    elif ':' in hostport:
        # 127.0.0.1:8080
        # localhost:8080
        host, port_str = hostport.rsplit(':', 1)
        try:
            port = int(port_str)
        except ValueError:
            raise ValueError(f"Bad port: {port_str!r}")
        else:
            if port >= 0:
                return HostPort(host=host or default_host,
                                port=port)
            else:
                raise ValueError(f"Bad port: '{port}'")
    else:
        # 8080
        # localhost
        try:
            port = int(hostport)
        except ValueError:
            return HostPort(host=hostport or default_host,
                            port=default_port)
        else:
            return HostPort(host=default_host, port=port)
