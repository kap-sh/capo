"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowBuildVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer
    import capo_imagebuilder.types.workflow_wildcard_version_arn


class ListWorkflowBuildVersionsRequest(TypedDict, closed=True):
    workflow_version_arn: NotRequired[
        "capo_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource for which to get a list of build versions. The version segments can contain wildcards (<code>x</code>) to match multiple versions of the workflow. If you don't specify an ARN, the response lists build versions for all of the workflows in your account.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request. If you don't specify a value, Image Builder returns up to 25 items. The largest page size that you can request is 100 items. A page can contain fewer items than the maximum, with a <code>nextToken</code> to continue paging.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowBuildVersionsRequest) -> dict:
    out: dict = {}
    if "workflow_version_arn" in value:
        out["workflowVersionArn"] = value["workflow_version_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowBuildVersionsRequest:
    out: ListWorkflowBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("workflowVersionArn") is not None:
        out["workflow_version_arn"] = data["workflowVersionArn"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
