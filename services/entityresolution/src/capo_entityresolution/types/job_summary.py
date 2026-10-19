"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.job_id
    import capo_entityresolution.types.job_status


class JobSummary(TypedDict, closed=True):
    job_id: "capo_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    status: "capo_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_entityresolution.types.job_status

    out["status"] = capo_entityresolution.types.job_status.serialize_json(
        value["status"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["startTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_entityresolution.types._prelude.timestamp

        out["endTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        import capo_entityresolution.types.job_status

        out["status"] = capo_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_entityresolution.types.job_status.JobStatus", ""
        )
    if data.get("startTime") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    return out
