"""Generated from Smithy shape ``com.amazonaws.datasync#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.max_results
    import capo_datasync.types.next_token
    import capo_datasync.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the resource that you want tag information on.</p>"""
    max_results: NotRequired["capo_datasync.types.max_results.MaxResults"]
    """<p>Specifies how many results that you want in the response.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>Specifies an opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
