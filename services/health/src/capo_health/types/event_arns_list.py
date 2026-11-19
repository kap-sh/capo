"""Generated from Smithy shape ``com.amazonaws.health#EventArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_arn

EventArnsList: TypeAlias = list["capo_health.types.event_arn.eventArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EventArnsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventArnsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> EventArnsList:
    return [item for item in data if item is not None]
