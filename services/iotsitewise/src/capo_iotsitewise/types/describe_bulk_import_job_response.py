"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeBulkImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.adaptive_ingestion
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.delete_files_after_import
    import capo_iotsitewise.types.error_report_location
    import capo_iotsitewise.types.files
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_configuration
    import capo_iotsitewise.types.job_status
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.workspace_name


class DescribeBulkImportJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the job.</p>"""
    job_name: "capo_iotsitewise.types.name.Name"
    """<p>The unique name that helps identify the job request.</p>"""
    job_status: "capo_iotsitewise.types.job_status.JobStatus"
    """<p>The status of the bulk import job can be one of following values:</p> <ul> <li> <p> <code>PENDING</code> – IoT SiteWise is waiting for the current bulk import job to finish.</p> </li> <li> <p> <code>CANCELLED</code> – The bulk import job has been canceled.</p> </li> <li> <p> <code>RUNNING</code> – IoT SiteWise is processing your request to import your data from Amazon S3.</p> </li> <li> <p> <code>COMPLETED</code> – IoT SiteWise successfully completed your request to import data from Amazon S3.</p> </li> <li> <p> <code>FAILED</code> – IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> <li> <p> <code>COMPLETED_WITH_FAILURES</code> – IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> </ul>"""
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
    job_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the job was created, in Unix epoch TIME.</p>"""
    job_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the job was last updated, in Unix epoch time.</p>"""
    adaptive_ingestion: NotRequired[
        "capo_iotsitewise.types.adaptive_ingestion.AdaptiveIngestion"
    ]
    """<p>If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.</p>"""
    delete_files_after_import: NotRequired[
        "capo_iotsitewise.types.delete_files_after_import.DeleteFilesAfterImport"
    ]
    """<p>If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.</p>"""
    dataset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBulkImportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import capo_iotsitewise.types.job_status

    out["jobStatus"] = capo_iotsitewise.types.job_status.serialize_json(
        value["job_status"]
    )
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
    import capo_iotsitewise.types.timestamp

    out["jobCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["job_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["jobLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["job_last_update_date"]
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


def deserialize_json(data: dict) -> DescribeBulkImportJobResponse:
    out: DescribeBulkImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DescribeBulkImportJobResponse.job_id required")
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("DescribeBulkImportJobResponse.job_name required")
    if data.get("jobStatus") is not None:
        import capo_iotsitewise.types.job_status

        out["job_status"] = capo_iotsitewise.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("DescribeBulkImportJobResponse.job_status required")
    if data.get("jobRoleArn") is not None:
        out["job_role_arn"] = data["jobRoleArn"]
    else:
        raise DeserializationError(
            "DescribeBulkImportJobResponse.job_role_arn required"
        )
    if data.get("files") is not None:
        import capo_iotsitewise.types.files

        out["files"] = capo_iotsitewise.types.files.deserialize_json(data["files"])
    else:
        raise DeserializationError("DescribeBulkImportJobResponse.files required")
    if data.get("errorReportLocation") is not None:
        import capo_iotsitewise.types.error_report_location

        out["error_report_location"] = (
            capo_iotsitewise.types.error_report_location.deserialize_json(
                data["errorReportLocation"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBulkImportJobResponse.error_report_location required"
        )
    if data.get("jobConfiguration") is not None:
        import capo_iotsitewise.types.job_configuration

        out["job_configuration"] = (
            capo_iotsitewise.types.job_configuration.deserialize_json(
                data["jobConfiguration"]
            )
        )
    if data.get("jobCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["job_creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["jobCreationDate"]
        )
    else:
        raise DeserializationError(
            "DescribeBulkImportJobResponse.job_creation_date required"
        )
    if data.get("jobLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["job_last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["jobLastUpdateDate"]
        )
    else:
        raise DeserializationError(
            "DescribeBulkImportJobResponse.job_last_update_date required"
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
