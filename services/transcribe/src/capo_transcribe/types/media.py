"""Generated from Smithy shape ``com.amazonaws.transcribe#Media``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.uri


class Media(TypedDict, closed=True):
    media_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the media file you want to transcribe. For example:</p> <ul> <li> <p> <code>s3://DOC-EXAMPLE-BUCKET/my-media-file.flac</code> </p> </li> <li> <p> <code>s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac</code> </p> </li> </ul> <p>Note that the Amazon S3 bucket that contains your input media must be located in the same Amazon Web Services Region where you're making your transcription request.</p>"""
    redacted_media_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the media file you want to redact. For example:</p> <ul> <li> <p> <code>s3://DOC-EXAMPLE-BUCKET/my-media-file.flac</code> </p> </li> <li> <p> <code>s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac</code> </p> </li> </ul> <p>Note that the Amazon S3 bucket that contains your input media must be located in the same Amazon Web Services Region where you're making your transcription request.</p> <important> <p> <code>RedactedMediaFileUri</code> produces a redacted audio file in addition to a redacted transcript. It is only supported for Call Analytics (<code>StartCallAnalyticsJob</code>) transcription requests.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Media) -> dict:
    out: dict = {}
    if "media_file_uri" in value:
        out["MediaFileUri"] = value["media_file_uri"]
    if "redacted_media_file_uri" in value:
        out["RedactedMediaFileUri"] = value["redacted_media_file_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Media:
    out: Media = {}  # type: ignore[typeddict-item]
    if data.get("MediaFileUri") is not None:
        out["media_file_uri"] = data["MediaFileUri"]
    if data.get("RedactedMediaFileUri") is not None:
        out["redacted_media_file_uri"] = data["RedactedMediaFileUri"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Media) -> dict:
    out: dict = {}
    if "media_file_uri" in value:
        out["MediaFileUri"] = value["media_file_uri"]
    if "redacted_media_file_uri" in value:
        out["RedactedMediaFileUri"] = value["redacted_media_file_uri"]
    return out


def deserialize_cbor(data: dict) -> Media:
    out: Media = {}  # type: ignore[typeddict-item]
    if data.get("MediaFileUri") is not None:
        out["media_file_uri"] = data["MediaFileUri"]
    if data.get("RedactedMediaFileUri") is not None:
        out["redacted_media_file_uri"] = data["RedactedMediaFileUri"]
    return out
