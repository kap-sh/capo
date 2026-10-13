"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMembershipsForAppInstanceUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list
    import capo_chime_sdk_messaging.types.next_token


class ListChannelMembershipsForAppInstanceUserResponse(TypedDict, closed=True):
    channel_memberships: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.ChannelMembershipForAppInstanceUserSummaryList"
    ]
    """<p>The information for the requested channel memberships.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMembershipsForAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "channel_memberships" in value:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list

        out["ChannelMemberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.serialize_json(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelMembershipsForAppInstanceUserResponse:
    out: ListChannelMembershipsForAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelMemberships") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list

        out["channel_memberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.deserialize_json(
                data["ChannelMemberships"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListChannelMembershipsForAppInstanceUserResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_memberships" in value:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list

        out["channel_memberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.redact_sensitive(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
