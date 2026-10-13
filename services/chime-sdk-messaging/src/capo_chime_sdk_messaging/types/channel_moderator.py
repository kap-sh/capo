"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModerator``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.timestamp


class ChannelModerator(TypedDict, closed=True):
    moderator: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The moderator's data.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the moderator's channel.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the moderator was created.</p>"""
    created_by: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModerator) -> dict:
    out: dict = {}
    if "moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Moderator"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["moderator"]
        )
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "created_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "created_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["CreatedBy"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["created_by"]
        )
    return out


def deserialize_json(data: dict) -> ChannelModerator:
    out: ChannelModerator = {}  # type: ignore[typeddict-item]
    if data.get("Moderator") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["moderator"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Moderator"]
        )
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["created_by"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["CreatedBy"]
        )
    return out


def redact_sensitive(value: ChannelModerator) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["moderator"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["moderator"]
        )
    if "created_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["created_by"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["created_by"]
        )
    return out
