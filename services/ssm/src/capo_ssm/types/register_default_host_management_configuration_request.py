"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterDefaultHostManagementConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.dhmc_permission_model
    import capo_ssm.types.dhmc_role_arn


class RegisterDefaultHostManagementConfigurationRequest(TypedDict, closed=True):
    permission_model: "capo_ssm.types.dhmc_permission_model.DHMCPermissionModel"
    """<p>The permission model that determines how the IAM role for Default Host Management Configuration is provided.</p> <p>The permission model can be one of the following values:</p> <dl> <dt>SERVICE_MANAGED</dt> <dd> <p>Amazon Web Services Systems Manager creates and manages the role on your behalf.</p> </dd> <dt>SELF_MANAGED</dt> <dd> <p>You provide the role to register in <code>RoleArn</code>.</p> </dd> </dl>"""
    role_arn: NotRequired["capo_ssm.types.dhmc_role_arn.DHMCRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the self-managed IAM role that you register for Default Host Management Configuration. The requirement for this value depends on the permission model:</p> <ul> <li> <p>If <code>PermissionModel</code> is <code>SELF_MANAGED</code>, this value is required.</p> </li> <li> <p>If <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>, this value must not be set.</p> </li> </ul>"""
    overwrite: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Specifies whether to override the role that is currently registered for Default Host Management Configuration. The default is <code>false</code>, which acts as a guardrail against accidentally replacing an existing configuration. Set this to <code>true</code> to replace the currently registered role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: RegisterDefaultHostManagementConfigurationRequest,
) -> dict:
    out: dict = {}
    import capo_ssm.types.dhmc_permission_model

    out["PermissionModel"] = (
        capo_ssm.types.dhmc_permission_model.serialize_aws_json_1_1(
            value["permission_model"]
        )
    )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "overwrite" in value:
        out["Overwrite"] = value["overwrite"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> RegisterDefaultHostManagementConfigurationRequest:
    out: RegisterDefaultHostManagementConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PermissionModel") is not None:
        import capo_ssm.types.dhmc_permission_model

        out["permission_model"] = (
            capo_ssm.types.dhmc_permission_model.deserialize_aws_json_1_1(
                data["PermissionModel"]
            )
        )
    else:
        import typing

        out["permission_model"] = typing.cast(
            "capo_ssm.types.dhmc_permission_model.DHMCPermissionModel", ""
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Overwrite") is not None:
        out["overwrite"] = data["Overwrite"]
    return out
