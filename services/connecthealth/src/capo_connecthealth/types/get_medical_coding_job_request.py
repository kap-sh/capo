"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalCodingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.job_id


class GetMedicalCodingJobRequest(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p>The unique identifier of the medical coding job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalCodingJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMedicalCodingJobRequest:
    out: GetMedicalCodingJobRequest = {}  # type: ignore[typeddict-item]
    return out
