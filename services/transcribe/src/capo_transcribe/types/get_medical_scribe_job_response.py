"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalScribeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_job


class GetMedicalScribeJobResponse(TypedDict, closed=True):
    medical_scribe_job: NotRequired[
        "capo_transcribe.types.medical_scribe_job.MedicalScribeJob"
    ]
    """<p>Provides detailed information about the specified Medical Scribe job, including job status and, if applicable, failure reason</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalScribeJobResponse) -> dict:
    out: dict = {}
    if "medical_scribe_job" in value:
        import capo_transcribe.types.medical_scribe_job

        out["MedicalScribeJob"] = (
            capo_transcribe.types.medical_scribe_job.serialize_aws_json_1_1(
                value["medical_scribe_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalScribeJobResponse:
    out: GetMedicalScribeJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJob") is not None:
        import capo_transcribe.types.medical_scribe_job

        out["medical_scribe_job"] = (
            capo_transcribe.types.medical_scribe_job.deserialize_aws_json_1_1(
                data["MedicalScribeJob"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMedicalScribeJobResponse) -> dict:
    out: dict = {}
    if "medical_scribe_job" in value:
        import capo_transcribe.types.medical_scribe_job

        out["MedicalScribeJob"] = (
            capo_transcribe.types.medical_scribe_job.serialize_cbor(
                value["medical_scribe_job"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetMedicalScribeJobResponse:
    out: GetMedicalScribeJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJob") is not None:
        import capo_transcribe.types.medical_scribe_job

        out["medical_scribe_job"] = (
            capo_transcribe.types.medical_scribe_job.deserialize_cbor(
                data["MedicalScribeJob"]
            )
        )
    return out
