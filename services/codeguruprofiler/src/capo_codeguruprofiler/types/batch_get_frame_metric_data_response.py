"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#BatchGetFrameMetricDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.aggregation_period
    import capo_codeguruprofiler.types.frame_metric_data
    import capo_codeguruprofiler.types.list_of_timestamps
    import capo_codeguruprofiler.types.timestamp
    import capo_codeguruprofiler.types.unprocessed_end_time_map


class BatchGetFrameMetricDataResponse(TypedDict, closed=True):
    start_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    resolution: "capo_codeguruprofiler.types.aggregation_period.AggregationPeriod"
    """<p>Resolution or granularity of the profile data used to generate the time series. This is the value used to jump through time steps in a time series. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>"""
    end_times: "capo_codeguruprofiler.types.list_of_timestamps.ListOfTimestamps"
    """<p> List of instances, or time steps, in the time series. For example, if the <code>period</code> is one day (<code>PT24H)</code>), and the <code>resolution</code> is five minutes (<code>PT5M</code>), then there are 288 <code>endTimes</code> in the list that are each five minutes appart. </p>"""
    unprocessed_end_times: (
        "capo_codeguruprofiler.types.unprocessed_end_time_map.UnprocessedEndTimeMap"
    )
    """<p>List of instances which remained unprocessed. This will create a missing time step in the list of end times.</p>"""
    frame_metric_data: "capo_codeguruprofiler.types.frame_metric_data.FrameMetricData"
    """<p>Details of the metrics to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFrameMetricDataResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.timestamp

    out["startTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_codeguruprofiler.types.timestamp

    out["endTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["end_time"]
    )
    out["resolution"] = value["resolution"]
    import capo_codeguruprofiler.types.list_of_timestamps

    out["endTimes"] = capo_codeguruprofiler.types.list_of_timestamps.serialize_json(
        value["end_times"]
    )
    import capo_codeguruprofiler.types.unprocessed_end_time_map

    out["unprocessedEndTimes"] = (
        capo_codeguruprofiler.types.unprocessed_end_time_map.serialize_json(
            value["unprocessed_end_times"]
        )
    )
    import capo_codeguruprofiler.types.frame_metric_data

    out["frameMetricData"] = (
        capo_codeguruprofiler.types.frame_metric_data.serialize_json(
            value["frame_metric_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFrameMetricDataResponse:
    out: BatchGetFrameMetricDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["start_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["end_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("resolution") is not None:
        out["resolution"] = data["resolution"]
    else:
        out["resolution"] = ""
    if data.get("endTimes") is not None:
        import capo_codeguruprofiler.types.list_of_timestamps

        out["end_times"] = (
            capo_codeguruprofiler.types.list_of_timestamps.deserialize_json(
                data["endTimes"]
            )
        )
    else:
        out["end_times"] = []
    if data.get("unprocessedEndTimes") is not None:
        import capo_codeguruprofiler.types.unprocessed_end_time_map

        out["unprocessed_end_times"] = (
            capo_codeguruprofiler.types.unprocessed_end_time_map.deserialize_json(
                data["unprocessedEndTimes"]
            )
        )
    else:
        out["unprocessed_end_times"] = {}
    if data.get("frameMetricData") is not None:
        import capo_codeguruprofiler.types.frame_metric_data

        out["frame_metric_data"] = (
            capo_codeguruprofiler.types.frame_metric_data.deserialize_json(
                data["frameMetricData"]
            )
        )
    else:
        out["frame_metric_data"] = []
    return out
