"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.email_channel_subtype_config
    import capo_connectcampaignsv2.types.sms_channel_subtype_config
    import capo_connectcampaignsv2.types.telephony_channel_subtype_config
    import capo_connectcampaignsv2.types.whats_app_channel_subtype_config


class ChannelSubtypeConfig(TypedDict, closed=True):
    telephony: NotRequired[
        "capo_connectcampaignsv2.types.telephony_channel_subtype_config.TelephonyChannelSubtypeConfig"
    ]
    sms: NotRequired[
        "capo_connectcampaignsv2.types.sms_channel_subtype_config.SmsChannelSubtypeConfig"
    ]
    email: NotRequired[
        "capo_connectcampaignsv2.types.email_channel_subtype_config.EmailChannelSubtypeConfig"
    ]
    whats_app: NotRequired[
        "capo_connectcampaignsv2.types.whats_app_channel_subtype_config.WhatsAppChannelSubtypeConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "telephony" in value:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            capo_connectcampaignsv2.types.telephony_channel_subtype_config.serialize_json(
                value["telephony"]
            )
        )
    if "sms" in value:
        import capo_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            capo_connectcampaignsv2.types.sms_channel_subtype_config.serialize_json(
                value["sms"]
            )
        )
    if "email" in value:
        import capo_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_config.serialize_json(
                value["email"]
            )
        )
    if "whats_app" in value:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whatsApp"] = (
            capo_connectcampaignsv2.types.whats_app_channel_subtype_config.serialize_json(
                value["whats_app"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelSubtypeConfig:
    out: ChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if data.get("telephony") is not None:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            capo_connectcampaignsv2.types.telephony_channel_subtype_config.deserialize_json(
                data["telephony"]
            )
        )
    if data.get("sms") is not None:
        import capo_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            capo_connectcampaignsv2.types.sms_channel_subtype_config.deserialize_json(
                data["sms"]
            )
        )
    if data.get("email") is not None:
        import capo_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_config.deserialize_json(
                data["email"]
            )
        )
    if data.get("whatsApp") is not None:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whats_app"] = (
            capo_connectcampaignsv2.types.whats_app_channel_subtype_config.deserialize_json(
                data["whatsApp"]
            )
        )
    return out


def redact_sensitive(value: ChannelSubtypeConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        import capo_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_config.redact_sensitive(
                value["email"]
            )
        )
    return out
