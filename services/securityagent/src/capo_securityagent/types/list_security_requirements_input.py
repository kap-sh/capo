"""Generated from Smithy shape ``com.amazonaws.securityagent#ListSecurityRequirementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.security_requirement_pack_id


class ListSecurityRequirementsInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to list requirements for.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>The pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityRequirementsInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListSecurityRequirementsInput:
    out: ListSecurityRequirementsInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
