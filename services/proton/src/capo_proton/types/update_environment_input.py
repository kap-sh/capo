"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.deployment_update_type
    import capo_proton.types.description
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.repository_branch_input
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.spec_contents
    import capo_proton.types.template_version_part


class UpdateEnvironmentInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment to update.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the environment update.</p>"""
    spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The formatted specification that defines the update.</p>"""
    template_major_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The major version of the environment to update.</p>"""
    template_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The minor version of the environment to update.</p>"""
    proton_service_role_arn: NotRequired["capo_proton.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make API calls to other services your behalf.</p>"""
    deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType"
    """<p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that is higher than the major version in use and a minor version (optional).</p> </dd> </dl>"""
    environment_account_connection_id: NotRequired[
        "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    ]
    """<p>The ID of the environment account connection.</p> <p>You can only update to a new environment account connection if it was created in the same environment account that the current environment account connection was created in and is associated with the current environment.</p>"""
    provisioning_repository: NotRequired[
        "capo_proton.types.repository_branch_input.RepositoryBranchInput"
    ]
    """<p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>"""
    component_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>The environment must have a <code>componentRoleArn</code> to allow directly defined components to be associated with the environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "spec" in value:
        out["spec"] = value["spec"]
    if "template_major_version" in value:
        out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    if "proton_service_role_arn" in value:
        out["protonServiceRoleArn"] = value["proton_service_role_arn"]
    out["deploymentType"] = value["deployment_type"]
    if "environment_account_connection_id" in value:
        out["environmentAccountConnectionId"] = value[
            "environment_account_connection_id"
        ]
    if "provisioning_repository" in value:
        import capo_proton.types.repository_branch_input

        out["provisioningRepository"] = (
            capo_proton.types.repository_branch_input.serialize_aws_json_1_0(
                value["provisioning_repository"]
            )
        )
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    if "codebuild_role_arn" in value:
        out["codebuildRoleArn"] = value["codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentInput:
    out: UpdateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateEnvironmentInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    if data.get("protonServiceRoleArn") is not None:
        out["proton_service_role_arn"] = data["protonServiceRoleArn"]
    if data.get("deploymentType") is not None:
        out["deployment_type"] = data["deploymentType"]
    else:
        raise DeserializationError("UpdateEnvironmentInput.deployment_type required")
    if data.get("environmentAccountConnectionId") is not None:
        out["environment_account_connection_id"] = data[
            "environmentAccountConnectionId"
        ]
    if data.get("provisioningRepository") is not None:
        import capo_proton.types.repository_branch_input

        out["provisioning_repository"] = (
            capo_proton.types.repository_branch_input.deserialize_aws_json_1_0(
                data["provisioningRepository"]
            )
        )
    if data.get("componentRoleArn") is not None:
        out["component_role_arn"] = data["componentRoleArn"]
    if data.get("codebuildRoleArn") is not None:
        out["codebuild_role_arn"] = data["codebuildRoleArn"]
    return out
