"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StartSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration
    import capo_chime_sdk_media_pipelines.types.non_empty_string


class StartSpeakerSearchTaskRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    voice_profile_domain_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the voice profile domain that will store the voice profile.</p>"""
    kinesis_video_stream_source_task_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.KinesisVideoStreamSourceTaskConfiguration"
    ]
    """<p>The task configuration for the Kinesis video stream source of the media insights pipeline.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the client request. Use a different token for different speaker search tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    out["VoiceProfileDomainArn"] = value["voice_profile_domain_arn"]
    if "kinesis_video_stream_source_task_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration

        out["KinesisVideoStreamSourceTaskConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.serialize_json(
                value["kinesis_video_stream_source_task_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartSpeakerSearchTaskRequest:
    out: StartSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfileDomainArn") is not None:
        out["voice_profile_domain_arn"] = data["VoiceProfileDomainArn"]
    else:
        raise DeserializationError(
            "StartSpeakerSearchTaskRequest.voice_profile_domain_arn required"
        )
    if data.get("KinesisVideoStreamSourceTaskConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration

        out["kinesis_video_stream_source_task_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.deserialize_json(
                data["KinesisVideoStreamSourceTaskConfiguration"]
            )
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out


def redact_sensitive(value: StartSpeakerSearchTaskRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile_domain_arn" in value:
        out["voice_profile_domain_arn"] = "*** Sensitive Data Redacted ***"
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
