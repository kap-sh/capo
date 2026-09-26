"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#EndpointIpAddressType``."""

from typing import Literal, TypeAlias, cast

"""<p>The IP address type used by a private endpoint.</p>"""
EndpointIpAddressType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointIpAddressType) -> str:
    return value


def deserialize_json(data: str) -> EndpointIpAddressType:
    return cast(EndpointIpAddressType, data)
