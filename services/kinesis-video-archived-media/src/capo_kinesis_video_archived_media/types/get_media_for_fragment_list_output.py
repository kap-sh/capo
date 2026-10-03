"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetMediaForFragmentListOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.content_type
    import capo_kinesis_video_archived_media.types.payload


class GetMediaForFragmentListOutput(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_kinesis_video_archived_media.types.content_type.ContentType"
    ]
    """<p>The content type of the requested media.</p>"""
    payload: "capo_kinesis_video_archived_media.types.payload.Payload"
    """<p>The payload that Kinesis Video Streams returns is a sequence of chunks from the specified stream. For information about the chunks, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html">PutMedia</a>. The chunks that Kinesis Video Streams returns in the <code>GetMediaForFragmentList</code> call also include the following additional Matroska (MKV) tags: </p> <ul> <li> <p>AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.</p> </li> <li> <p>AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side timestamp of the fragment.</p> </li> <li> <p>AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side timestamp of the fragment.</p> </li> </ul> <p>The following tags will be included if an exception occurs:</p> <ul> <li> <p>AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception </p> </li> <li> <p>AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the </p> </li> <li> <p>AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception </p> </li> </ul>"""
