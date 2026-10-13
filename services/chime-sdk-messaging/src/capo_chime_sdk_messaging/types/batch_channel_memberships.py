"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchChannelMemberships``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.members
    import capo_chime_sdk_messaging.types.sub_channel_id


class BatchChannelMemberships(TypedDict, closed=True):
    invited_by: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The identifier of the member who invited another member.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership types set for the channel members.</p>"""
    members: NotRequired["capo_chime_sdk_messaging.types.members.Members"]
    """<p>The users successfully added to the request.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel to which you're adding members.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchChannelMemberships) -> dict:
    out: dict = {}
    if "invited_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["InvitedBy"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["invited_by"]
        )
    if "type" in value:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    if "members" in value:
        import capo_chime_sdk_messaging.types.members

        out["Members"] = capo_chime_sdk_messaging.types.members.serialize_json(
            value["members"]
        )
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> BatchChannelMemberships:
    out: BatchChannelMemberships = {}  # type: ignore[typeddict-item]
    if data.get("InvitedBy") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["invited_by"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["InvitedBy"]
        )
    if data.get("Type") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("Members") is not None:
        import capo_chime_sdk_messaging.types.members

        out["members"] = capo_chime_sdk_messaging.types.members.deserialize_json(
            data["Members"]
        )
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("SubChannelId") is not None:
        out["sub_channel_id"] = data["SubChannelId"]
    return out


def redact_sensitive(value: BatchChannelMemberships) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invited_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["invited_by"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["invited_by"]
        )
    if "members" in value:
        import capo_chime_sdk_messaging.types.members

        out["members"] = capo_chime_sdk_messaging.types.members.redact_sensitive(
            value["members"]
        )
    return out
