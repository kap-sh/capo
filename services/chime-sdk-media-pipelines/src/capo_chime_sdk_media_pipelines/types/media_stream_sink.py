"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSink``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type
    import capo_chime_sdk_media_pipelines.types.media_stream_type
    import capo_chime_sdk_media_pipelines.types.reserved_stream_capacity


class MediaStreamSink(TypedDict, closed=True):
    sink_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the Kinesis Video Stream pool returned by the <a>CreateMediaPipelineKinesisVideoStreamPool</a> API.</p>"""
    sink_type: "capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.MediaStreamPipelineSinkType"
    """<p>The media stream sink's type.</p>"""
    reserved_stream_capacity: "capo_chime_sdk_media_pipelines.types.reserved_stream_capacity.ReservedStreamCapacity"
    """<p>Specifies the number of streams that the sink can accept.</p>"""
    media_stream_type: (
        "capo_chime_sdk_media_pipelines.types.media_stream_type.MediaStreamType"
    )
    """<p>The media stream sink's media stream type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSink) -> dict:
    out: dict = {}
    out["SinkArn"] = value["sink_arn"]
    import capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type

    out["SinkType"] = (
        capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.serialize_json(
            value["sink_type"]
        )
    )
    out["ReservedStreamCapacity"] = value["reserved_stream_capacity"]
    import capo_chime_sdk_media_pipelines.types.media_stream_type

    out["MediaStreamType"] = (
        capo_chime_sdk_media_pipelines.types.media_stream_type.serialize_json(
            value["media_stream_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaStreamSink:
    out: MediaStreamSink = {}  # type: ignore[typeddict-item]
    if data.get("SinkArn") is not None:
        out["sink_arn"] = data["SinkArn"]
    else:
        raise DeserializationError("MediaStreamSink.sink_arn required")
    if data.get("SinkType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type

        out["sink_type"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    else:
        raise DeserializationError("MediaStreamSink.sink_type required")
    if data.get("ReservedStreamCapacity") is not None:
        out["reserved_stream_capacity"] = data["ReservedStreamCapacity"]
    else:
        raise DeserializationError("MediaStreamSink.reserved_stream_capacity required")
    if data.get("MediaStreamType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_type

        out["media_stream_type"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_type.deserialize_json(
                data["MediaStreamType"]
            )
        )
    else:
        raise DeserializationError("MediaStreamSink.media_stream_type required")
    return out


def redact_sensitive(value: MediaStreamSink) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sink_arn" in value:
        out["sink_arn"] = "*** Sensitive Data Redacted ***"
    return out
