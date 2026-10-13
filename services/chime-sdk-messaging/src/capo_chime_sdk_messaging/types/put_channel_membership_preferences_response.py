"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelMembershipPreferencesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_preferences
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity


class PutChannelMembershipPreferencesResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The details of a user.</p>"""
    preferences: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences"
    ]
    """<p>The ARN and metadata of the member being added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelMembershipPreferencesResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "preferences" in value:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["Preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutChannelMembershipPreferencesResponse:
    out: PutChannelMembershipPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("Member") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if data.get("Preferences") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.deserialize_json(
                data["Preferences"]
            )
        )
    return out


def redact_sensitive(value: PutChannelMembershipPreferencesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["member"]
        )
    if "preferences" in value:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.redact_sensitive(
                value["preferences"]
            )
        )
    return out
