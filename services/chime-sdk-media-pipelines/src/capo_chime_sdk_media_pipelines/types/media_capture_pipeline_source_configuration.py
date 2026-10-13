"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaCapturePipelineSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration


class MediaCapturePipelineSourceConfiguration(TypedDict, closed=True):
    media_pipeline_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The media pipeline ARN in the configuration object of a media capture pipeline.</p>"""
    chime_sdk_meeting_configuration: "capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration.ChimeSdkMeetingConcatenationConfiguration"
    """<p>The meeting configuration settings in a media capture pipeline configuration object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaCapturePipelineSourceConfiguration) -> dict:
    out: dict = {}
    out["MediaPipelineArn"] = value["media_pipeline_arn"]
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration

    out["ChimeSdkMeetingConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration.serialize_json(
            value["chime_sdk_meeting_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaCapturePipelineSourceConfiguration:
    out: MediaCapturePipelineSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MediaPipelineArn") is not None:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    else:
        raise DeserializationError(
            "MediaCapturePipelineSourceConfiguration.media_pipeline_arn required"
        )
    if data.get("ChimeSdkMeetingConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration

        out["chime_sdk_meeting_configuration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_concatenation_configuration.deserialize_json(
                data["ChimeSdkMeetingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "MediaCapturePipelineSourceConfiguration.chime_sdk_meeting_configuration required"
        )
    return out


def redact_sensitive(value: MediaCapturePipelineSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_pipeline_arn" in value:
        out["media_pipeline_arn"] = "*** Sensitive Data Redacted ***"
    return out
