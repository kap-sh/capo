"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_mode
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_resource_name


class UpdateChannelRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    name: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel.</p>"""
    mode: NotRequired["capo_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the update request.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata for the update request.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "mode" in value:
        import capo_chime_sdk_messaging.types.channel_mode

        out["Mode"] = capo_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Mode") is not None:
        import capo_chime_sdk_messaging.types.channel_mode

        out["mode"] = capo_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


def redact_sensitive(value: UpdateChannelRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
