"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#S3RecordingSinkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.recording_file_format


class S3RecordingSinkConfiguration(TypedDict, closed=True):
    destination: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The default URI of the Amazon S3 bucket used as the recording sink.</p>"""
    recording_file_format: NotRequired[
        "capo_chime_sdk_media_pipelines.types.recording_file_format.RecordingFileFormat"
    ]
    """<p>The default file format for the media files sent to the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RecordingSinkConfiguration) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "recording_file_format" in value:
        import capo_chime_sdk_media_pipelines.types.recording_file_format

        out["RecordingFileFormat"] = (
            capo_chime_sdk_media_pipelines.types.recording_file_format.serialize_json(
                value["recording_file_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3RecordingSinkConfiguration:
    out: S3RecordingSinkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    if data.get("RecordingFileFormat") is not None:
        import capo_chime_sdk_media_pipelines.types.recording_file_format

        out["recording_file_format"] = (
            capo_chime_sdk_media_pipelines.types.recording_file_format.deserialize_json(
                data["RecordingFileFormat"]
            )
        )
    return out


def redact_sensitive(value: S3RecordingSinkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination" in value:
        out["destination"] = "*** Sensitive Data Redacted ***"
    return out
