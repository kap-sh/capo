"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.job_id
    import capo_drs.types.recovery_plan_server_impact_level
    import capo_drs.types.source_server_arn


class RecoveryPlanExecutionServer(TypedDict, closed=True):
    server_arn: "capo_drs.types.source_server_arn.SourceServerARN"
    """<p>The ARN of the source server.</p>"""
    impact_level: NotRequired[
        "capo_drs.types.recovery_plan_server_impact_level.RecoveryPlanServerImpactLevel"
    ]
    """Defaults to CRITICAL if not specified."""
    job_id: NotRequired["capo_drs.types.job_id.JobID"]
    """The DRS recovery job ID. Populated when recovery is initiated for this server."""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionServer) -> dict:
    out: dict = {}
    out["serverArn"] = value["server_arn"]
    if "impact_level" in value:
        out["impactLevel"] = value["impact_level"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> RecoveryPlanExecutionServer:
    out: RecoveryPlanExecutionServer = {}  # type: ignore[typeddict-item]
    if data.get("serverArn") is not None:
        out["server_arn"] = data["serverArn"]
    else:
        out["server_arn"] = ""
    if data.get("impactLevel") is not None:
        out["impact_level"] = data["impactLevel"]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    return out
