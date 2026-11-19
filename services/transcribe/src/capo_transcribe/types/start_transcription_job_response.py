"""Generated from Smithy shape ``com.amazonaws.transcribe#StartTranscriptionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.transcription_job


class StartTranscriptionJobResponse(TypedDict, closed=True):
    transcription_job: NotRequired[
        "capo_transcribe.types.transcription_job.TranscriptionJob"
    ]
    """<p>Provides detailed information about the current transcription job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "transcription_job" in value:
        import capo_transcribe.types.transcription_job

        out["TranscriptionJob"] = (
            capo_transcribe.types.transcription_job.serialize_aws_json_1_1(
                value["transcription_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTranscriptionJobResponse:
    out: StartTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptionJob") is not None:
        import capo_transcribe.types.transcription_job

        out["transcription_job"] = (
            capo_transcribe.types.transcription_job.deserialize_aws_json_1_1(
                data["TranscriptionJob"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "transcription_job" in value:
        import capo_transcribe.types.transcription_job

        out["TranscriptionJob"] = (
            capo_transcribe.types.transcription_job.serialize_cbor(
                value["transcription_job"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartTranscriptionJobResponse:
    out: StartTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptionJob") is not None:
        import capo_transcribe.types.transcription_job

        out["transcription_job"] = (
            capo_transcribe.types.transcription_job.deserialize_cbor(
                data["TranscriptionJob"]
            )
        )
    return out
