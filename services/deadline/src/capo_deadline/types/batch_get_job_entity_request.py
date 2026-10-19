"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.job_entity_identifiers
    import capo_deadline.types.worker_id


class BatchGetJobEntityRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the worker that's fetching job details. The worker must have an assignment on a job to fetch job details.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker that's fetching job details. The worker must have an assignment on a job to fetch job details.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID of the worker containing the job details to get.</p>"""
    identifiers: "capo_deadline.types.job_entity_identifiers.JobEntityIdentifiers"
    """<p>The job identifiers to include within the job entity batch details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.job_entity_identifiers

    out["identifiers"] = capo_deadline.types.job_entity_identifiers.serialize_json(
        value["identifiers"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobEntityRequest:
    out: BatchGetJobEntityRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.job_entity_identifiers

        out["identifiers"] = (
            capo_deadline.types.job_entity_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
