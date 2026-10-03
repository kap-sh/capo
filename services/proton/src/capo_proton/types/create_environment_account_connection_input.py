"""Generated from Smithy shape ``com.amazonaws.proton#CreateEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.aws_account_id
    import capo_proton.types.client_token
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.tag_list


class CreateEnvironmentAccountConnectionInput(TypedDict, closed=True):
    client_token: NotRequired["capo_proton.types.client_token.ClientToken"]
    """<p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>"""
    management_account_id: "capo_proton.types.aws_account_id.AwsAccountId"
    """<p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>"""
    role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the Proton environment that's created in the associated management account.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    component_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["managementAccountId"] = value["management_account_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    out["environmentName"] = value["environment_name"]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    if "codebuild_role_arn" in value:
        out["codebuildRoleArn"] = value["codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentAccountConnectionInput:
    out: CreateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("managementAccountId") is not None:
        out["management_account_id"] = data["managementAccountId"]
    else:
        raise DeserializationError(
            "CreateEnvironmentAccountConnectionInput.management_account_id required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError(
            "CreateEnvironmentAccountConnectionInput.environment_name required"
        )
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if data.get("componentRoleArn") is not None:
        out["component_role_arn"] = data["componentRoleArn"]
    if data.get("codebuildRoleArn") is not None:
        out["codebuild_role_arn"] = data["codebuildRoleArn"]
    return out
