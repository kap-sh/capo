"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.dataset_export_job_output
    import capo_personalize.types.ingestion_mode
    import capo_personalize.types.name
    import capo_personalize.types.role_arn
    import capo_personalize.types.tags


class CreateDatasetExportJobRequest(TypedDict, closed=True):
    job_name: "capo_personalize.types.name.Name"
    """<p>The name for the dataset export job.</p>"""
    dataset_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset that contains the data to export.</p>"""
    ingestion_mode: NotRequired["capo_personalize.types.ingestion_mode.IngestionMode"]
    """<p>The data to export, based on how you imported the data. You can choose to export only <code>BULK</code> data that you imported using a dataset import job, only <code>PUT</code> data that you imported incrementally (using the console, PutEvents, PutUsers and PutItems operations), or <code>ALL</code> for both types. The default value is <code>PUT</code>. </p>"""
    role_arn: "capo_personalize.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket.</p>"""
    job_output: (
        "capo_personalize.types.dataset_export_job_output.DatasetExportJobOutput"
    )
    """<p>The path to the Amazon S3 bucket where the job's output is stored.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset export job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetExportJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["datasetArn"] = value["dataset_arn"]
    if "ingestion_mode" in value:
        import capo_personalize.types.ingestion_mode

        out["ingestionMode"] = (
            capo_personalize.types.ingestion_mode.serialize_aws_json_1_1(
                value["ingestion_mode"]
            )
        )
    out["roleArn"] = value["role_arn"]
    import capo_personalize.types.dataset_export_job_output

    out["jobOutput"] = (
        capo_personalize.types.dataset_export_job_output.serialize_aws_json_1_1(
            value["job_output"]
        )
    )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetExportJobRequest:
    out: CreateDatasetExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateDatasetExportJobRequest.job_name required")
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("CreateDatasetExportJobRequest.dataset_arn required")
    if data.get("ingestionMode") is not None:
        import capo_personalize.types.ingestion_mode

        out["ingestion_mode"] = (
            capo_personalize.types.ingestion_mode.deserialize_aws_json_1_1(
                data["ingestionMode"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateDatasetExportJobRequest.role_arn required")
    if data.get("jobOutput") is not None:
        import capo_personalize.types.dataset_export_job_output

        out["job_output"] = (
            capo_personalize.types.dataset_export_job_output.deserialize_aws_json_1_1(
                data["jobOutput"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetExportJobRequest.job_output required")
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
