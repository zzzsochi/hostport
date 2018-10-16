from typing import NamedTuple, Optional


class HostPort(NamedTuple):
    host: str
    port: int


def parse(hostport: str = '', *,
          default_host: Optional[str] = None,
          default_port: Optional[int] = None) -> HostPort:
    """ Parse host:port strings like as 'localhost:8080'.
    """
    if ':' in hostport:
        host, port_str = hostport.split(':', 1)
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
        try:
            port = int(hostport)
        except ValueError:
            return HostPort(host=hostport or default_host,
                            port=default_port)
        else:
            return HostPort(host=default_host, port=port)
