"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TimeSeriesDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.datum
    import capo_timestream_query.types.timestamp


class TimeSeriesDataPoint(TypedDict, closed=True):
    time: "capo_timestream_query.types.timestamp.Timestamp"
    """<p>The timestamp when the measure value was collected.</p>"""
    value: "capo_timestream_query.types.datum.Datum"
    """<p>The measure value for the data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeSeriesDataPoint) -> dict:
    out: dict = {}
    out["Time"] = value["time"]
    import capo_timestream_query.types.datum

    out["Value"] = capo_timestream_query.types.datum.serialize_aws_json_1_0(
        value["value"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeSeriesDataPoint:
    out: TimeSeriesDataPoint = {}  # type: ignore[typeddict-item]
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    else:
        out["time"] = ""
    if data.get("Value") is not None:
        import capo_timestream_query.types.datum

        out["value"] = capo_timestream_query.types.datum.deserialize_aws_json_1_0(
            data["Value"]
        )
    else:
        raise DeserializationError("TimeSeriesDataPoint.value required")
    return out
