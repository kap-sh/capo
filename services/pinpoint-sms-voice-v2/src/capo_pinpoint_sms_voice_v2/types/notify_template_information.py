"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list
    import capo_pinpoint_sms_voice_v2.types.notify_language_code
    import capo_pinpoint_sms_voice_v2.types.notify_template_id
    import capo_pinpoint_sms_voice_v2.types.notify_template_status
    import capo_pinpoint_sms_voice_v2.types.notify_template_type
    import capo_pinpoint_sms_voice_v2.types.notify_template_version
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.template_content
    import capo_pinpoint_sms_voice_v2.types.template_variables_map
    import capo_pinpoint_sms_voice_v2.types.voice_id_list


class NotifyTemplateInformation(TypedDict, closed=True):
    template_id: "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    """<p>The unique identifier for the template.</p>"""
    version: (
        "capo_pinpoint_sms_voice_v2.types.notify_template_version.NotifyTemplateVersion"
    )
    """<p>The version of the template.</p>"""
    template_type: (
        "capo_pinpoint_sms_voice_v2.types.notify_template_type.NotifyTemplateType"
    )
    """<p>The type of the template.</p>"""
    channels: (
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    )
    """<p>The channels for the template. Supported values are <code>SMS</code> and <code>VOICE</code>.</p>"""
    tier_access: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.NotifyConfigurationTierList"
    ]
    """<p>The tier access level for the template.</p>"""
    status: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_status.NotifyTemplateStatus"
    ]
    """<p>The current status of the template.</p>"""
    supported_countries: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of supported country codes for the template.</p>"""
    language_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_language_code.NotifyLanguageCode"
    ]
    """<p>The language code for the template.</p>"""
    content: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.template_content.TemplateContent"
    ]
    """<p>The content of the template.</p>"""
    variables: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.template_variables_map.TemplateVariablesMap"
    ]
    """<p>An array of template variable metadata for the template.</p>"""
    supported_voice_ids: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.voice_id_list.VoiceIdList"
    ]
    """<p>An array of supported voice IDs for voice templates.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the notify template was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTemplateInformation) -> dict:
    out: dict = {}
    out["TemplateId"] = value["template_id"]
    out["Version"] = value["version"]
    out["TemplateType"] = value["template_type"]
    import capo_pinpoint_sms_voice_v2.types.number_capability_list

    out["Channels"] = (
        capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["channels"]
        )
    )
    if "tier_access" in value:
        import capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list

        out["TierAccess"] = (
            capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.serialize_aws_json_1_0(
                value["tier_access"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "supported_countries" in value:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["SupportedCountries"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["supported_countries"]
            )
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "content" in value:
        out["Content"] = value["content"]
    if "variables" in value:
        import capo_pinpoint_sms_voice_v2.types.template_variables_map

        out["Variables"] = (
            capo_pinpoint_sms_voice_v2.types.template_variables_map.serialize_aws_json_1_0(
                value["variables"]
            )
        )
    if "supported_voice_ids" in value:
        import capo_pinpoint_sms_voice_v2.types.voice_id_list

        out["SupportedVoiceIds"] = (
            capo_pinpoint_sms_voice_v2.types.voice_id_list.serialize_aws_json_1_0(
                value["supported_voice_ids"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyTemplateInformation:
    out: NotifyTemplateInformation = {}  # type: ignore[typeddict-item]
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    else:
        raise DeserializationError("NotifyTemplateInformation.template_id required")
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("NotifyTemplateInformation.version required")
    if data.get("TemplateType") is not None:
        out["template_type"] = data["TemplateType"]
    else:
        raise DeserializationError("NotifyTemplateInformation.template_type required")
    if data.get("Channels") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["channels"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["Channels"]
            )
        )
    else:
        raise DeserializationError("NotifyTemplateInformation.channels required")
    if data.get("TierAccess") is not None:
        import capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list

        out["tier_access"] = (
            capo_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.deserialize_aws_json_1_0(
                data["TierAccess"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("SupportedCountries") is not None:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["supported_countries"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["SupportedCountries"]
            )
        )
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Variables") is not None:
        import capo_pinpoint_sms_voice_v2.types.template_variables_map

        out["variables"] = (
            capo_pinpoint_sms_voice_v2.types.template_variables_map.deserialize_aws_json_1_0(
                data["Variables"]
            )
        )
    if data.get("SupportedVoiceIds") is not None:
        import capo_pinpoint_sms_voice_v2.types.voice_id_list

        out["supported_voice_ids"] = (
            capo_pinpoint_sms_voice_v2.types.voice_id_list.deserialize_aws_json_1_0(
                data["SupportedVoiceIds"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyTemplateInformation.created_timestamp required"
        )
    return out
