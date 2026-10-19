"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchSegmentJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeBatchSegmentJobRequest(TypedDict, closed=True):
    batch_segment_job_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the batch segment job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchSegmentJobRequest) -> dict:
    out: dict = {}
    out["batchSegmentJobArn"] = value["batch_segment_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchSegmentJobRequest:
    out: DescribeBatchSegmentJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("batchSegmentJobArn") is not None:
        out["batch_segment_job_arn"] = data["batchSegmentJobArn"]
    else:
        out["batch_segment_job_arn"] = ""
    return out
