"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.role_arn


class UpdateEnvironmentAccountConnectionInput(TypedDict, closed=True):
    id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection to update.</p>"""
    role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>"""
    component_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    if "codebuild_role_arn" in value:
        out["codebuildRoleArn"] = value["codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentAccountConnectionInput:
    out: UpdateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentAccountConnectionInput.id required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("componentRoleArn") is not None:
        out["component_role_arn"] = data["componentRoleArn"]
    if data.get("codebuildRoleArn") is not None:
        out["codebuild_role_arn"] = data["codebuildRoleArn"]
    return out
