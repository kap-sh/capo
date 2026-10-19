"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateNotifyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import capo_pinpoint_sms_voice_v2.types.notify_pool_id_or_unset
    import capo_pinpoint_sms_voice_v2.types.notify_template_id


class UpdateNotifyConfigurationRequest(TypedDict, closed=True):
    notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn"
    """<p>The identifier of the notify configuration to update. The NotifyConfigurationId can be found using the <a>DescribeNotifyConfigurations</a> operation.</p>"""
    default_template_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier. Pass the special value <code>UNSET_DEFAULT_TEMPLATE</code> to clear the current default template from the notify configuration.</p>"""
    pool_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_pool_id_or_unset.NotifyPoolIdOrUnset"
    ]
    """<p>The pool identifier or Amazon Resource Name (ARN) to associate with the notify configuration. Pass the special value <code>UNSET_DEFAULT_POOL_FOR_NOTIFY</code> to clear the current default pool from the notify configuration.</p>"""
    enabled_countries: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>"""
    enabled_channels: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    ]
    """<p>An array of channels to enable for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>When set to true the notify configuration can't be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateNotifyConfigurationRequest) -> dict:
    out: dict = {}
    out["NotifyConfigurationId"] = value["notify_configuration_id"]
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
    if "enabled_channels" in value:
        import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["EnabledChannels"] = (
            capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
                value["enabled_channels"]
            )
        )
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateNotifyConfigurationRequest:
    out: UpdateNotifyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("NotifyConfigurationId") is not None:
        out["notify_configuration_id"] = data["NotifyConfigurationId"]
    else:
        out["notify_configuration_id"] = ""
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
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    return out
