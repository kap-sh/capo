"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopSNOMEDCTInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class StopSNOMEDCTInferenceJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehendmedical.types.job_id.JobId"
    """<p> The job id of the asynchronous InferSNOMEDCT job to be stopped. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSNOMEDCTInferenceJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSNOMEDCTInferenceJobRequest:
    out: StopSNOMEDCTInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
