"""Generated from Smithy shape ``com.amazonaws.health#eventTypeList2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type2

eventTypeList2: TypeAlias = list["capo_health.types.event_type2.EventType2"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeList2) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> eventTypeList2:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventTypeList2) -> list:
    return list(value)


def deserialize_cbor(data: list) -> eventTypeList2:
    return [item for item in data if item is not None]
