"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#S3RecordingSinkRuntimeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.recording_file_format


class S3RecordingSinkRuntimeConfiguration(TypedDict, closed=True):
    destination: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The URI of the S3 bucket used as the sink.</p>"""
    recording_file_format: (
        "capo_chime_sdk_media_pipelines.types.recording_file_format.RecordingFileFormat"
    )
    """<p>The file format for the media files sent to the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RecordingSinkRuntimeConfiguration) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    import capo_chime_sdk_media_pipelines.types.recording_file_format

    out["RecordingFileFormat"] = (
        capo_chime_sdk_media_pipelines.types.recording_file_format.serialize_json(
            value["recording_file_format"]
        )
    )
    return out


def deserialize_json(data: dict) -> S3RecordingSinkRuntimeConfiguration:
    out: S3RecordingSinkRuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        out["destination"] = ""
    if data.get("RecordingFileFormat") is not None:
        import capo_chime_sdk_media_pipelines.types.recording_file_format

        out["recording_file_format"] = (
            capo_chime_sdk_media_pipelines.types.recording_file_format.deserialize_json(
                data["RecordingFileFormat"]
            )
        )
    else:
        import typing

        out["recording_file_format"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.recording_file_format.RecordingFileFormat",
            "",
        )
    return out


def redact_sensitive(value: S3RecordingSinkRuntimeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination" in value:
        out["destination"] = "*** Sensitive Data Redacted ***"
    return out
