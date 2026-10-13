"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeParameters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.email_channel_subtype_parameters
    import capo_connectcampaignsv2.types.sms_channel_subtype_parameters
    import capo_connectcampaignsv2.types.telephony_channel_subtype_parameters
    import capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters


class _ChannelSubtypeParameters_telephony(TypedDict, closed=True):
    telephony: "capo_connectcampaignsv2.types.telephony_channel_subtype_parameters.TelephonyChannelSubtypeParameters"


class _ChannelSubtypeParameters_sms(TypedDict, closed=True):
    sms: "capo_connectcampaignsv2.types.sms_channel_subtype_parameters.SmsChannelSubtypeParameters"


class _ChannelSubtypeParameters_email(TypedDict, closed=True):
    email: "capo_connectcampaignsv2.types.email_channel_subtype_parameters.EmailChannelSubtypeParameters"


class _ChannelSubtypeParameters_whatsApp(TypedDict, closed=True):
    whatsApp: "capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters.WhatsAppChannelSubtypeParameters"


ChannelSubtypeParameters: TypeAlias = (
    _ChannelSubtypeParameters_telephony
    | _ChannelSubtypeParameters_sms
    | _ChannelSubtypeParameters_email
    | _ChannelSubtypeParameters_whatsApp
)


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeParameters) -> dict:
    if "telephony" in value:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_parameters

        return {
            "telephony": capo_connectcampaignsv2.types.telephony_channel_subtype_parameters.serialize_json(
                value["telephony"]
            )
        }
    elif "sms" in value:
        import capo_connectcampaignsv2.types.sms_channel_subtype_parameters

        return {
            "sms": capo_connectcampaignsv2.types.sms_channel_subtype_parameters.serialize_json(
                value["sms"]
            )
        }
    elif "email" in value:
        import capo_connectcampaignsv2.types.email_channel_subtype_parameters

        return {
            "email": capo_connectcampaignsv2.types.email_channel_subtype_parameters.serialize_json(
                value["email"]
            )
        }
    elif "whatsApp" in value:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters

        return {
            "whatsApp": capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError("ChannelSubtypeParameters: no variant present")


def deserialize_json(data: dict) -> ChannelSubtypeParameters:
    if data.get("telephony") is not None:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_parameters

        return {
            "telephony": capo_connectcampaignsv2.types.telephony_channel_subtype_parameters.deserialize_json(
                data["telephony"]
            )
        }
    elif data.get("sms") is not None:
        import capo_connectcampaignsv2.types.sms_channel_subtype_parameters

        return {
            "sms": capo_connectcampaignsv2.types.sms_channel_subtype_parameters.deserialize_json(
                data["sms"]
            )
        }
    elif data.get("email") is not None:
        import capo_connectcampaignsv2.types.email_channel_subtype_parameters

        return {
            "email": capo_connectcampaignsv2.types.email_channel_subtype_parameters.deserialize_json(
                data["email"]
            )
        }
    elif data.get("whatsApp") is not None:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters

        return {
            "whatsApp": capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters.deserialize_json(
                data["whatsApp"]
            )
        }
    else:
        raise DeserializationError(
            "ChannelSubtypeParameters: no recognized variant key"
        )


def redact_sensitive(value: ChannelSubtypeParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "telephony" in value:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_parameters

        out["telephony"] = (
            capo_connectcampaignsv2.types.telephony_channel_subtype_parameters.redact_sensitive(
                value["telephony"]
            )
        )
    if "sms" in value:
        import capo_connectcampaignsv2.types.sms_channel_subtype_parameters

        out["sms"] = (
            capo_connectcampaignsv2.types.sms_channel_subtype_parameters.redact_sensitive(
                value["sms"]
            )
        )
    if "email" in value:
        import capo_connectcampaignsv2.types.email_channel_subtype_parameters

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_parameters.redact_sensitive(
                value["email"]
            )
        )
    if "whatsApp" in value:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters

        out["whatsApp"] = (
            capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters.redact_sensitive(
                value["whatsApp"]
            )
        )
    return out
