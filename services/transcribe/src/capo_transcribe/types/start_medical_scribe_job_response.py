"""Generated from Smithy shape ``com.amazonaws.transcribe#StartMedicalScribeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_job


class StartMedicalScribeJobResponse(TypedDict, closed=True):
    medical_scribe_job: NotRequired[
        "capo_transcribe.types.medical_scribe_job.MedicalScribeJob"
    ]
    """<p>Provides detailed information about the current Medical Scribe job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMedicalScribeJobResponse) -> dict:
    out: dict = {}
    if "medical_scribe_job" in value:
        import capo_transcribe.types.medical_scribe_job

        out["MedicalScribeJob"] = (
            capo_transcribe.types.medical_scribe_job.serialize_aws_json_1_1(
                value["medical_scribe_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMedicalScribeJobResponse:
    out: StartMedicalScribeJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJob") is not None:
        import capo_transcribe.types.medical_scribe_job

        out["medical_scribe_job"] = (
            capo_transcribe.types.medical_scribe_job.deserialize_aws_json_1_1(
                data["MedicalScribeJob"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartMedicalScribeJobResponse) -> dict:
    out: dict = {}
    if "medical_scribe_job" in value:
        import capo_transcribe.types.medical_scribe_job

        out["MedicalScribeJob"] = (
            capo_transcribe.types.medical_scribe_job.serialize_cbor(
                value["medical_scribe_job"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartMedicalScribeJobResponse:
    out: StartMedicalScribeJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJob") is not None:
        import capo_transcribe.types.medical_scribe_job

        out["medical_scribe_job"] = (
            capo_transcribe.types.medical_scribe_job.deserialize_cbor(
                data["MedicalScribeJob"]
            )
        )
    return out
