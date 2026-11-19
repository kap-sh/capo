"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EventSourceMappingAction``."""

from typing import Literal, TypeAlias, cast

EventSourceMappingAction: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSourceMappingAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventSourceMappingAction:
    return cast(EventSourceMappingAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceMappingAction) -> str:
    return value


def deserialize_cbor(data: str) -> EventSourceMappingAction:
    return cast(EventSourceMappingAction, data)
