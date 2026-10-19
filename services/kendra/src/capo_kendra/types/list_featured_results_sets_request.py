"""Generated from Smithy shape ``com.amazonaws.kendra#ListFeaturedResultsSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.index_id
    import capo_kendra.types.max_results_integer_for_list_featured_results_sets_request
    import capo_kendra.types.next_token


class ListFeaturedResultsSetsRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used for featuring results.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of featured results sets.</p>"""
    max_results: NotRequired[
        "capo_kendra.types.max_results_integer_for_list_featured_results_sets_request.MaxResultsIntegerForListFeaturedResultsSetsRequest"
    ]
    """<p>The maximum number of featured results sets to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFeaturedResultsSetsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFeaturedResultsSetsRequest:
    out: ListFeaturedResultsSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
