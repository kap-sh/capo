"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateFlywheelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.update_data_security_config


class UpdateFlywheelRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p>The Amazon Resource Number (ARN) of the flywheel to update.</p>"""
    active_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the active model version.</p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.</p>"""
    data_security_config: NotRequired[
        "capo_comprehend.types.update_data_security_config.UpdateDataSecurityConfig"
    ]
    """<p>Flywheel data security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFlywheelRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "data_security_config" in value:
        import capo_comprehend.types.update_data_security_config

        out["DataSecurityConfig"] = (
            capo_comprehend.types.update_data_security_config.serialize_aws_json_1_1(
                value["data_security_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFlywheelRequest:
    out: UpdateFlywheelRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        out["flywheel_arn"] = ""
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("DataSecurityConfig") is not None:
        import capo_comprehend.types.update_data_security_config

        out["data_security_config"] = (
            capo_comprehend.types.update_data_security_config.deserialize_aws_json_1_1(
                data["DataSecurityConfig"]
            )
        )
    return out
