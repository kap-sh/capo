"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterDefaultHostManagementConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.dhmc_role_arn


class RegisterDefaultHostManagementConfigurationResult(TypedDict, closed=True):
    role_arn: NotRequired["capo_ssm.types.dhmc_role_arn.DHMCRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role registered for Default Host Management Configuration. The value depends on the permission model:</p> <dl> <dt>SERVICE_MANAGED</dt> <dd> <p>The ARN of the role that Amazon Web Services Systems Manager created in the IAM reserved path.</p> </dd> <dt>SELF_MANAGED</dt> <dd> <p>The <code>RoleArn</code> that you provided.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: RegisterDefaultHostManagementConfigurationResult,
) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> RegisterDefaultHostManagementConfigurationResult:
    out: RegisterDefaultHostManagementConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
