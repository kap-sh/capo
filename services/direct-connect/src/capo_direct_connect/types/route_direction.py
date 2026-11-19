"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteDirection``."""

from typing import Literal, TypeAlias, cast

RouteDirection: TypeAlias = Literal[
    "accepted",
    "advertised",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RouteDirection:
    return cast(RouteDirection, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteDirection) -> str:
    return value


def deserialize_cbor(data: str) -> RouteDirection:
    return cast(RouteDirection, data)
