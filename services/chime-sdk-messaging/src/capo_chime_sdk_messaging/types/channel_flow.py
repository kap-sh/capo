"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlow``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.processor_list
    import capo_chime_sdk_messaging.types.timestamp


class ChannelFlow(TypedDict, closed=True):
    channel_flow_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel flow.</p>"""
    processors: NotRequired[
        "capo_chime_sdk_messaging.types.processor_list.ProcessorList"
    ]
    """<p>Information about the processor Lambda functions.</p>"""
    name: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel flow.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the channel flow was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a channel flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlow) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "processors" in value:
        import capo_chime_sdk_messaging.types.processor_list

        out["Processors"] = (
            capo_chime_sdk_messaging.types.processor_list.serialize_json(
                value["processors"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "created_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelFlow:
    out: ChannelFlow = {}  # type: ignore[typeddict-item]
    if data.get("ChannelFlowArn") is not None:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if data.get("Processors") is not None:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    return out


def redact_sensitive(value: ChannelFlow) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "processors" in value:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.redact_sensitive(
                value["processors"]
            )
        )
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
