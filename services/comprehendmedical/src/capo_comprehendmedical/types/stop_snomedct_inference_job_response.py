"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopSNOMEDCTInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class StopSNOMEDCTInferenceJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehendmedical.types.job_id.JobId"]
    """<p> The identifier generated for the job. To get the status of job, use this identifier with the DescribeSNOMEDCTInferenceJob operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSNOMEDCTInferenceJobResponse:
    out: StopSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_cbor(data: dict) -> StopSNOMEDCTInferenceJobResponse:
    out: StopSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out
