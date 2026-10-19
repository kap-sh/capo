"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecycleExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListLifecycleExecutionsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""
    resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to list lifecycle executions. Specify a lifecycle policy ARN to list its executions, or an image build version ARN to list the executions that <a>StartResourceStateUpdate</a> started for that image. Other ARN types aren't valid for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecycleExecutionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ListLifecycleExecutionsRequest:
    out: ListLifecycleExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
