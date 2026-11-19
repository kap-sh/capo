"""Generated from Smithy shape ``com.amazonaws.health#EventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type

EventTypeList: TypeAlias = list["capo_health.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeList) -> list:
    import capo_health.types.event_type

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeList:
    import capo_health.types.event_type

    out: EventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_type.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTypeList) -> list:
    import capo_health.types.event_type

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventTypeList:
    import capo_health.types.event_type

    out: EventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_type.deserialize_cbor(item))
    return out
