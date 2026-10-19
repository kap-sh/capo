"""Generated from Smithy shape ``com.amazonaws.xray#TelemetryRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.backend_connection_errors
    import capo_xray.types.nullable_integer
    import capo_xray.types.timestamp


class TelemetryRecord(TypedDict, closed=True):
    timestamp: "capo_xray.types.timestamp.Timestamp"
    """<p></p>"""
    segments_received_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_sent_count: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p></p>"""
    segments_spillover_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_rejected_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    backend_connection_errors: NotRequired[
        "capo_xray.types.backend_connection_errors.BackendConnectionErrors"
    ]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRecord) -> dict:
    out: dict = {}
    import capo_xray.types.timestamp

    out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    if "segments_received_count" in value:
        out["SegmentsReceivedCount"] = value["segments_received_count"]
    if "segments_sent_count" in value:
        out["SegmentsSentCount"] = value["segments_sent_count"]
    if "segments_spillover_count" in value:
        out["SegmentsSpilloverCount"] = value["segments_spillover_count"]
    if "segments_rejected_count" in value:
        out["SegmentsRejectedCount"] = value["segments_rejected_count"]
    if "backend_connection_errors" in value:
        import capo_xray.types.backend_connection_errors

        out["BackendConnectionErrors"] = (
            capo_xray.types.backend_connection_errors.serialize_json(
                value["backend_connection_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryRecord:
    out: TelemetryRecord = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("SegmentsReceivedCount") is not None:
        out["segments_received_count"] = data["SegmentsReceivedCount"]
    if data.get("SegmentsSentCount") is not None:
        out["segments_sent_count"] = data["SegmentsSentCount"]
    if data.get("SegmentsSpilloverCount") is not None:
        out["segments_spillover_count"] = data["SegmentsSpilloverCount"]
    if data.get("SegmentsRejectedCount") is not None:
        out["segments_rejected_count"] = data["SegmentsRejectedCount"]
    if data.get("BackendConnectionErrors") is not None:
        import capo_xray.types.backend_connection_errors

        out["backend_connection_errors"] = (
            capo_xray.types.backend_connection_errors.deserialize_json(
                data["BackendConnectionErrors"]
            )
        )
    return out
