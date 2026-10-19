"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.filter_expression
    import capo_xray.types.nullable_boolean
    import capo_xray.types.sampling_strategy
    import capo_xray.types.string
    import capo_xray.types.time_range_type
    import capo_xray.types.timestamp


class GetTraceSummariesRequest(TypedDict, closed=True):
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The start of the time frame for which to retrieve traces.</p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The end of the time frame for which to retrieve traces.</p>"""
    time_range_type: NotRequired["capo_xray.types.time_range_type.TimeRangeType"]
    """<p>Query trace summaries by TraceId (trace start time), Event (trace update time), or Service (trace segment end time).</p>"""
    sampling: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>Set to <code>true</code> to get summaries for only a subset of available traces.</p>"""
    sampling_strategy: NotRequired["capo_xray.types.sampling_strategy.SamplingStrategy"]
    """<p>A parameter to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.</p>"""
    filter_expression: NotRequired["capo_xray.types.filter_expression.FilterExpression"]
    """<p>Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Specify the pagination token returned by a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceSummariesRequest) -> dict:
    out: dict = {}
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "time_range_type" in value:
        import capo_xray.types.time_range_type

        out["TimeRangeType"] = capo_xray.types.time_range_type.serialize_json(
            value["time_range_type"]
        )
    if "sampling" in value:
        out["Sampling"] = value["sampling"]
    if "sampling_strategy" in value:
        import capo_xray.types.sampling_strategy

        out["SamplingStrategy"] = capo_xray.types.sampling_strategy.serialize_json(
            value["sampling_strategy"]
        )
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTraceSummariesRequest:
    out: GetTraceSummariesRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("TimeRangeType") is not None:
        import capo_xray.types.time_range_type

        out["time_range_type"] = capo_xray.types.time_range_type.deserialize_json(
            data["TimeRangeType"]
        )
    if data.get("Sampling") is not None:
        out["sampling"] = data["Sampling"]
    if data.get("SamplingStrategy") is not None:
        import capo_xray.types.sampling_strategy

        out["sampling_strategy"] = capo_xray.types.sampling_strategy.deserialize_json(
            data["SamplingStrategy"]
        )
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
