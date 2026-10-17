"""Generated from Smithy shape ``com.amazonaws.sagemaker#EMRServerlessStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.emr_serverless_application_id
    import capo_sagemaker.types.emr_serverless_job_run_id
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.string1024


class EMRServerlessStepMetadata(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_sagemaker.types.emr_serverless_application_id.EMRServerlessApplicationId"
    ]
    """<p>The identifier of the Amazon EMR Serverless application.</p>"""
    job_run_id: NotRequired[
        "capo_sagemaker.types.emr_serverless_job_run_id.EMRServerlessJobRunId"
    ]
    """<p>The identifier of the Amazon EMR Serverless job run.</p>"""
    job_run_name: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The name of the Amazon EMR Serverless job run.</p>"""
    log_file_path: NotRequired["capo_sagemaker.types.string1024.String1024"]
    """<p>The path to the log file for the Amazon EMR Serverless job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EMRServerlessStepMetadata) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "job_run_name" in value:
        out["JobRunName"] = value["job_run_name"]
    if "log_file_path" in value:
        out["LogFilePath"] = value["log_file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EMRServerlessStepMetadata:
    out: EMRServerlessStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("JobRunId") is not None:
        out["job_run_id"] = data["JobRunId"]
    if data.get("JobRunName") is not None:
        out["job_run_name"] = data["JobRunName"]
    if data.get("LogFilePath") is not None:
        out["log_file_path"] = data["LogFilePath"]
    return out
