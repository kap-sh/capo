"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeDatasetExportJobRequest(TypedDict, closed=True):
    dataset_export_job_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset export job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetExportJobRequest) -> dict:
    out: dict = {}
    out["datasetExportJobArn"] = value["dataset_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetExportJobRequest:
    out: DescribeDatasetExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetExportJobArn") is not None:
        out["dataset_export_job_arn"] = data["datasetExportJobArn"]
    else:
        out["dataset_export_job_arn"] = ""
    return out
