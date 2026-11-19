"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StartSNOMEDCTInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class StartSNOMEDCTInferenceJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehendmedical.types.job_id.JobId"]
    """<p> The identifier generated for the job. To get the status of a job, use this identifier with the StartSNOMEDCTInferenceJob operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSNOMEDCTInferenceJobResponse:
    out: StartSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_cbor(data: dict) -> StartSNOMEDCTInferenceJobResponse:
    out: StartSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out
