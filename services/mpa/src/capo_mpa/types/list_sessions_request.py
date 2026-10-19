"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.filters
    import capo_mpa.types.max_results
    import capo_mpa.types.token


class ListSessionsRequest(TypedDict, closed=True):
    approval_team_arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    max_results: NotRequired["capo_mpa.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""
    next_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    filters: NotRequired["capo_mpa.types.filters.Filters"]
    """<p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_mpa.types.filters

        out["Filters"] = capo_mpa.types.filters.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_mpa.types.filters

        out["filters"] = capo_mpa.types.filters.deserialize_json(data["Filters"])
    return out
