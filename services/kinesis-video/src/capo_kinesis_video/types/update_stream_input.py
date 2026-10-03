"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.device_name
    import capo_kinesis_video.types.media_type
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.version


class UpdateStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream whose metadata you want to update.</p> <p>The stream name is an identifier for the stream, and must be unique for each account and region.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The ARN of the stream whose metadata you want to update.</p>"""
    current_version: "capo_kinesis_video.types.version.Version"
    """<p>The version of the stream whose metadata you want to update.</p>"""
    device_name: NotRequired["capo_kinesis_video.types.device_name.DeviceName"]
    """<p>The name of the device that is writing to the stream. </p> <note> <p> In the current implementation, Kinesis Video Streams does not use this name. </p> </note>"""
    media_type: NotRequired["capo_kinesis_video.types.media_type.MediaType"]
    """<p>The stream's media type. Use <code>MediaType</code> to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see <a href="http://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. If you choose to specify the <code>MediaType</code>, see <a href="https://tools.ietf.org/html/rfc6838#section-4.2">Naming Requirements</a>.</p> <p>To play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify <code>video/h264</code> as the <code>MediaType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    out["CurrentVersion"] = value["current_version"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "media_type" in value:
        out["MediaType"] = value["media_type"]
    return out


def deserialize_json(data: dict) -> UpdateStreamInput:
    out: UpdateStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    else:
        raise DeserializationError("UpdateStreamInput.current_version required")
    if data.get("DeviceName") is not None:
        out["device_name"] = data["DeviceName"]
    if data.get("MediaType") is not None:
        out["media_type"] = data["MediaType"]
    return out
