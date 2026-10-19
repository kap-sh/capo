"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.max_results
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of tags to return.</p>"""
    resource_arn: "capo_iotthingsgraph.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource whose tags are to be returned.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The token that specifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["resourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
