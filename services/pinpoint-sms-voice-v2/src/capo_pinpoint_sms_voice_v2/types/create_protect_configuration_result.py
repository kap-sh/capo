"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateProtectConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id
    import capo_pinpoint_sms_voice_v2.types.tag_list


class CreateProtectConfigurationResult(TypedDict, closed=True):
    protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the protect configuration was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    account_default: "bool"
    """<p>This is true if the protect configuration is set as your account default protect configuration.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false. </p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProtectConfigurationResult) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["AccountDefault"] = value.get("account_default", False)
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProtectConfigurationResult:
    out: CreateProtectConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationArn") is not None:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateProtectConfigurationResult.protect_configuration_arn required"
        )
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "CreateProtectConfigurationResult.protect_configuration_id required"
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
            "CreateProtectConfigurationResult.created_timestamp required"
        )
    if data.get("AccountDefault") is not None:
        out["account_default"] = data["AccountDefault"]
    else:
        out["account_default"] = False
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
