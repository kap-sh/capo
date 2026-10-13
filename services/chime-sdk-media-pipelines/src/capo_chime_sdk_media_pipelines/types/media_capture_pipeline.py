"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaCapturePipeline``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status
    import capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params


class MediaCapturePipeline(TypedDict, closed=True):
    media_pipeline_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of a media pipeline.</p>"""
    media_pipeline_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the media capture pipeline</p>"""
    source_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType"
    ]
    """<p>Source type from which media artifacts are saved. You must use <code>ChimeMeeting</code>.</p>"""
    source_arn: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>ARN of the source from which the media artifacts are saved.</p>"""
    status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_status.MediaPipelineStatus"
    ]
    """<p>The status of the media pipeline.</p>"""
    sink_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.MediaPipelineSinkType"
    ]
    """<p>Destination type to which the media artifacts are saved. You must use an S3 Bucket.</p>"""
    sink_arn: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>ARN of the destination to which the media artifacts are saved.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the pipeline was created, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the pipeline was updated, in ISO 8601 format.</p>"""
    chime_sdk_meeting_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.ChimeSdkMeetingConfiguration"
    ]
    """<p>The configuration for a specified media pipeline. <code>SourceType</code> must be <code>ChimeSdkMeeting</code>.</p>"""
    sse_aws_key_management_params: NotRequired[
        "capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params.SseAwsKeyManagementParams"
    ]
    """<p>An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.</p>"""
    sink_iam_role_arn: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the sink role to be used with <code>AwsKmsKeyId</code> in <code>SseAwsKeyManagementParams</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaCapturePipeline) -> dict:
    out: dict = {}
    if "media_pipeline_id" in value:
        out["MediaPipelineId"] = value["media_pipeline_id"]
    if "media_pipeline_arn" in value:
        out["MediaPipelineArn"] = value["media_pipeline_arn"]
    if "source_type" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

        out["SourceType"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.serialize_json(
                value["source_type"]
            )
        )
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["Status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "sink_type" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type

        out["SinkType"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.serialize_json(
                value["sink_type"]
            )
        )
    if "sink_arn" in value:
        out["SinkArn"] = value["sink_arn"]
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
    if "chime_sdk_meeting_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration

        out["ChimeSdkMeetingConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.serialize_json(
                value["chime_sdk_meeting_configuration"]
            )
        )
    if "sse_aws_key_management_params" in value:
        import capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params

        out["SseAwsKeyManagementParams"] = (
            capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params.serialize_json(
                value["sse_aws_key_management_params"]
            )
        )
    if "sink_iam_role_arn" in value:
        out["SinkIamRoleArn"] = value["sink_iam_role_arn"]
    return out


def deserialize_json(data: dict) -> MediaCapturePipeline:
    out: MediaCapturePipeline = {}  # type: ignore[typeddict-item]
    if data.get("MediaPipelineId") is not None:
        out["media_pipeline_id"] = data["MediaPipelineId"]
    if data.get("MediaPipelineArn") is not None:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    if data.get("SourceType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

        out["source_type"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    if data.get("Status") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("SinkType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type

        out["sink_type"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    if data.get("SinkArn") is not None:
        out["sink_arn"] = data["SinkArn"]
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
    if data.get("ChimeSdkMeetingConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration

        out["chime_sdk_meeting_configuration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.deserialize_json(
                data["ChimeSdkMeetingConfiguration"]
            )
        )
    if data.get("SseAwsKeyManagementParams") is not None:
        import capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params

        out["sse_aws_key_management_params"] = (
            capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params.deserialize_json(
                data["SseAwsKeyManagementParams"]
            )
        )
    if data.get("SinkIamRoleArn") is not None:
        out["sink_iam_role_arn"] = data["SinkIamRoleArn"]
    return out


def redact_sensitive(value: MediaCapturePipeline) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_arn" in value:
        out["source_arn"] = "*** Sensitive Data Redacted ***"
    if "sink_arn" in value:
        out["sink_arn"] = "*** Sensitive Data Redacted ***"
    if "chime_sdk_meeting_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration

        out["chime_sdk_meeting_configuration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.redact_sensitive(
                value["chime_sdk_meeting_configuration"]
            )
        )
    if "sink_iam_role_arn" in value:
        out["sink_iam_role_arn"] = "*** Sensitive Data Redacted ***"
    return out
