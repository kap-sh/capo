"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetCaptureDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.capture_blob
    import capo_iotsitewise.types.get_capture_data_next_token
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.video_data_type


class GetCaptureDataResponse(TypedDict, closed=True):
    data: "capo_iotsitewise.types.capture_blob.CaptureBlob"
    """<p>The binary video data.</p>"""
    start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The actual start time of the returned data.</p>"""
    end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The actual end time of the returned data.</p>"""
    data_type: "capo_iotsitewise.types.video_data_type.VideoDataType"
    """<p>The type of the returned data.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.get_capture_data_next_token.GetCaptureDataNextToken"
    ]
    """<p>The token used to retrieve the next chunk. Absent if no more data is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaptureDataResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.capture_blob

    out["data"] = capo_iotsitewise.types.capture_blob.serialize_json(value["data"])
    import capo_iotsitewise.types.time_in_nanos

    out["startTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_time"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_time"]
    )
    import capo_iotsitewise.types.video_data_type

    out["dataType"] = capo_iotsitewise.types.video_data_type.serialize_json(
        value["data_type"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCaptureDataResponse:
    out: GetCaptureDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_iotsitewise.types.capture_blob

        out["data"] = capo_iotsitewise.types.capture_blob.deserialize_json(data["data"])
    else:
        out["data"] = b""
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetCaptureDataResponse.start_time required")
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetCaptureDataResponse.end_time required")
    if data.get("dataType") is not None:
        import capo_iotsitewise.types.video_data_type

        out["data_type"] = capo_iotsitewise.types.video_data_type.deserialize_json(
            data["dataType"]
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_iotsitewise.types.video_data_type.VideoDataType", ""
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
