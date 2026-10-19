"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CancelEnrichmentJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.id


class CancelEnrichmentJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the cancelled enrichment job.</p>"""
    status: "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
    """<p>The status of the enrichment job after cancellation. This will be CANCELLED, indicating the job was successfully cancelled or was already in CANCELLED state (idempotent behavior).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelEnrichmentJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_iotsitewise.types.enrichment_job_status

    out["status"] = capo_iotsitewise.types.enrichment_job_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CancelEnrichmentJobResponse:
    out: CancelEnrichmentJobResponse = {}  # type: ignore[typeddict-item]
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
    return out
