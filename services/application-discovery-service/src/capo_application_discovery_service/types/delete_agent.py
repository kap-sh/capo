"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_id
    import capo_application_discovery_service.types.boolean


class DeleteAgent(TypedDict, closed=True):
    agent_id: "capo_application_discovery_service.types.agent_id.AgentId"
    """<p> The ID of the agent or data collector to delete. </p>"""
    force: "capo_application_discovery_service.types.boolean.Boolean"
    """<p> Optional flag used to force delete an agent or data collector. It is needed to delete any agent in HEALTHY/UNHEALTHY/RUNNING status. Note that deleting an agent that is actively reporting health causes it to be re-registered with a different agent ID after data collector re-connects with Amazon Web Services. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgent) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAgent:
    out: DeleteAgent = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("force") is not None:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
