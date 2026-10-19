"""Generated from Smithy shape ``com.amazonaws.securityagent#StartThreatModelJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.job_status


class StartThreatModelJobOutput(TypedDict, closed=True):
    title: NotRequired["str"]
    """<p>The title of the threat model job.</p>"""
    status: NotRequired["capo_securityagent.types.job_status.JobStatus"]
    """<p>The current status of the threat model job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job was last updated, in UTC format.</p>"""
    threat_model_id: NotRequired["str"]
    """<p>The unique identifier of the threat model.</p>"""
    threat_model_job_id: "str"
    """<p>The unique identifier of the started threat model job.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThreatModelJobOutput) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "status" in value:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "threat_model_id" in value:
        out["threatModelId"] = value["threat_model_id"]
    out["threatModelJobId"] = value["threat_model_job_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> StartThreatModelJobOutput:
    out: StartThreatModelJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("status") is not None:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.deserialize_json(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    if data.get("threatModelJobId") is not None:
        out["threat_model_job_id"] = data["threatModelJobId"]
    else:
        out["threat_model_job_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    return out
