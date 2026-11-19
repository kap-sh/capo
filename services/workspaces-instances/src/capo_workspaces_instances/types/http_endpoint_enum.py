"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HttpEndpointEnum``."""

from typing import Literal, TypeAlias, cast

HttpEndpointEnum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HttpEndpointEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HttpEndpointEnum:
    return cast(HttpEndpointEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpEndpointEnum) -> str:
    return value


def deserialize_cbor(data: str) -> HttpEndpointEnum:
    return cast(HttpEndpointEnum, data)
