"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListWorkloadIdentitiesRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListWorkloadIdentitiesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>Pagination token.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadIdentitiesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListWorkloadIdentitiesRequest:
    out: ListWorkloadIdentitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
