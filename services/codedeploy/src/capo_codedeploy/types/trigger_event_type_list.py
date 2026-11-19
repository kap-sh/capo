"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.trigger_event_type

TriggerEventTypeList: TypeAlias = list[
    "capo_codedeploy.types.trigger_event_type.TriggerEventType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerEventTypeList) -> list:
    import capo_codedeploy.types.trigger_event_type

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.trigger_event_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TriggerEventTypeList:
    import capo_codedeploy.types.trigger_event_type

    out: TriggerEventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.trigger_event_type.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TriggerEventTypeList) -> list:
    import capo_codedeploy.types.trigger_event_type

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.trigger_event_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TriggerEventTypeList:
    import capo_codedeploy.types.trigger_event_type

    out: TriggerEventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.trigger_event_type.deserialize_cbor(item))
    return out
