"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_id
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.workspace_name


class SearchResult(TypedDict, closed=True):
    search_id: "capo_iotsitewise.types.search_id.SearchId"
    """<p>The identifier of the search that produced this result.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace the search ran against.</p>"""
    dataset_id: "capo_iotsitewise.types.dataset_id.DatasetId"
    """<p>The identifier of the dataset that contains the matching data.</p>"""
    time_series_id: "capo_iotsitewise.types.time_series_id.TimeSeriesId"
    """<p>The identifier of the time series that contains the matching data.</p>"""
    start_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The start of the matching time-series segment, in nanoseconds since the Unix epoch.</p>"""
    end_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The end of the matching time-series segment, in nanoseconds since the Unix epoch.</p>"""
    top_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The timestamp of the most relevant point within the matching segment, in nanoseconds since the Unix epoch.</p>"""
    score: "float"
    """<p>The relevance score of this result. Higher scores indicate a stronger match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResult) -> dict:
    out: dict = {}
    out["searchId"] = value["search_id"]
    out["workspaceName"] = value["workspace_name"]
    out["datasetId"] = value["dataset_id"]
    out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types.time_in_nanos

    out["startTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["topTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["top_timestamp"]
    )
    out["score"] = (
        "NaN"
        if value["score"] != value["score"]
        else "Infinity"
        if value["score"] == float("inf")
        else "-Infinity"
        if value["score"] == float("-inf")
        else value["score"]
    )
    return out


def deserialize_json(data: dict) -> SearchResult:
    out: SearchResult = {}  # type: ignore[typeddict-item]
    if data.get("searchId") is not None:
        out["search_id"] = data["searchId"]
    else:
        out["search_id"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    else:
        out["time_series_id"] = ""
    if data.get("startTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTimestamp"]
        )
    else:
        raise DeserializationError("SearchResult.start_timestamp required")
    if data.get("endTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTimestamp"]
        )
    else:
        raise DeserializationError("SearchResult.end_timestamp required")
    if data.get("topTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["top_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["topTimestamp"]
        )
    else:
        raise DeserializationError("SearchResult.top_timestamp required")
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0.0
    return out
