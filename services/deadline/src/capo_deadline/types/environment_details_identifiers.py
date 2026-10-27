"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.environment_id
    import capo_deadline.types.job_id


class EnvironmentDetailsIdentifiers(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """The environment ID."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentDetailsIdentifiers:
    out: EnvironmentDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    return out
