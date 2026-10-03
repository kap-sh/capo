"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_status
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_tier
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import capo_pinpoint_sms_voice_v2.types.notify_template_id
    import capo_pinpoint_sms_voice_v2.types.tier_upgrade_status


class NotifyConfigurationInformation(TypedDict, closed=True):
    notify_configuration_arn: "capo_pinpoint_sms_voice_v2.types.notify_configuration_arn.NotifyConfigurationArn"
    """<p>The Amazon Resource Name (ARN) for the notify configuration.</p>"""
    notify_configuration_id: (
        "capo_pinpoint_sms_voice_v2.types.notify_configuration_id.NotifyConfigurationId"
    )
    """<p>The unique identifier for the notify configuration.</p>"""
    display_name: "capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name.NotifyConfigurationDisplayName"
    """<p>The display name associated with the notify configuration.</p>"""
    use_case: "capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase"
    """<p>The use case for the notify configuration.</p>"""
    default_template_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The default template identifier associated with the notify configuration.</p>"""
    pool_id: NotRequired["str"]
    """<p>The identifier of the pool associated with the notify configuration.</p>"""
    enabled_countries: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>"""
    enabled_channels: "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of channels enabled for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    tier: "capo_pinpoint_sms_voice_v2.types.notify_configuration_tier.NotifyConfigurationTier"
    """<p>The tier of the notify configuration.</p>"""
    tier_upgrade_status: (
        "capo_pinpoint_sms_voice_v2.types.tier_upgrade_status.TierUpgradeStatus"
    )
    """<p>The tier upgrade status of the notify configuration.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.notify_configuration_status.NotifyConfigurationStatus"
    """<p>The current status of the notify configuration.</p>"""
    rejection_reason: NotRequired["str"]
    """<p>The reason the notify configuration was rejected, if applicable.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false. </p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the notify configuration was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyConfigurationInformation) -> dict:
    out: dict = {}
    out["NotifyConfigurationArn"] = value["notify_configuration_arn"]
    out["NotifyConfigurationId"] = value["notify_configuration_id"]
    out["DisplayName"] = value["display_name"]
    out["UseCase"] = value["use_case"]
    if "default_template_id" in value:
        out["DefaultTemplateId"] = value["default_template_id"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "enabled_countries" in value:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["EnabledCountries"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["enabled_countries"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

    out["EnabledChannels"] = (
        capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
            value["enabled_channels"]
        )
    )
    out["Tier"] = value["tier"]
    out["TierUpgradeStatus"] = value["tier_upgrade_status"]
    out["Status"] = value["status"]
    if "rejection_reason" in value:
        out["RejectionReason"] = value["rejection_reason"]
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyConfigurationInformation:
    out: NotifyConfigurationInformation = {}  # type: ignore[typeddict-item]
    if data.get("NotifyConfigurationArn") is not None:
        out["notify_configuration_arn"] = data["NotifyConfigurationArn"]
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.notify_configuration_arn required"
        )
    if data.get("NotifyConfigurationId") is not None:
        out["notify_configuration_id"] = data["NotifyConfigurationId"]
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.notify_configuration_id required"
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.display_name required"
        )
    if data.get("UseCase") is not None:
        out["use_case"] = data["UseCase"]
    else:
        raise DeserializationError("NotifyConfigurationInformation.use_case required")
    if data.get("DefaultTemplateId") is not None:
        out["default_template_id"] = data["DefaultTemplateId"]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("EnabledCountries") is not None:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["enabled_countries"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["EnabledCountries"]
            )
        )
    if data.get("EnabledChannels") is not None:
        import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["enabled_channels"] = (
            capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.deserialize_aws_json_1_0(
                data["EnabledChannels"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.enabled_channels required"
        )
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    else:
        raise DeserializationError("NotifyConfigurationInformation.tier required")
    if data.get("TierUpgradeStatus") is not None:
        out["tier_upgrade_status"] = data["TierUpgradeStatus"]
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.tier_upgrade_status required"
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("NotifyConfigurationInformation.status required")
    if data.get("RejectionReason") is not None:
        out["rejection_reason"] = data["RejectionReason"]
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyConfigurationInformation.created_timestamp required"
        )
    return out
