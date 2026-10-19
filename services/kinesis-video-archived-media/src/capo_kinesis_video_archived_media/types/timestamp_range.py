"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#TimestampRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.timestamp


class TimestampRange(TypedDict, closed=True):
    start_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The starting timestamp in the range of timestamps for which to return fragments.</p>"""
    end_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The ending timestamp in the range of timestamps for which to return fragments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampRange) -> dict:
    out: dict = {}
    import capo_kinesis_video_archived_media.types.timestamp

    out["StartTimestamp"] = (
        capo_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    )
    import capo_kinesis_video_archived_media.types.timestamp

    out["EndTimestamp"] = (
        capo_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["end_timestamp"]
        )
    )
    return out


def deserialize_json(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if data.get("StartTimestamp") is not None:
        import capo_kinesis_video_archived_media.types.timestamp

        out["start_timestamp"] = (
            capo_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        import datetime

        out["start_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EndTimestamp") is not None:
        import capo_kinesis_video_archived_media.types.timestamp

        out["end_timestamp"] = (
            capo_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    else:
        import datetime

        out["end_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
