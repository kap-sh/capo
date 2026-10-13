"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelMembershipPreferencesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_preferences
    import capo_chime_sdk_messaging.types.chime_arn


class PutChannelMembershipPreferencesRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the member setting the preferences.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    preferences: "capo_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences"
    """<p>The channel membership preferences of an <code>AppInstanceUser</code> .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelMembershipPreferencesRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.channel_membership_preferences

    out["Preferences"] = (
        capo_chime_sdk_messaging.types.channel_membership_preferences.serialize_json(
            value["preferences"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutChannelMembershipPreferencesRequest:
    out: PutChannelMembershipPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Preferences") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.deserialize_json(
                data["Preferences"]
            )
        )
    else:
        raise DeserializationError(
            "PutChannelMembershipPreferencesRequest.preferences required"
        )
    return out


def redact_sensitive(value: PutChannelMembershipPreferencesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "preferences" in value:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.redact_sensitive(
                value["preferences"]
            )
        )
    return out
