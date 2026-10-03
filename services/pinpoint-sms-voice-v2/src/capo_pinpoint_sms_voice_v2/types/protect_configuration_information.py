"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id


class ProtectConfigurationInformation(TypedDict, closed=True):
    protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the protect configuration was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    account_default: "bool"
    """<p>This is true if the protect configuration is set as your account default protect configuration.</p>"""
    deletion_protection_enabled: "bool"
    """<p>The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtectConfigurationInformation) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ProtectConfigurationInformation:
    out: ProtectConfigurationInformation = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationArn") is not None:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "ProtectConfigurationInformation.protect_configuration_arn required"
        )
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "ProtectConfigurationInformation.protect_configuration_id required"
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
            "ProtectConfigurationInformation.created_timestamp required"
        )
    if data.get("AccountDefault") is not None:
        out["account_default"] = data["AccountDefault"]
    else:
        out["account_default"] = False
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    return out
