"""Generated from Smithy shape ``com.amazonaws.comprehend#StopEntitiesDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.job_id


class StopEntitiesDetectionJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehend.types.job_id.JobId"
    """<p>The identifier of the entities detection job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEntitiesDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEntitiesDetectionJobRequest:
    out: StopEntitiesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
