"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTimeSeriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.time_series_summaries
    import capo_iotsitewise.types.workspace_name


class ListTimeSeriesResponse(TypedDict, closed=True):
    time_series_summaries: (
        "capo_iotsitewise.types.time_series_summaries.TimeSeriesSummaries"
    )
    """<p>One or more time series summaries to list.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.time_series_summaries

    out["TimeSeriesSummaries"] = (
        capo_iotsitewise.types.time_series_summaries.serialize_json(
            value["time_series_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> ListTimeSeriesResponse:
    out: ListTimeSeriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("TimeSeriesSummaries") is not None:
        import capo_iotsitewise.types.time_series_summaries

        out["time_series_summaries"] = (
            capo_iotsitewise.types.time_series_summaries.deserialize_json(
                data["TimeSeriesSummaries"]
            )
        )
    else:
        out["time_series_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    return out
