"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeLagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token


class DescribeLagsRequest(TypedDict, closed=True):
    lag_id: NotRequired["capo_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLagsRequest) -> dict:
    out: dict = {}
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLagsRequest:
    out: DescribeLagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeLagsRequest) -> dict:
    out: dict = {}
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeLagsRequest:
    out: DescribeLagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
