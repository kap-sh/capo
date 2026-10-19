"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecycleExecutionResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution_id
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListLifecycleExecutionResourcesRequest(TypedDict, closed=True):
    lifecycle_execution_id: (
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    )
    """<p>The unique identifier for a runtime instance of the lifecycle policy.</p>"""
    parent_resource_id: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of an image build version to get the output resources for, such as AMIs or container images in Amazon ECR. You can get this value from the <code>resourceId</code> in the top-level response. If you leave this property empty, the response lists the Image Builder resources that the lifecycle execution identified for lifecycle actions. If the image build version that you specify in <code>parentResourceId</code> wasn't part of this lifecycle execution, the response contains an empty list.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecycleExecutionResourcesRequest) -> dict:
    out: dict = {}
    out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "parent_resource_id" in value:
        out["parentResourceId"] = value["parent_resource_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLifecycleExecutionResourcesRequest:
    out: ListLifecycleExecutionResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleExecutionId") is not None:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    else:
        out["lifecycle_execution_id"] = ""
    if data.get("parentResourceId") is not None:
        out["parent_resource_id"] = data["parentResourceId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
