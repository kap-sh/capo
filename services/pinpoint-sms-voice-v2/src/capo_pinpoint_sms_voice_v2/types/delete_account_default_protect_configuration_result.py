"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteAccountDefaultProtectConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id


class DeleteAccountDefaultProtectConfigurationResult(TypedDict, closed=True):
    default_protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the account default protect configuration.</p>"""
    default_protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier of the account default protect configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DeleteAccountDefaultProtectConfigurationResult,
) -> dict:
    out: dict = {}
    out["DefaultProtectConfigurationArn"] = value["default_protect_configuration_arn"]
    out["DefaultProtectConfigurationId"] = value["default_protect_configuration_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DeleteAccountDefaultProtectConfigurationResult:
    out: DeleteAccountDefaultProtectConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("DefaultProtectConfigurationArn") is not None:
        out["default_protect_configuration_arn"] = data[
            "DefaultProtectConfigurationArn"
        ]
    else:
        out["default_protect_configuration_arn"] = ""
    if data.get("DefaultProtectConfigurationId") is not None:
        out["default_protect_configuration_id"] = data["DefaultProtectConfigurationId"]
    else:
        out["default_protect_configuration_id"] = ""
    return out
