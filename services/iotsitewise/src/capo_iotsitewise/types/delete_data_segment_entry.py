"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteDataSegmentEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.time_in_nanos


class DeleteDataSegmentEntry(TypedDict, closed=True):
    time_series_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the time series.</p>"""
    start_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision start time of the data segment to delete.</p>"""
    end_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision end time of the data segment to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSegmentEntry) -> dict:
    out: dict = {}
    out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types.time_in_nanos

    out["startTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataSegmentEntry:
    out: DeleteDataSegmentEntry = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("DeleteDataSegmentEntry.start_timestamp required")
    if data.get("endTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTimestamp"]
        )
    else:
        raise DeserializationError("DeleteDataSegmentEntry.end_timestamp required")
    return out
