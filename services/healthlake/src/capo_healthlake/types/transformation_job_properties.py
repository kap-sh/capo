"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.bounded_string
    import capo_healthlake.types.data_transformation_iam_role_arn
    import capo_healthlake.types.data_transformation_job_id
    import capo_healthlake.types.data_transformation_job_name
    import capo_healthlake.types.date_time
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_name_string
    import capo_healthlake.types.transformation_input_data_config
    import capo_healthlake.types.transformation_job_progress_report
    import capo_healthlake.types.transformation_job_status
    import capo_healthlake.types.transformation_output_data_config


class TransformationJobProperties(TypedDict, closed=True):
    job_id: "capo_healthlake.types.data_transformation_job_id.DataTransformationJobId"
    """<p>The unique identifier of the data transformation job.</p>"""
    job_status: (
        "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
    )
    """<p>The current status of the data transformation job.</p>"""
    input_data_config: "capo_healthlake.types.transformation_input_data_config.TransformationInputDataConfig"
    """<p>The Amazon S3 location and format of the source files for this job.</p>"""
    output_data_config: "capo_healthlake.types.transformation_output_data_config.TransformationOutputDataConfig"
    """<p>The Amazon S3 location and encryption configuration for the converted output.</p>"""
    data_access_role_arn: "capo_healthlake.types.data_transformation_iam_role_arn.DataTransformationIamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that grants HealthLake access to the specified Amazon S3 locations. HealthLake assumes this role to read input files and write output files.</p>"""
    submit_time: "capo_healthlake.types.date_time.DateTime"
    """<p>The timestamp when the job was submitted.</p>"""
    job_name: NotRequired[
        "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
    ]
    """<p>The name of the data transformation job.</p>"""
    profile_id: NotRequired["capo_healthlake.types.profile_id_string.ProfileIdString"]
    """<p>The unique identifier of the data transformation profile used for this job.</p>"""
    profile_name: NotRequired[
        "capo_healthlake.types.profile_name_string.ProfileNameString"
    ]
    """<p>The name of the data transformation profile used for this job.</p>"""
    profile_version: NotRequired["int"]
    """<p>The version number of the data transformation profile used for this job.</p>"""
    end_time: NotRequired["capo_healthlake.types.date_time.DateTime"]
    """<p>The timestamp when the job completed or failed.</p>"""
    drift_detection_enabled: NotRequired["bool"]
    """<p>Specifies whether drift detection is enabled for this job. When enabled, HealthLake writes a drift report to the output Amazon S3 location alongside the converted files.</p>"""
    provenance_enabled: NotRequired["bool"]
    """<p>Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation job. When provenance is enabled, the service also generates related DocumentReference and Device resources.</p>"""
    message: NotRequired["capo_healthlake.types.bounded_string.BoundedString"]
    """<p>An informational message about the job, such as an error description if the job failed.</p>"""
    job_progress_report: NotRequired[
        "capo_healthlake.types.transformation_job_progress_report.TransformationJobProgressReport"
    ]
    """<p>The progress report for the data transformation job, including counts of files processed and resources generated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationJobProperties) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import capo_healthlake.types.transformation_job_status

    out["JobStatus"] = (
        capo_healthlake.types.transformation_job_status.serialize_aws_json_1_0(
            value["job_status"]
        )
    )
    import capo_healthlake.types.transformation_input_data_config

    out["InputDataConfig"] = (
        capo_healthlake.types.transformation_input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    import capo_healthlake.types.transformation_output_data_config

    out["OutputDataConfig"] = (
        capo_healthlake.types.transformation_output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    import capo_healthlake.types.date_time

    out["SubmitTime"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
        value["submit_time"]
    )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    if "end_time" in value:
        import capo_healthlake.types.date_time

        out["EndTime"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "drift_detection_enabled" in value:
        out["DriftDetectionEnabled"] = value["drift_detection_enabled"]
    if "provenance_enabled" in value:
        out["ProvenanceEnabled"] = value["provenance_enabled"]
    if "message" in value:
        out["Message"] = value["message"]
    if "job_progress_report" in value:
        import capo_healthlake.types.transformation_job_progress_report

        out["JobProgressReport"] = (
            capo_healthlake.types.transformation_job_progress_report.serialize_aws_json_1_0(
                value["job_progress_report"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformationJobProperties:
    out: TransformationJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.transformation_job_status

        out["job_status"] = (
            capo_healthlake.types.transformation_job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_healthlake.types.transformation_job_status.TransformationJobStatus",
            "",
        )
    if data.get("InputDataConfig") is not None:
        import capo_healthlake.types.transformation_input_data_config

        out["input_data_config"] = (
            capo_healthlake.types.transformation_input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "TransformationJobProperties.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_healthlake.types.transformation_output_data_config

        out["output_data_config"] = (
            capo_healthlake.types.transformation_output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "TransformationJobProperties.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    if data.get("SubmitTime") is not None:
        import capo_healthlake.types.date_time

        out["submit_time"] = capo_healthlake.types.date_time.deserialize_aws_json_1_0(
            data["SubmitTime"]
        )
    else:
        import datetime

        out["submit_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    if data.get("ProfileVersion") is not None:
        out["profile_version"] = data["ProfileVersion"]
    if data.get("EndTime") is not None:
        import capo_healthlake.types.date_time

        out["end_time"] = capo_healthlake.types.date_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("DriftDetectionEnabled") is not None:
        out["drift_detection_enabled"] = data["DriftDetectionEnabled"]
    if data.get("ProvenanceEnabled") is not None:
        out["provenance_enabled"] = data["ProvenanceEnabled"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("JobProgressReport") is not None:
        import capo_healthlake.types.transformation_job_progress_report

        out["job_progress_report"] = (
            capo_healthlake.types.transformation_job_progress_report.deserialize_aws_json_1_0(
                data["JobProgressReport"]
            )
        )
    return out
