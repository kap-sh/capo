"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeDatasetImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeDatasetImportJobRequest(TypedDict, closed=True):
    dataset_import_job_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset import job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetImportJobRequest:
    out: DescribeDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetImportJobArn") is not None:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    else:
        out["dataset_import_job_arn"] = ""
    return out
