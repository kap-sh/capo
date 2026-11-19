"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsPerformanceMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.query_data
    import capo_networkflowmonitor.types.query_fields


class GetQueryResultsPerformanceMonitorOutput(TypedDict, closed=True):
    fields: "capo_networkflowmonitor.types.query_fields.QueryFields"
    """<p>The columns that the query returns, in the order that the values for each row appear in <code>data</code>.</p>"""
    data: "capo_networkflowmonitor.types.query_data.QueryData"
    """<p>The results of the query. Each row contains the values for the columns that <code>fields</code> describes, in the same order.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsPerformanceMonitorOutput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.query_fields

    out["fields"] = capo_networkflowmonitor.types.query_fields.serialize_json(
        value["fields"]
    )
    import capo_networkflowmonitor.types.query_data

    out["data"] = capo_networkflowmonitor.types.query_data.serialize_json(value["data"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetQueryResultsPerformanceMonitorOutput:
    out: GetQueryResultsPerformanceMonitorOutput = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_networkflowmonitor.types.query_fields

        out["fields"] = capo_networkflowmonitor.types.query_fields.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("data") is not None:
        import capo_networkflowmonitor.types.query_data

        out["data"] = capo_networkflowmonitor.types.query_data.deserialize_json(
            data["data"]
        )
    else:
        out["data"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
