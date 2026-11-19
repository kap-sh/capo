"""Generated from Smithy shape ``com.amazonaws.servicediscovery#RoutingPolicy``."""

from typing import Literal, TypeAlias, cast

RoutingPolicy: TypeAlias = Literal[
    "MULTIVALUE",
    "WEIGHTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingPolicy:
    return cast(RoutingPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RoutingPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> RoutingPolicy:
    return cast(RoutingPolicy, data)
