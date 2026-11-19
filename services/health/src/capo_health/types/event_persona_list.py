"""Generated from Smithy shape ``com.amazonaws.health#EventPersonaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_persona

EventPersonaList: TypeAlias = list["capo_health.types.event_persona.EventPersona"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventPersonaList) -> list:
    import capo_health.types.event_persona

    out: list = []
    for item in value:
        out.append(capo_health.types.event_persona.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventPersonaList:
    import capo_health.types.event_persona

    out: EventPersonaList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_persona.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventPersonaList) -> list:
    import capo_health.types.event_persona

    out: list = []
    for item in value:
        out.append(capo_health.types.event_persona.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventPersonaList:
    import capo_health.types.event_persona

    out: EventPersonaList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_persona.deserialize_cbor(item))
    return out
