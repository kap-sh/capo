"""Generated from Smithy shape ``com.amazonaws.omics#UpdateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.readme_markdown
    import capo_omics.types.storage_type
    import capo_omics.types.workflow_description
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_name


class UpdateWorkflowRequest(TypedDict, closed=True):
    id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""
    name: NotRequired["capo_omics.types.workflow_name.WorkflowName"]
    """<p>A name for the workflow.</p>"""
    description: NotRequired[
        "capo_omics.types.workflow_description.WorkflowDescription"
    ]
    """<p>A description for the workflow.</p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html">Running workflows</a> in the <i>Amazon Web Services HealthOmics User Guide</i>. </p>"""
    storage_capacity: NotRequired["int"]
    """<p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. </p>"""
    readme_markdown: NotRequired["capo_omics.types.readme_markdown.ReadmeMarkdown"]
    """<p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "readme_markdown" in value:
        out["readmeMarkdown"] = value["readme_markdown"]
    return out


def deserialize_json(data: dict) -> UpdateWorkflowRequest:
    out: UpdateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("storageCapacity") is not None:
        out["storage_capacity"] = data["storageCapacity"]
    if data.get("readmeMarkdown") is not None:
        out["readme_markdown"] = data["readmeMarkdown"]
    return out
