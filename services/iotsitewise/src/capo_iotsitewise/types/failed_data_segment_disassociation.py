"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FailedDataSegmentDisassociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_segment_error_code
    import capo_iotsitewise.types.data_segment_error_message
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.time_series_id


class FailedDataSegmentDisassociation(TypedDict, closed=True):
    source_dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the source dataset.</p>"""
    time_series_id: "capo_iotsitewise.types.time_series_id.TimeSeriesId"
    """<p>The ID of the time series.</p>"""
    start_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision start time of the data segment.</p>"""
    end_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision end time of the data segment.</p>"""
    error_code: "capo_iotsitewise.types.data_segment_error_code.DataSegmentErrorCode"
    """<p>The error code for the failed disassociation.</p>"""
    error_message: (
        "capo_iotsitewise.types.data_segment_error_message.DataSegmentErrorMessage"
    )
    """<p>The error message for the failed disassociation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedDataSegmentDisassociation) -> dict:
    out: dict = {}
    out["sourceDatasetId"] = value["source_dataset_id"]
    out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types.time_in_nanos

    out["startTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_timestamp"]
    )
    import capo_iotsitewise.types.data_segment_error_code

    out["errorCode"] = capo_iotsitewise.types.data_segment_error_code.serialize_json(
        value["error_code"]
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedDataSegmentDisassociation:
    out: FailedDataSegmentDisassociation = {}  # type: ignore[typeddict-item]
    if data.get("sourceDatasetId") is not None:
        out["source_dataset_id"] = data["sourceDatasetId"]
    else:
        out["source_dataset_id"] = ""
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
        raise DeserializationError(
            "FailedDataSegmentDisassociation.start_timestamp required"
        )
    if data.get("endTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTimestamp"]
        )
    else:
        raise DeserializationError(
            "FailedDataSegmentDisassociation.end_timestamp required"
        )
    if data.get("errorCode") is not None:
        import capo_iotsitewise.types.data_segment_error_code

        out["error_code"] = (
            capo_iotsitewise.types.data_segment_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_iotsitewise.types.data_segment_error_code.DataSegmentErrorCode", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
