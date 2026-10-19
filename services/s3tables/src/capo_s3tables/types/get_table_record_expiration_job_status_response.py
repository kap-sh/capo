"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableRecordExpirationJobStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.table_record_expiration_job_metrics
    import capo_s3tables.types.table_record_expiration_job_status


class GetTableRecordExpirationJobStatusResponse(TypedDict, closed=True):
    status: "capo_s3tables.types.table_record_expiration_job_status.TableRecordExpirationJobStatus"
    """<p>The current status of the most recent expiration job.</p>"""
    last_run_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the expiration job was last executed.</p>"""
    failure_message: NotRequired["str"]
    """<p>If the job failed, this field contains an error message describing the failure reason.</p>"""
    metrics: NotRequired[
        "capo_s3tables.types.table_record_expiration_job_metrics.TableRecordExpirationJobMetrics"
    ]
    """<p>Metrics about the most recent expiration job execution, including the number of records and files deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableRecordExpirationJobStatusResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_record_expiration_job_status

    out["status"] = (
        capo_s3tables.types.table_record_expiration_job_status.serialize_json(
            value["status"]
        )
    )
    if "last_run_timestamp" in value:
        import capo_s3tables._protocol.serialize

        out["lastRunTimestamp"] = capo_s3tables._protocol.serialize.fmt_date_time(
            value["last_run_timestamp"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "metrics" in value:
        import capo_s3tables.types.table_record_expiration_job_metrics

        out["metrics"] = (
            capo_s3tables.types.table_record_expiration_job_metrics.serialize_json(
                value["metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTableRecordExpirationJobStatusResponse:
    out: GetTableRecordExpirationJobStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_s3tables.types.table_record_expiration_job_status

        out["status"] = (
            capo_s3tables.types.table_record_expiration_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3tables.types.table_record_expiration_job_status.TableRecordExpirationJobStatus",
            "",
        )
    if data.get("lastRunTimestamp") is not None:
        import datetime

        out["last_run_timestamp"] = datetime.datetime.fromisoformat(
            data["lastRunTimestamp"].replace("Z", "+00:00")
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("metrics") is not None:
        import capo_s3tables.types.table_record_expiration_job_metrics

        out["metrics"] = (
            capo_s3tables.types.table_record_expiration_job_metrics.deserialize_json(
                data["metrics"]
            )
        )
    return out
