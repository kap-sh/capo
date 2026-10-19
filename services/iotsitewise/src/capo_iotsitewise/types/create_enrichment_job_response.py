"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateEnrichmentJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.id


class CreateEnrichmentJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>Unique identifier for the enrichment job. Use this ID with DescribeEnrichmentJob to monitor progress or with CancelEnrichmentJob to cancel the job.</p>"""
    status: "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
    """<p>Initial status of the enrichment job, typically PENDING. The job will transition to RUNNING when processing begins, then to a terminal state (COMPLETED, FAILED, TIMED_OUT, or CANCELLED). Use DescribeEnrichmentJob to track status changes.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the enrichment job was created in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnrichmentJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_iotsitewise.types.enrichment_job_status

    out["status"] = capo_iotsitewise.types.enrichment_job_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types._prelude.timestamp

    out["createdAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateEnrichmentJobResponse:
    out: CreateEnrichmentJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.enrichment_job_status

        out["status"] = capo_iotsitewise.types.enrichment_job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["created_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
