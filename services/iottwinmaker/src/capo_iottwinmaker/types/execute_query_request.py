"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ExecuteQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.query_service_max_results
    import capo_iottwinmaker.types.query_statement


class ExecuteQueryRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    query_statement: "capo_iottwinmaker.types.query_statement.QueryStatement"
    """<p>The query statement.</p>"""
    max_results: NotRequired[
        "capo_iottwinmaker.types.query_service_max_results.QueryServiceMaxResults"
    ]
    """<p>The maximum number of results to return at one time. The default is 50.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteQueryRequest) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["queryStatement"] = value["query_statement"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExecuteQueryRequest:
    out: ExecuteQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("queryStatement") is not None:
        out["query_statement"] = data["queryStatement"]
    else:
        out["query_statement"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
