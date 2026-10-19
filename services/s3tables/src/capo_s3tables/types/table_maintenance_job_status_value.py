"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobStatusValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.job_status


class TableMaintenanceJobStatusValue(TypedDict, closed=True):
    status: "capo_s3tables.types.job_status.JobStatus"
    """<p>The status of the job.</p>"""
    last_run_timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time that the maintenance job was last run.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message of a failed job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceJobStatusValue) -> dict:
    out: dict = {}
    import capo_s3tables.types.job_status

    out["status"] = capo_s3tables.types.job_status.serialize_json(value["status"])
    if "last_run_timestamp" in value:
        import capo_s3tables._protocol.serialize

        out["lastRunTimestamp"] = capo_s3tables._protocol.serialize.fmt_date_time(
            value["last_run_timestamp"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> TableMaintenanceJobStatusValue:
    out: TableMaintenanceJobStatusValue = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_s3tables.types.job_status

        out["status"] = capo_s3tables.types.job_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_s3tables.types.job_status.JobStatus", "")
    if data.get("lastRunTimestamp") is not None:
        import datetime

        out["last_run_timestamp"] = datetime.datetime.fromisoformat(
            data["lastRunTimestamp"].replace("Z", "+00:00")
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    return out
