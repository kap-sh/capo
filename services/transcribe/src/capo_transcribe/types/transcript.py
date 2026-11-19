"""Generated from Smithy shape ``com.amazonaws.transcribe#Transcript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.uri


class Transcript(TypedDict, closed=True):
    transcript_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of your transcript. You can use this URI to access or download your transcript.</p> <p>If you included <code>OutputBucketName</code> in your transcription job request, this is the URI of that bucket. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If you didn't include <code>OutputBucketName</code> in your transcription job request, your transcript is stored in a service-managed bucket, and <code>TranscriptFileUri</code> provides you with a temporary URI you can use for secure access to your transcript.</p> <note> <p>Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an <code>AccesDenied</code> error, you can get a new temporary URI by running a <code>GetTranscriptionJob</code> or <code>ListTranscriptionJob</code> request.</p> </note>"""
    redacted_transcript_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of your redacted transcript. You can use this URI to access or download your transcript.</p> <p>If you included <code>OutputBucketName</code> in your transcription job request, this is the URI of that bucket. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If you didn't include <code>OutputBucketName</code> in your transcription job request, your transcript is stored in a service-managed bucket, and <code>RedactedTranscriptFileUri</code> provides you with a temporary URI you can use for secure access to your transcript.</p> <note> <p>Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an <code>AccesDenied</code> error, you can get a new temporary URI by running a <code>GetTranscriptionJob</code> or <code>ListTranscriptionJob</code> request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Transcript) -> dict:
    out: dict = {}
    if "transcript_file_uri" in value:
        out["TranscriptFileUri"] = value["transcript_file_uri"]
    if "redacted_transcript_file_uri" in value:
        out["RedactedTranscriptFileUri"] = value["redacted_transcript_file_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFileUri") is not None:
        out["transcript_file_uri"] = data["TranscriptFileUri"]
    if data.get("RedactedTranscriptFileUri") is not None:
        out["redacted_transcript_file_uri"] = data["RedactedTranscriptFileUri"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Transcript) -> dict:
    out: dict = {}
    if "transcript_file_uri" in value:
        out["TranscriptFileUri"] = value["transcript_file_uri"]
    if "redacted_transcript_file_uri" in value:
        out["RedactedTranscriptFileUri"] = value["redacted_transcript_file_uri"]
    return out


def deserialize_cbor(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFileUri") is not None:
        out["transcript_file_uri"] = data["TranscriptFileUri"]
    if data.get("RedactedTranscriptFileUri") is not None:
        out["redacted_transcript_file_uri"] = data["RedactedTranscriptFileUri"]
    return out
