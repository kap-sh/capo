"""Generated from Smithy shape ``com.amazonaws.memorydb#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.event

EventList: TypeAlias = list["capo_memorydb.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventList) -> list:
    import capo_memorydb.types.event

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventList:
    import capo_memorydb.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.event.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventList) -> list:
    import capo_memorydb.types.event

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.event.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventList:
    import capo_memorydb.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.event.deserialize_cbor(item))
    return out
