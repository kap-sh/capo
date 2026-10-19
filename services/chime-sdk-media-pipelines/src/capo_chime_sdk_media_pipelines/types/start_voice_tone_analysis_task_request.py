"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StartVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration
    import capo_chime_sdk_media_pipelines.types.non_empty_string
    import capo_chime_sdk_media_pipelines.types.voice_analytics_language_code


class StartVoiceToneAnalysisTaskRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    language_code: "capo_chime_sdk_media_pipelines.types.voice_analytics_language_code.VoiceAnalyticsLanguageCode"
    """<p>The language code.</p>"""
    kinesis_video_stream_source_task_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.KinesisVideoStreamSourceTaskConfiguration"
    ]
    """<p>The task configuration for the Kinesis video stream source of the media insights pipeline.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the client request. Use a different token for different voice tone analysis tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.voice_analytics_language_code

    out["LanguageCode"] = (
        capo_chime_sdk_media_pipelines.types.voice_analytics_language_code.serialize_json(
            value["language_code"]
        )
    )
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


def deserialize_json(data: dict) -> StartVoiceToneAnalysisTaskRequest:
    out: StartVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_chime_sdk_media_pipelines.types.voice_analytics_language_code

        out["language_code"] = (
            capo_chime_sdk_media_pipelines.types.voice_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.voice_analytics_language_code.VoiceAnalyticsLanguageCode",
            "",
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


def redact_sensitive(value: StartVoiceToneAnalysisTaskRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
