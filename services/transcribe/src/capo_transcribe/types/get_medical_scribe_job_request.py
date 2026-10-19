"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalScribeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.transcription_job_name


class GetMedicalScribeJobRequest(TypedDict, closed=True):
    medical_scribe_job_name: (
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the Medical Scribe job you want information about. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalScribeJobRequest) -> dict:
    out: dict = {}
    out["MedicalScribeJobName"] = value["medical_scribe_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalScribeJobRequest:
    out: GetMedicalScribeJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJobName") is not None:
        out["medical_scribe_job_name"] = data["MedicalScribeJobName"]
    else:
        out["medical_scribe_job_name"] = ""
    return out
