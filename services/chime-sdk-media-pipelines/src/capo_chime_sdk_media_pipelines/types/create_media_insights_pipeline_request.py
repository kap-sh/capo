"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaInsightsPipelineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata
    import capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaInsightsPipelineRequest(TypedDict, closed=True):
    media_insights_pipeline_configuration_arn: (
        "capo_chime_sdk_media_pipelines.types.arn.Arn"
    )
    """<p>The ARN of the pipeline's configuration.</p>"""
    kinesis_video_stream_source_runtime_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.KinesisVideoStreamSourceRuntimeConfiguration"
    ]
    """<p>The runtime configuration for the Kinesis video stream source of the media insights pipeline.</p>"""
    media_insights_runtime_metadata: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.MediaInsightsRuntimeMetadata"
    ]
    """<p>The runtime metadata for the media insights pipeline. Consists of a key-value map of strings.</p>"""
    kinesis_video_stream_recording_source_runtime_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.KinesisVideoStreamRecordingSourceRuntimeConfiguration"
    ]
    """<p>The runtime configuration for the Kinesis video recording stream source.</p>"""
    s3_recording_sink_runtime_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.S3RecordingSinkRuntimeConfiguration"
    ]
    """<p>The runtime configuration for the S3 recording sink. If specified, the settings in this structure override any settings in <code>S3RecordingSinkConfiguration</code>.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags assigned to the media insights pipeline.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the media insights pipeline request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaInsightsPipelineRequest) -> dict:
    out: dict = {}
    out["MediaInsightsPipelineConfigurationArn"] = value[
        "media_insights_pipeline_configuration_arn"
    ]
    if "kinesis_video_stream_source_runtime_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration

        out["KinesisVideoStreamSourceRuntimeConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.serialize_json(
                value["kinesis_video_stream_source_runtime_configuration"]
            )
        )
    if "media_insights_runtime_metadata" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata

        out["MediaInsightsRuntimeMetadata"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.serialize_json(
                value["media_insights_runtime_metadata"]
            )
        )
    if "kinesis_video_stream_recording_source_runtime_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration

        out["KinesisVideoStreamRecordingSourceRuntimeConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.serialize_json(
                value["kinesis_video_stream_recording_source_runtime_configuration"]
            )
        )
    if "s3_recording_sink_runtime_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration

        out["S3RecordingSinkRuntimeConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.serialize_json(
                value["s3_recording_sink_runtime_configuration"]
            )
        )
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateMediaInsightsPipelineRequest:
    out: CreateMediaInsightsPipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfigurationArn") is not None:
        out["media_insights_pipeline_configuration_arn"] = data[
            "MediaInsightsPipelineConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "CreateMediaInsightsPipelineRequest.media_insights_pipeline_configuration_arn required"
        )
    if data.get("KinesisVideoStreamSourceRuntimeConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration

        out["kinesis_video_stream_source_runtime_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.deserialize_json(
                data["KinesisVideoStreamSourceRuntimeConfiguration"]
            )
        )
    if data.get("MediaInsightsRuntimeMetadata") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata

        out["media_insights_runtime_metadata"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.deserialize_json(
                data["MediaInsightsRuntimeMetadata"]
            )
        )
    if data.get("KinesisVideoStreamRecordingSourceRuntimeConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration

        out["kinesis_video_stream_recording_source_runtime_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.deserialize_json(
                data["KinesisVideoStreamRecordingSourceRuntimeConfiguration"]
            )
        )
    if data.get("S3RecordingSinkRuntimeConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration

        out["s3_recording_sink_runtime_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.deserialize_json(
                data["S3RecordingSinkRuntimeConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out


def redact_sensitive(value: CreateMediaInsightsPipelineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_pipeline_configuration_arn" in value:
        out["media_insights_pipeline_configuration_arn"] = (
            "*** Sensitive Data Redacted ***"
        )
    if "media_insights_runtime_metadata" in value:
        out["media_insights_runtime_metadata"] = "*** Sensitive Data Redacted ***"
    if "s3_recording_sink_runtime_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration

        out["s3_recording_sink_runtime_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.redact_sensitive(
                value["s3_recording_sink_runtime_configuration"]
            )
        )
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
