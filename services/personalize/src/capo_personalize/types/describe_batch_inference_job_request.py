"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeBatchInferenceJobRequest(TypedDict, closed=True):
    batch_inference_job_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the batch inference job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchInferenceJobRequest) -> dict:
    out: dict = {}
    out["batchInferenceJobArn"] = value["batch_inference_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchInferenceJobRequest:
    out: DescribeBatchInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("batchInferenceJobArn") is not None:
        out["batch_inference_job_arn"] = data["batchInferenceJobArn"]
    else:
        out["batch_inference_job_arn"] = ""
    return out
