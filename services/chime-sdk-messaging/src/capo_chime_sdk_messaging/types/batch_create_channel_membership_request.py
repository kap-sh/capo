"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.member_arns
    import capo_chime_sdk_messaging.types.sub_channel_id


class BatchCreateChannelMembershipRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel to which you're adding users or bots.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>"""
    member_arns: "capo_chime_sdk_messaging.types.member_arns.MemberArns"
    """<p>The ARNs of the members you want to add to the channel. Only <code>AppInstanceUsers</code> and <code>AppInstanceBots</code> can be added as a channel member.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request. </p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    import capo_chime_sdk_messaging.types.member_arns

    out["MemberArns"] = capo_chime_sdk_messaging.types.member_arns.serialize_json(
        value["member_arns"]
    )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> BatchCreateChannelMembershipRequest:
    out: BatchCreateChannelMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("MemberArns") is not None:
        import capo_chime_sdk_messaging.types.member_arns

        out["member_arns"] = (
            capo_chime_sdk_messaging.types.member_arns.deserialize_json(
                data["MemberArns"]
            )
        )
    else:
        out["member_arns"] = []
    if data.get("SubChannelId") is not None:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
