"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteDatasetImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteDatasetImportJobRequest(TypedDict, closed=True):
    dataset_import_job_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset import job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatasetImportJobRequest:
    out: DeleteDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetImportJobArn") is not None:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    else:
        out["dataset_import_job_arn"] = ""
    return out
