"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteMedicalTranscriptionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.transcription_job_name


class DeleteMedicalTranscriptionJobRequest(TypedDict, closed=True):
    medical_transcription_job_name: (
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the medical transcription job you want to delete. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMedicalTranscriptionJobRequest) -> dict:
    out: dict = {}
    out["MedicalTranscriptionJobName"] = value["medical_transcription_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMedicalTranscriptionJobRequest:
    out: DeleteMedicalTranscriptionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJobName") is not None:
        out["medical_transcription_job_name"] = data["MedicalTranscriptionJobName"]
    else:
        out["medical_transcription_job_name"] = ""
    return out
