"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AssociateProtectConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id


class AssociateProtectConfigurationResult(TypedDict, closed=True):
    configuration_set_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the configuration set.</p>"""
    configuration_set_name: (
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the ConfigurationSet.</p>"""
    protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateProtectConfigurationResult) -> dict:
    out: dict = {}
    out["ConfigurationSetArn"] = value["configuration_set_arn"]
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateProtectConfigurationResult:
    out: AssociateProtectConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetArn") is not None:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    else:
        out["configuration_set_arn"] = ""
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        out["configuration_set_name"] = ""
    if data.get("ProtectConfigurationArn") is not None:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        out["protect_configuration_arn"] = ""
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    return out
