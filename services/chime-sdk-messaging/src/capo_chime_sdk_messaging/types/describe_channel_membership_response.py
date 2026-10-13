"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelMembershipResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership


class DescribeChannelMembershipResponse(TypedDict, closed=True):
    channel_membership: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership.ChannelMembership"
    ]
    """<p>The details of the membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelMembershipResponse) -> dict:
    out: dict = {}
    if "channel_membership" in value:
        import capo_chime_sdk_messaging.types.channel_membership

        out["ChannelMembership"] = (
            capo_chime_sdk_messaging.types.channel_membership.serialize_json(
                value["channel_membership"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelMembershipResponse:
    out: DescribeChannelMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelMembership") is not None:
        import capo_chime_sdk_messaging.types.channel_membership

        out["channel_membership"] = (
            capo_chime_sdk_messaging.types.channel_membership.deserialize_json(
                data["ChannelMembership"]
            )
        )
    return out


def redact_sensitive(value: DescribeChannelMembershipResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_membership" in value:
        import capo_chime_sdk_messaging.types.channel_membership

        out["channel_membership"] = (
            capo_chime_sdk_messaging.types.channel_membership.redact_sensitive(
                value["channel_membership"]
            )
        )
    return out
