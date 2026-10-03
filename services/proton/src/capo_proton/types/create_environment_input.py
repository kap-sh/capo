"""Generated from Smithy shape ``com.amazonaws.proton#CreateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.description
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.repository_branch_input
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.spec_contents
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part


class CreateEnvironmentInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Environment Templates</a> in the <i>Proton User Guide</i>.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the environment template.</p>"""
    template_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The minor version of the environment template.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the environment that's being created and deployed.</p>"""
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> in the <i>Proton User Guide</i>.</p>"""
    proton_service_role_arn: NotRequired["capo_proton.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>"""
    environment_account_connection_id: NotRequired[
        "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    ]
    """<p>The ID of the environment account connection that you provide if you're provisioning your environment infrastructure resources to an environment account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton environment. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    provisioning_repository: NotRequired[
        "capo_proton.types.repository_branch_input.RepositoryBranchInput"
    ]
    """<p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To use self-managed provisioning for the environment, specify this parameter and omit the <code>environmentAccountConnectionId</code> and <code>protonServiceRoleArn</code> parameters.</p>"""
    component_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with this environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p> <p>To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the <code>environmentAccountConnectionId</code> or <code>codebuildRoleArn</code> parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    if "description" in value:
        out["description"] = value["description"]
    out["spec"] = value["spec"]
    if "proton_service_role_arn" in value:
        out["protonServiceRoleArn"] = value["proton_service_role_arn"]
    if "environment_account_connection_id" in value:
        out["environmentAccountConnectionId"] = value[
            "environment_account_connection_id"
        ]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
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


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentInput:
    out: CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentInput.name required")
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateEnvironmentInput.template_name required")
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError(
            "CreateEnvironmentInput.template_major_version required"
        )
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    else:
        raise DeserializationError("CreateEnvironmentInput.spec required")
    if data.get("protonServiceRoleArn") is not None:
        out["proton_service_role_arn"] = data["protonServiceRoleArn"]
    if data.get("environmentAccountConnectionId") is not None:
        out["environment_account_connection_id"] = data[
            "environmentAccountConnectionId"
        ]
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
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
