"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalTranscript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.uri


class MedicalTranscript(TypedDict, closed=True):
    transcript_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of your transcript. You can use this URI to access or download your transcript.</p> <p>Note that this is the Amazon S3 location you specified in your request using the <code>OutputBucketName</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalTranscript) -> dict:
    out: dict = {}
    if "transcript_file_uri" in value:
        out["TranscriptFileUri"] = value["transcript_file_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalTranscript:
    out: MedicalTranscript = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFileUri") is not None:
        out["transcript_file_uri"] = data["TranscriptFileUri"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MedicalTranscript) -> dict:
    out: dict = {}
    if "transcript_file_uri" in value:
        out["TranscriptFileUri"] = value["transcript_file_uri"]
    return out


def deserialize_cbor(data: dict) -> MedicalTranscript:
    out: MedicalTranscript = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFileUri") is not None:
        out["transcript_file_uri"] = data["TranscriptFileUri"]
    return out
