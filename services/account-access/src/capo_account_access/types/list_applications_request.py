"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListApplicationsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListApplicationsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>Specifies the maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
