"""Generated from Smithy shape ``com.amazonaws.omics#UpdateWorkflowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.readme_markdown
    import capo_omics.types.storage_type
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_version_description
    import capo_omics.types.workflow_version_name


class UpdateWorkflowVersionRequest(TypedDict, closed=True):
    workflow_id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>"""
    version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName"
    """<p>The name of the workflow version.</p>"""
    description: NotRequired[
        "capo_omics.types.workflow_version_description.WorkflowVersionDescription"
    ]
    """<p>Description of the workflow version.</p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The default storage type for runs that use this workflow version. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>in the <i>Amazon Web Services HealthOmics User Guide</i> </i>.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The default static storage capacity (in gibibytes) for runs that use this workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>"""
    readme_markdown: NotRequired["capo_omics.types.readme_markdown.ReadmeMarkdown"]
    """<p>The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "readme_markdown" in value:
        out["readmeMarkdown"] = value["readme_markdown"]
    return out


def deserialize_json(data: dict) -> UpdateWorkflowVersionRequest:
    out: UpdateWorkflowVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("storageCapacity") is not None:
        out["storage_capacity"] = data["storageCapacity"]
    if data.get("readmeMarkdown") is not None:
        out["readme_markdown"] = data["readmeMarkdown"]
    return out
