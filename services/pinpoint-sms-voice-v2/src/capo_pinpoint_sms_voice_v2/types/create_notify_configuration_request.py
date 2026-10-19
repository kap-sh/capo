"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateNotifyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import capo_pinpoint_sms_voice_v2.types.notify_template_id
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.tag_list


class CreateNotifyConfigurationRequest(TypedDict, closed=True):
    display_name: "capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name.NotifyConfigurationDisplayName"
    """<p>The display name to associate with the notify configuration.</p>"""
    use_case: "capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase"
    """<p>The use case for the notify configuration.</p>"""
    default_template_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier.</p>"""
    pool_id: NotRequired["capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"]
    """<p>The identifier of the pool to associate with the notify configuration.</p>"""
    enabled_countries: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>"""
    enabled_channels: "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of channels to enable for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the notify configuration can't be deleted. You can change this value using the <a>UpdateNotifyConfiguration</a> action.</p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the notify configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateNotifyConfigurationRequest) -> dict:
    out: dict = {}
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
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateNotifyConfigurationRequest:
    out: CreateNotifyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("UseCase") is not None:
        out["use_case"] = data["UseCase"]
    else:
        out["use_case"] = ""
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
        out["enabled_channels"] = []
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
