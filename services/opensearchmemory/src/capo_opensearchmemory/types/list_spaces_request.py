"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListSpacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.next_token


class ListSpacesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_opensearchmemory.types.max_results.MaxResults"]
    """<p>The maximum number of spaces to return, from 1 to 100. The default is 100.</p>"""
    next_token: NotRequired["capo_opensearchmemory.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSpacesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSpacesRequest:
    out: ListSpacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
