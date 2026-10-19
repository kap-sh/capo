"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDashboardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dashboard_summaries
    import capo_iotsitewise.types.next_token


class ListDashboardsResponse(TypedDict, closed=True):
    dashboard_summaries: "capo_iotsitewise.types.dashboard_summaries.DashboardSummaries"
    """<p>A list that summarizes each dashboard in the project.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.dashboard_summaries

    out["dashboardSummaries"] = (
        capo_iotsitewise.types.dashboard_summaries.serialize_json(
            value["dashboard_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDashboardsResponse:
    out: ListDashboardsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dashboardSummaries") is not None:
        import capo_iotsitewise.types.dashboard_summaries

        out["dashboard_summaries"] = (
            capo_iotsitewise.types.dashboard_summaries.deserialize_json(
                data["dashboardSummaries"]
            )
        )
    else:
        out["dashboard_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
