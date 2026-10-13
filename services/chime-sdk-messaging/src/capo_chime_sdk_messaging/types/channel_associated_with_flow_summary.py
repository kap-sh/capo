"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelAssociatedWithFlowSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_mode
    import capo_chime_sdk_messaging.types.channel_privacy
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_resource_name


class ChannelAssociatedWithFlowSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel flow.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    mode: NotRequired["capo_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the channel.</p>"""
    privacy: NotRequired[
        "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The channel's privacy setting.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The channel's metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelAssociatedWithFlowSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "mode" in value:
        import capo_chime_sdk_messaging.types.channel_mode

        out["Mode"] = capo_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "privacy" in value:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["Privacy"] = capo_chime_sdk_messaging.types.channel_privacy.serialize_json(
            value["privacy"]
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> ChannelAssociatedWithFlowSummary:
    out: ChannelAssociatedWithFlowSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("Mode") is not None:
        import capo_chime_sdk_messaging.types.channel_mode

        out["mode"] = capo_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if data.get("Privacy") is not None:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["privacy"] = (
            capo_chime_sdk_messaging.types.channel_privacy.deserialize_json(
                data["Privacy"]
            )
        )
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


def redact_sensitive(value: ChannelAssociatedWithFlowSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
