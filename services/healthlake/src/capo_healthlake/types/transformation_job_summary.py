"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_job_id
    import capo_healthlake.types.data_transformation_job_name
    import capo_healthlake.types.date_time
    import capo_healthlake.types.source_format
    import capo_healthlake.types.transformation_job_status


class TransformationJobSummary(TypedDict, closed=True):
    job_id: "capo_healthlake.types.data_transformation_job_id.DataTransformationJobId"
    """<p>The unique identifier of the job.</p>"""
    job_status: (
        "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
    )
    """<p>The current status of the job.</p>"""
    submit_time: "capo_healthlake.types.date_time.DateTime"
    """<p>The timestamp when the job was submitted.</p>"""
    job_name: NotRequired[
        "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
    ]
    """<p>The name of the job.</p>"""
    end_time: NotRequired["capo_healthlake.types.date_time.DateTime"]
    """<p>The timestamp when the job completed.</p>"""
    source_format: NotRequired["capo_healthlake.types.source_format.SourceFormat"]
    """<p>The source data format for this job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationJobSummary) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import capo_healthlake.types.transformation_job_status

    out["JobStatus"] = (
        capo_healthlake.types.transformation_job_status.serialize_aws_json_1_0(
            value["job_status"]
        )
    )
    import capo_healthlake.types.date_time

    out["SubmitTime"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
        value["submit_time"]
    )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "end_time" in value:
        import capo_healthlake.types.date_time

        out["EndTime"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "source_format" in value:
        import capo_healthlake.types.source_format

        out["SourceFormat"] = (
            capo_healthlake.types.source_format.serialize_aws_json_1_0(
                value["source_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformationJobSummary:
    out: TransformationJobSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("EndTime") is not None:
        import capo_healthlake.types.date_time

        out["end_time"] = capo_healthlake.types.date_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    return out
