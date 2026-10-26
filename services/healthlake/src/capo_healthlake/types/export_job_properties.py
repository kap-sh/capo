"""Generated from Smithy shape ``com.amazonaws.healthlake#ExportJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.health_lake_timestamp
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.job_id
    import capo_healthlake.types.job_name
    import capo_healthlake.types.job_status
    import capo_healthlake.types.message
    import capo_healthlake.types.output_data_config


class ExportJobProperties(TypedDict, closed=True):
    job_id: "capo_healthlake.types.job_id.JobId"
    """<p>The export job identifier.</p>"""
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>The export job name.</p>"""
    job_status: "capo_healthlake.types.job_status.JobStatus"
    """<p>The export job status.</p>"""
    submit_time: "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    """<p>The time the export job was initiated.</p>"""
    end_time: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """<p>The time the export job completed.</p>"""
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier from which files are being exported.</p>"""
    output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig"
    """<p>The output data configuration supplied when the export job was created.</p>"""
    data_access_role_arn: NotRequired["capo_healthlake.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) used during the initiation of the export job.</p>"""
    message: NotRequired["capo_healthlake.types.message.Message"]
    """<p>An explanation of any errors that might have occurred during the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportJobProperties) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_healthlake.types.job_status

    out["JobStatus"] = capo_healthlake.types.job_status.serialize_aws_json_1_0(
        value["job_status"]
    )
    import capo_healthlake.types.health_lake_timestamp

    out["SubmitTime"] = (
        capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
            value["submit_time"]
        )
    )
    if "end_time" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["EndTime"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    out["DatastoreId"] = value["datastore_id"]
    import capo_healthlake.types.output_data_config

    out["OutputDataConfig"] = (
        capo_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportJobProperties:
    out: ExportJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.job_status

        out["job_status"] = capo_healthlake.types.job_status.deserialize_aws_json_1_0(
            data["JobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_healthlake.types.job_status.JobStatus", ""
        )
    if data.get("SubmitTime") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["submit_time"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["SubmitTime"]
            )
        )
    else:
        import datetime

        out["submit_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EndTime") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["end_time"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("OutputDataConfig") is not None:
        import capo_healthlake.types.output_data_config

        out["output_data_config"] = (
            capo_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        out["output_data_config"] = {"$unknown": {"name": ""}}
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
