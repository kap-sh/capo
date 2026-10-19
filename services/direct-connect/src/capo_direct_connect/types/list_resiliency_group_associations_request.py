"""Generated from Smithy shape ``com.amazonaws.directconnect#ListResiliencyGroupAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.resiliency_group_id


class ListResiliencyGroupAssociationsRequest(TypedDict, closed=True):
    resiliency_group_id: (
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    )
    """<p>The ID of the resiliency group.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResiliencyGroupAssociationsRequest) -> dict:
    out: dict = {}
    out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResiliencyGroupAssociationsRequest:
    out: ListResiliencyGroupAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    else:
        out["resiliency_group_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
