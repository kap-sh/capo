"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaCapturePipelineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type
    import capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaCapturePipelineRequest(TypedDict, closed=True):
    source_type: "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType"
    """<p>Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source.</p>"""
    source_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>ARN of the source from which the media artifacts are captured.</p>"""
    sink_type: "capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.MediaPipelineSinkType"
    """<p>Destination type to which the media artifacts are saved. You must use an S3 bucket.</p>"""
    sink_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the sink type.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request.</p>"""
    chime_sdk_meeting_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.ChimeSdkMeetingConfiguration"
    ]
    """<p>The configuration for a specified media pipeline. <code>SourceType</code> must be <code>ChimeSdkMeeting</code>.</p>"""
    sse_aws_key_management_params: NotRequired[
        "capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params.SseAwsKeyManagementParams"
    ]
    """<p>An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.</p>"""
    sink_iam_role_arn: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the sink role to be used with <code>AwsKmsKeyId</code> in <code>SseAwsKeyManagementParams</code>. Can only interact with <code>S3Bucket</code> sink type. The role must belong to the caller’s account and be able to act on behalf of the caller during the API call. All minimum policy permissions requirements for the caller to perform sink-related actions are the same for <code>SinkIamRoleArn</code>.</p> <p>Additionally, the role must have permission to <code>kms:GenerateDataKey</code> using KMS key supplied as <code>AwsKmsKeyId</code> in <code>SseAwsKeyManagementParams</code>. If media concatenation will be required later, the role must also have permission to <code>kms:Decrypt</code> for the same KMS key.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaCapturePipelineRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

    out["SourceType"] = (
        capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.serialize_json(
            value["source_type"]
        )
    )
    out["SourceArn"] = value["source_arn"]
    import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type

    out["SinkType"] = (
        capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.serialize_json(
            value["sink_type"]
        )
    )
    out["SinkArn"] = value["sink_arn"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
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
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMediaCapturePipelineRequest:
    out: CreateMediaCapturePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

        out["source_type"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType",
            "",
        )
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("SinkType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type

        out["sink_type"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    else:
        import typing

        out["sink_type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.MediaPipelineSinkType",
            "",
        )
    if data.get("SinkArn") is not None:
        out["sink_arn"] = data["SinkArn"]
    else:
        out["sink_arn"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
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
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateMediaCapturePipelineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_arn" in value:
        out["source_arn"] = "*** Sensitive Data Redacted ***"
    if "sink_arn" in value:
        out["sink_arn"] = "*** Sensitive Data Redacted ***"
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
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
