"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RoutingControlStateChange``."""

from typing import Literal, TypeAlias, cast

RoutingControlStateChange: TypeAlias = Literal[
    "On",
    "Off",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingControlStateChange) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RoutingControlStateChange:
    return cast(RoutingControlStateChange, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RoutingControlStateChange) -> str:
    return value


def deserialize_cbor(data: str) -> RoutingControlStateChange:
    return cast(RoutingControlStateChange, data)
