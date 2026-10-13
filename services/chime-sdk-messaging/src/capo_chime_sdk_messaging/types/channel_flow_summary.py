"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.processor_list


class ChannelFlowSummary(TypedDict, closed=True):
    channel_flow_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel flow.</p>"""
    name: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel flow.</p>"""
    processors: NotRequired[
        "capo_chime_sdk_messaging.types.processor_list.ProcessorList"
    ]
    """<p>Information about the processor Lambda functions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowSummary) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "processors" in value:
        import capo_chime_sdk_messaging.types.processor_list

        out["Processors"] = (
            capo_chime_sdk_messaging.types.processor_list.serialize_json(
                value["processors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelFlowSummary:
    out: ChannelFlowSummary = {}  # type: ignore[typeddict-item]
    if data.get("ChannelFlowArn") is not None:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Processors") is not None:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    return out


def redact_sensitive(value: ChannelFlowSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "processors" in value:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.redact_sensitive(
                value["processors"]
            )
        )
    return out
