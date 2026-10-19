"""Generated from Smithy shape ``com.amazonaws.proton#CreateTemplateSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.resource_name
    import capo_proton.types.subdirectory
    import capo_proton.types.template_type


class CreateTemplateSyncConfigInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of your registered template.</p>"""
    template_type: "capo_proton.types.template_type.TemplateType"
    """<p>The type of the registered template.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The provider type for your repository.</p>"""
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name (for example, <code>myrepos/myrepo</code>).</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch for your template.</p>"""
    subdirectory: NotRequired["capo_proton.types.subdirectory.Subdirectory"]
    """<p>A repository subdirectory path to your template bundle directory. When included, Proton limits the template bundle search to this repository directory.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTemplateSyncConfigInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    if "subdirectory" in value:
        out["subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTemplateSyncConfigInput:
    out: CreateTemplateSyncConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("templateType") is not None:
        out["template_type"] = data["templateType"]
    else:
        out["template_type"] = ""
    if data.get("repositoryProvider") is not None:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        out["repository_provider"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        out["branch"] = ""
    if data.get("subdirectory") is not None:
        out["subdirectory"] = data["subdirectory"]
    return out
