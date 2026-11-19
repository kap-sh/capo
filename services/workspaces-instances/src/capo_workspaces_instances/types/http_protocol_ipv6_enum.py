"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HttpProtocolIpv6Enum``."""

from typing import Literal, TypeAlias, cast

HttpProtocolIpv6Enum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HttpProtocolIpv6Enum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HttpProtocolIpv6Enum:
    return cast(HttpProtocolIpv6Enum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpProtocolIpv6Enum) -> str:
    return value


def deserialize_cbor(data: str) -> HttpProtocolIpv6Enum:
    return cast(HttpProtocolIpv6Enum, data)
