"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.max_size
    import capo_cloudhsm_v2.types.next_token
    import capo_cloudhsm_v2.types.resource_id


class ListTagsRequest(TypedDict, closed=True):
    resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId"
    """<p>The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""
    next_token: NotRequired["capo_cloudhsm_v2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more tags.</p>"""
    max_results: NotRequired["capo_cloudhsm_v2.types.max_size.MaxSize"]
    """<p>The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
