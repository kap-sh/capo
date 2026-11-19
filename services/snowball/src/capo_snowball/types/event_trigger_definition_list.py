"""Generated from Smithy shape ``com.amazonaws.snowball#EventTriggerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.event_trigger_definition

EventTriggerDefinitionList: TypeAlias = list[
    "capo_snowball.types.event_trigger_definition.EventTriggerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTriggerDefinitionList) -> list:
    import capo_snowball.types.event_trigger_definition

    out: list = []
    for item in value:
        out.append(
            capo_snowball.types.event_trigger_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventTriggerDefinitionList:
    import capo_snowball.types.event_trigger_definition

    out: EventTriggerDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_snowball.types.event_trigger_definition.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTriggerDefinitionList) -> list:
    import capo_snowball.types.event_trigger_definition

    out: list = []
    for item in value:
        out.append(capo_snowball.types.event_trigger_definition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventTriggerDefinitionList:
    import capo_snowball.types.event_trigger_definition

    out: EventTriggerDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.event_trigger_definition.deserialize_cbor(item))
    return out
