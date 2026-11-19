"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.trigger_event_type_list
    import capo_codedeploy.types.trigger_name
    import capo_codedeploy.types.trigger_target_arn


class TriggerConfig(TypedDict, closed=True):
    trigger_name: NotRequired["capo_codedeploy.types.trigger_name.TriggerName"]
    """<p>The name of the notification trigger.</p>"""
    trigger_target_arn: NotRequired[
        "capo_codedeploy.types.trigger_target_arn.TriggerTargetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.</p>"""
    trigger_events: NotRequired[
        "capo_codedeploy.types.trigger_event_type_list.TriggerEventTypeList"
    ]
    """<p>The event type or types for which notifications are triggered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerConfig) -> dict:
    out: dict = {}
    if "trigger_name" in value:
        out["triggerName"] = value["trigger_name"]
    if "trigger_target_arn" in value:
        out["triggerTargetArn"] = value["trigger_target_arn"]
    if "trigger_events" in value:
        import capo_codedeploy.types.trigger_event_type_list

        out["triggerEvents"] = (
            capo_codedeploy.types.trigger_event_type_list.serialize_aws_json_1_1(
                value["trigger_events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TriggerConfig:
    out: TriggerConfig = {}  # type: ignore[typeddict-item]
    if data.get("triggerName") is not None:
        out["trigger_name"] = data["triggerName"]
    if data.get("triggerTargetArn") is not None:
        out["trigger_target_arn"] = data["triggerTargetArn"]
    if data.get("triggerEvents") is not None:
        import capo_codedeploy.types.trigger_event_type_list

        out["trigger_events"] = (
            capo_codedeploy.types.trigger_event_type_list.deserialize_aws_json_1_1(
                data["triggerEvents"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TriggerConfig) -> dict:
    out: dict = {}
    if "trigger_name" in value:
        out["triggerName"] = value["trigger_name"]
    if "trigger_target_arn" in value:
        out["triggerTargetArn"] = value["trigger_target_arn"]
    if "trigger_events" in value:
        import capo_codedeploy.types.trigger_event_type_list

        out["triggerEvents"] = (
            capo_codedeploy.types.trigger_event_type_list.serialize_cbor(
                value["trigger_events"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TriggerConfig:
    out: TriggerConfig = {}  # type: ignore[typeddict-item]
    if data.get("triggerName") is not None:
        out["trigger_name"] = data["triggerName"]
    if data.get("triggerTargetArn") is not None:
        out["trigger_target_arn"] = data["triggerTargetArn"]
    if data.get("triggerEvents") is not None:
        import capo_codedeploy.types.trigger_event_type_list

        out["trigger_events"] = (
            capo_codedeploy.types.trigger_event_type_list.deserialize_cbor(
                data["triggerEvents"]
            )
        )
    return out
