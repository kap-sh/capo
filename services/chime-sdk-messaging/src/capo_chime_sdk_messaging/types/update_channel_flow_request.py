"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.processor_list


class UpdateChannelFlowRequest(TypedDict, closed=True):
    channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""
    processors: "capo_chime_sdk_messaging.types.processor_list.ProcessorList"
    """<p>Information about the processor Lambda functions </p>"""
    name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelFlowRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.processor_list

    out["Processors"] = capo_chime_sdk_messaging.types.processor_list.serialize_json(
        value["processors"]
    )
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateChannelFlowRequest:
    out: UpdateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Processors") is not None:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    else:
        out["processors"] = []
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out


def redact_sensitive(value: UpdateChannelFlowRequest) -> dict[str, Any]:
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
