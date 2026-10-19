"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ClipTimestampRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.timestamp


class ClipTimestampRange(TypedDict, closed=True):
    start_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The starting timestamp in the range of timestamps for which to return fragments. </p> <p>Only fragments that start exactly at or after <code>StartTimestamp</code> are included in the session. Fragments that start before <code>StartTimestamp</code> and continue past it aren't included in the session. If <code>FragmentSelectorType</code> is <code>SERVER_TIMESTAMP</code>, the <code>StartTimestamp</code> must be later than the stream head. </p>"""
    end_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The end of the timestamp range for the requested media.</p> <p>This value must be within 24 hours of the specified <code>StartTimestamp</code>, and it must be later than the <code>StartTimestamp</code> value. If <code>FragmentSelectorType</code> for the request is <code>SERVER_TIMESTAMP</code>, this value must be in the past. </p> <p>This value is inclusive. The <code>EndTimestamp</code> is compared to the (starting) timestamp of the fragment. Fragments that start before the <code>EndTimestamp</code> value and continue past it are included in the session. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClipTimestampRange) -> dict:
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


def deserialize_json(data: dict) -> ClipTimestampRange:
    out: ClipTimestampRange = {}  # type: ignore[typeddict-item]
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
