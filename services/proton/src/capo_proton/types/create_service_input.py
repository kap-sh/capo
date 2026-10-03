"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.description
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_id
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part


class CreateServiceInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The service name.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the Proton service.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template that's used to create the service.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the service template that was used to create the service.</p>"""
    template_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The minor version of the service template that was used to create the service.</p>"""
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>A link to a spec file that provides inputs as defined in the service template bundle schema file. The spec file is in YAML format. <i>Don’t</i> include pipeline inputs in the spec if your service template <i>doesn’t</i> include a service pipeline. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html">Create a service</a> in the <i>Proton User Guide</i>.</p>"""
    repository_connection_arn: NotRequired["capo_proton.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the repository connection. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol">Setting up an AWS CodeStar connection</a> in the <i>Proton User Guide</i>. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>"""
    repository_id: NotRequired["capo_proton.types.repository_id.RepositoryId"]
    """<p>The ID of the code repository. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>"""
    branch_name: NotRequired["capo_proton.types.git_branch_name.GitBranchName"]
    """<p>The name of the code repository branch that holds the code that's deployed in Proton. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton service. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    out["spec"] = value["spec"]
    if "repository_connection_arn" in value:
        out["repositoryConnectionArn"] = value["repository_connection_arn"]
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceInput:
    out: CreateServiceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateServiceInput.template_name required")
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError("CreateServiceInput.template_major_version required")
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    else:
        raise DeserializationError("CreateServiceInput.spec required")
    if data.get("repositoryConnectionArn") is not None:
        out["repository_connection_arn"] = data["repositoryConnectionArn"]
    if data.get("repositoryId") is not None:
        out["repository_id"] = data["repositoryId"]
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out
