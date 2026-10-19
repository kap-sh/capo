"""Generated from Smithy shape ``com.amazonaws.xray#StartTraceRetrievalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.timestamp
    import capo_xray.types.trace_id_list_for_retrieval


class StartTraceRetrievalRequest(TypedDict, closed=True):
    trace_ids: "capo_xray.types.trace_id_list_for_retrieval.TraceIdListForRetrieval"
    """<p> Specify the trace IDs of the traces to be retrieved. </p>"""
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p> The start of the time range to retrieve traces. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC. </p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p> The end of the time range to retrieve traces. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTraceRetrievalRequest) -> dict:
    out: dict = {}
    import capo_xray.types.trace_id_list_for_retrieval

    out["TraceIds"] = capo_xray.types.trace_id_list_for_retrieval.serialize_json(
        value["trace_ids"]
    )
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> StartTraceRetrievalRequest:
    out: StartTraceRetrievalRequest = {}  # type: ignore[typeddict-item]
    if data.get("TraceIds") is not None:
        import capo_xray.types.trace_id_list_for_retrieval

        out["trace_ids"] = capo_xray.types.trace_id_list_for_retrieval.deserialize_json(
            data["TraceIds"]
        )
    else:
        out["trace_ids"] = []
    if data.get("StartTime") is not None:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
