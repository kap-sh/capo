"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamPipeline``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status
    import capo_chime_sdk_media_pipelines.types.media_stream_sink_list
    import capo_chime_sdk_media_pipelines.types.media_stream_source_list


class MediaStreamPipeline(TypedDict, closed=True):
    media_pipeline_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the media stream pipeline</p>"""
    media_pipeline_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the media stream pipeline.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the media stream pipeline was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the media stream pipeline was updated.</p>"""
    status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_status.MediaPipelineStatus"
    ]
    """<p>The status of the media stream pipeline.</p>"""
    sources: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_stream_source_list.MediaStreamSourceList"
    ]
    """<p>The media stream pipeline's data sources.</p>"""
    sinks: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_stream_sink_list.MediaStreamSinkList"
    ]
    """<p>The media stream pipeline's data sinks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamPipeline) -> dict:
    out: dict = {}
    if "media_pipeline_id" in value:
        out["MediaPipelineId"] = value["media_pipeline_id"]
    if "media_pipeline_arn" in value:
        out["MediaPipelineArn"] = value["media_pipeline_arn"]
    if "created_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["Status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "sources" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_source_list

        out["Sources"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_source_list.serialize_json(
                value["sources"]
            )
        )
    if "sinks" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_sink_list

        out["Sinks"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_sink_list.serialize_json(
                value["sinks"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaStreamPipeline:
    out: MediaStreamPipeline = {}  # type: ignore[typeddict-item]
    if data.get("MediaPipelineId") is not None:
        out["media_pipeline_id"] = data["MediaPipelineId"]
    if data.get("MediaPipelineArn") is not None:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("Status") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("Sources") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_source_list.deserialize_json(
                data["Sources"]
            )
        )
    if data.get("Sinks") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_sink_list.deserialize_json(
                data["Sinks"]
            )
        )
    return out


def redact_sensitive(value: MediaStreamPipeline) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sources" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_source_list.redact_sensitive(
                value["sources"]
            )
        )
    if "sinks" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_sink_list.redact_sensitive(
                value["sinks"]
            )
        )
    return out
