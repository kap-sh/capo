"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelBan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.timestamp


class ChannelBan(TypedDict, closed=True):
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The member being banned from the channel.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel from which a member is being banned.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the ban was created.</p>"""
    created_by: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the ban.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelBan) -> dict:
    out: dict = {}
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
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


def deserialize_json(data: dict) -> ChannelBan:
    out: ChannelBan = {}  # type: ignore[typeddict-item]
    if data.get("Member") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
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


def redact_sensitive(value: ChannelBan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["member"]
        )
    if "created_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["created_by"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["created_by"]
        )
    return out
