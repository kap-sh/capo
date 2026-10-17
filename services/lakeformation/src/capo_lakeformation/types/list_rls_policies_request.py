"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListRLSPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.token


class ListRLSPoliciesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of row-level security policies to return in a single response.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRLSPoliciesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRLSPoliciesRequest:
    out: ListRLSPoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
