"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetClipOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.content_type
    import capo_kinesis_video_archived_media.types.payload


class GetClipOutput(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_kinesis_video_archived_media.types.content_type.ContentType"
    ]
    """<p>The content type of the media in the requested clip.</p>"""
    payload: "capo_kinesis_video_archived_media.types.payload.Payload"
    """<p>Traditional MP4 file that contains the media clip from the specified video stream. The output will contain the first 100 MB or the first 200 fragments from the specified start timestamp. For more information, see <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>. </p>"""
