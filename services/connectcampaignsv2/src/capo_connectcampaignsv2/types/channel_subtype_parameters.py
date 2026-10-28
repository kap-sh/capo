"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeParameters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.email_channel_subtype_parameters
    import capo_connectcampaignsv2.types.sms_channel_subtype_parameters
    import capo_connectcampaignsv2.types.telephony_channel_subtype_parameters
    import capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters


class ChannelSubtypeParametersTelephonyMember(TypedDict, closed=True):
    telephony: "capo_connectcampaignsv2.types.telephony_channel_subtype_parameters.TelephonyChannelSubtypeParameters"


class ChannelSubtypeParametersSmsMember(TypedDict, closed=True):
    sms: "capo_connectcampaignsv2.types.sms_channel_subtype_parameters.SmsChannelSubtypeParameters"


class ChannelSubtypeParametersEmailMember(TypedDict, closed=True):
    email: "capo_connectcampaignsv2.types.email_channel_subtype_parameters.EmailChannelSubtypeParameters"


class ChannelSubtypeParametersWhatsAppMember(TypedDict, closed=True):
    whatsApp: "capo_connectcampaignsv2.types.whats_app_channel_subtype_parameters.WhatsAppChannelSubtypeParameters"


ChannelSubtypeParameters: TypeAlias = (
    ChannelSubtypeParametersTelephonyMember
    | ChannelSubtypeParametersSmsMember
    | ChannelSubtypeParametersEmailMember
    | ChannelSubtypeParametersWhatsAppMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeParameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ChannelSubtypeParameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "telephony" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
