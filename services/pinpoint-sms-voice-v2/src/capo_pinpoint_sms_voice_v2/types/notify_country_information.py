"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyCountryInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import capo_pinpoint_sms_voice_v2.types.notify_tier_list
    import capo_pinpoint_sms_voice_v2.types.notify_use_case_list


class NotifyCountryInformation(TypedDict, closed=True):
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    country_name: "str"
    """<p>The name of the country.</p>"""
    supported_channels: "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of supported channels for the country. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    supported_use_cases: (
        "capo_pinpoint_sms_voice_v2.types.notify_use_case_list.NotifyUseCaseList"
    )
    """<p>An array of supported use cases for the country.</p>"""
    supported_tiers: "capo_pinpoint_sms_voice_v2.types.notify_tier_list.NotifyTierList"
    """<p>An array of supported tiers for the country.</p>"""
    customer_owned_identity_required: "bool"
    """<p>Whether a customer-owned identity is required to send notify messages to this country.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyCountryInformation) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["CountryName"] = value["country_name"]
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

    out["SupportedChannels"] = (
        capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
            value["supported_channels"]
        )
    )
    import capo_pinpoint_sms_voice_v2.types.notify_use_case_list

    out["SupportedUseCases"] = (
        capo_pinpoint_sms_voice_v2.types.notify_use_case_list.serialize_aws_json_1_0(
            value["supported_use_cases"]
        )
    )
    import capo_pinpoint_sms_voice_v2.types.notify_tier_list

    out["SupportedTiers"] = (
        capo_pinpoint_sms_voice_v2.types.notify_tier_list.serialize_aws_json_1_0(
            value["supported_tiers"]
        )
    )
    out["CustomerOwnedIdentityRequired"] = value.get(
        "customer_owned_identity_required", False
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyCountryInformation:
    out: NotifyCountryInformation = {}  # type: ignore[typeddict-item]
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        out["iso_country_code"] = ""
    if data.get("CountryName") is not None:
        out["country_name"] = data["CountryName"]
    else:
        out["country_name"] = ""
    if data.get("SupportedChannels") is not None:
        import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["supported_channels"] = (
            capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.deserialize_aws_json_1_0(
                data["SupportedChannels"]
            )
        )
    else:
        out["supported_channels"] = []
    if data.get("SupportedUseCases") is not None:
        import capo_pinpoint_sms_voice_v2.types.notify_use_case_list

        out["supported_use_cases"] = (
            capo_pinpoint_sms_voice_v2.types.notify_use_case_list.deserialize_aws_json_1_0(
                data["SupportedUseCases"]
            )
        )
    else:
        out["supported_use_cases"] = []
    if data.get("SupportedTiers") is not None:
        import capo_pinpoint_sms_voice_v2.types.notify_tier_list

        out["supported_tiers"] = (
            capo_pinpoint_sms_voice_v2.types.notify_tier_list.deserialize_aws_json_1_0(
                data["SupportedTiers"]
            )
        )
    else:
        out["supported_tiers"] = []
    if data.get("CustomerOwnedIdentityRequired") is not None:
        out["customer_owned_identity_required"] = data["CustomerOwnedIdentityRequired"]
    else:
        out["customer_owned_identity_required"] = False
    return out
