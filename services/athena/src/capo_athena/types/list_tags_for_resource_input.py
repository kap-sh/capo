"""Generated from Smithy shape ``com.amazonaws.athena#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.amazon_resource_name
    import capo_athena.types.max_tags_count
    import capo_athena.types.token


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>Lists the tags for the resource with the specified ARN.</p>"""
    next_token: NotRequired["capo_athena.types.token.Token"]
    """<p>The token for the next set of results, or null if there are no additional results for this request, where the request lists the tags for the resource with the specified ARN.</p>"""
    max_results: NotRequired["capo_athena.types.max_tags_count.MaxTagsCount"]
    """<p>The maximum number of results to be returned per request that lists the tags for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
