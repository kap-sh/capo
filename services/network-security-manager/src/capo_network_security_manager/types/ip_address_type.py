"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#IpAddressType``."""

from typing import Literal, TypeAlias, cast

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "dualstack-without-public-ipv4",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
