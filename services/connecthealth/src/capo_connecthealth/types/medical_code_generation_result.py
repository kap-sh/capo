"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodeGenerationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.artifact_details
    import capo_connecthealth.types.job_id


class MedicalCodeGenerationResult(TypedDict, closed=True):
    medical_codes_result: NotRequired[
        "capo_connecthealth.types.artifact_details.ArtifactDetails"
    ]
    """<p>Details about the generated medical codes. If the status is SKIPPED, medical codes weren't generated, for example because the clinical note wasn't generated or had no content.</p>"""
    job_id: NotRequired["capo_connecthealth.types.job_id.JobId"]
    """<p>The identifier of the medical coding job that generated the medical codes. To submit feedback on the medical codes, use this value as the artifactSourceId, with the artifactType MEDICAL_CODES, in SubmitFeedback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodeGenerationResult) -> dict:
    out: dict = {}
    if "medical_codes_result" in value:
        import capo_connecthealth.types.artifact_details

        out["medicalCodesResult"] = (
            capo_connecthealth.types.artifact_details.serialize_json(
                value["medical_codes_result"]
            )
        )
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> MedicalCodeGenerationResult:
    out: MedicalCodeGenerationResult = {}  # type: ignore[typeddict-item]
    if data.get("medicalCodesResult") is not None:
        import capo_connecthealth.types.artifact_details

        out["medical_codes_result"] = (
            capo_connecthealth.types.artifact_details.deserialize_json(
                data["medicalCodesResult"]
            )
        )
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    return out
