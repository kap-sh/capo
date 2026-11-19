"""Generated from Smithy shape ``com.amazonaws.health#EventTypeActionabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type_actionability

EventTypeActionabilityList: TypeAlias = list[
    "capo_health.types.event_type_actionability.EventTypeActionability"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeActionabilityList) -> list:
    import capo_health.types.event_type_actionability

    out: list = []
    for item in value:
        out.append(
            capo_health.types.event_type_actionability.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeActionabilityList:
    import capo_health.types.event_type_actionability

    out: EventTypeActionabilityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.event_type_actionability.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTypeActionabilityList) -> list:
    import capo_health.types.event_type_actionability

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type_actionability.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventTypeActionabilityList:
    import capo_health.types.event_type_actionability

    out: EventTypeActionabilityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_type_actionability.deserialize_cbor(item))
    return out
