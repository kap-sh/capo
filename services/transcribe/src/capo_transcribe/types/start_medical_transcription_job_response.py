"""Generated from Smithy shape ``com.amazonaws.transcribe#StartMedicalTranscriptionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_transcription_job


class StartMedicalTranscriptionJobResponse(TypedDict, closed=True):
    medical_transcription_job: NotRequired[
        "capo_transcribe.types.medical_transcription_job.MedicalTranscriptionJob"
    ]
    """<p>Provides detailed information about the current medical transcription job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMedicalTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "medical_transcription_job" in value:
        import capo_transcribe.types.medical_transcription_job

        out["MedicalTranscriptionJob"] = (
            capo_transcribe.types.medical_transcription_job.serialize_aws_json_1_1(
                value["medical_transcription_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMedicalTranscriptionJobResponse:
    out: StartMedicalTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJob") is not None:
        import capo_transcribe.types.medical_transcription_job

        out["medical_transcription_job"] = (
            capo_transcribe.types.medical_transcription_job.deserialize_aws_json_1_1(
                data["MedicalTranscriptionJob"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartMedicalTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "medical_transcription_job" in value:
        import capo_transcribe.types.medical_transcription_job

        out["MedicalTranscriptionJob"] = (
            capo_transcribe.types.medical_transcription_job.serialize_cbor(
                value["medical_transcription_job"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartMedicalTranscriptionJobResponse:
    out: StartMedicalTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJob") is not None:
        import capo_transcribe.types.medical_transcription_job

        out["medical_transcription_job"] = (
            capo_transcribe.types.medical_transcription_job.deserialize_cbor(
                data["MedicalTranscriptionJob"]
            )
        )
    return out
