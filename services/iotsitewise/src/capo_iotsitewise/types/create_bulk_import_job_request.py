"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateBulkImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.adaptive_ingestion
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.bulk_import_job_name
    import capo_iotsitewise.types.delete_files_after_import
    import capo_iotsitewise.types.error_report_location
    import capo_iotsitewise.types.files
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_configuration
    import capo_iotsitewise.types.workspace_name


class CreateBulkImportJobRequest(TypedDict, closed=True):
    job_name: "capo_iotsitewise.types.bulk_import_job_name.BulkImportJobName"
    """<p>The unique name that helps identify the job request.</p>"""
    job_role_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IAM role that allows IoT SiteWise to read Amazon S3 data.</p>"""
    files: "capo_iotsitewise.types.files.Files"
    """<p>The files in the specified Amazon S3 bucket that contain your data. You can specify up to 100 files for each bulk import job. Each file supports the following size limits:</p> <ul> <li> <p>Parquet files – Up to 256 MiB.</p> </li> <li> <p>Other file formats – Up to 5 GiB.</p> </li> </ul>"""
    error_report_location: (
        "capo_iotsitewise.types.error_report_location.ErrorReportLocation"
    )
    """<p>The Amazon S3 destination where errors associated with the job creation request are saved.</p>"""
    job_configuration: NotRequired[
        "capo_iotsitewise.types.job_configuration.JobConfiguration"
    ]
    """<p>Contains the configuration information of a job, such as the file format used to save data in Amazon S3.</p>"""
    adaptive_ingestion: NotRequired[
        "capo_iotsitewise.types.adaptive_ingestion.AdaptiveIngestion"
    ]
    """<p>If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.</p>"""
    delete_files_after_import: NotRequired[
        "capo_iotsitewise.types.delete_files_after_import.DeleteFilesAfterImport"
    ]
    """<p>If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.</p>"""
    dataset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the session dataset to ingest data into. Specify this field, together with <code>workspaceName</code>, to ingest data into a session dataset in a workspace.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace that contains the session dataset. Specify this field together with <code>datasetId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBulkImportJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["jobRoleArn"] = value["job_role_arn"]
    import capo_iotsitewise.types.files

    out["files"] = capo_iotsitewise.types.files.serialize_json(value["files"])
    import capo_iotsitewise.types.error_report_location

    out["errorReportLocation"] = (
        capo_iotsitewise.types.error_report_location.serialize_json(
            value["error_report_location"]
        )
    )
    if "job_configuration" in value:
        import capo_iotsitewise.types.job_configuration

        out["jobConfiguration"] = (
            capo_iotsitewise.types.job_configuration.serialize_json(
                value["job_configuration"]
            )
        )
    if "adaptive_ingestion" in value:
        out["adaptiveIngestion"] = value["adaptive_ingestion"]
    if "delete_files_after_import" in value:
        out["deleteFilesAfterImport"] = value["delete_files_after_import"]
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> CreateBulkImportJobRequest:
    out: CreateBulkImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateBulkImportJobRequest.job_name required")
    if data.get("jobRoleArn") is not None:
        out["job_role_arn"] = data["jobRoleArn"]
    else:
        raise DeserializationError("CreateBulkImportJobRequest.job_role_arn required")
    if data.get("files") is not None:
        import capo_iotsitewise.types.files

        out["files"] = capo_iotsitewise.types.files.deserialize_json(data["files"])
    else:
        raise DeserializationError("CreateBulkImportJobRequest.files required")
    if data.get("errorReportLocation") is not None:
        import capo_iotsitewise.types.error_report_location

        out["error_report_location"] = (
            capo_iotsitewise.types.error_report_location.deserialize_json(
                data["errorReportLocation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBulkImportJobRequest.error_report_location required"
        )
    if data.get("jobConfiguration") is not None:
        import capo_iotsitewise.types.job_configuration

        out["job_configuration"] = (
            capo_iotsitewise.types.job_configuration.deserialize_json(
                data["jobConfiguration"]
            )
        )
    if data.get("adaptiveIngestion") is not None:
        out["adaptive_ingestion"] = data["adaptiveIngestion"]
    if data.get("deleteFilesAfterImport") is not None:
        out["delete_files_after_import"] = data["deleteFilesAfterImport"]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    return out
