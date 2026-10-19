"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListMembershipsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to ListMemberships. When provided in this manner, the API fetches the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p>Request element for ListMemberships to limit the number of responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListMembershipsRequest:
    out: ListMembershipsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
