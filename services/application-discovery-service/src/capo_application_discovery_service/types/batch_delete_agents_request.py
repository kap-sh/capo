"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.delete_agents


class BatchDeleteAgentsRequest(TypedDict, closed=True):
    delete_agents: "capo_application_discovery_service.types.delete_agents.DeleteAgents"
    """<p> The list of agents to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteAgentsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.delete_agents

    out["deleteAgents"] = (
        capo_application_discovery_service.types.delete_agents.serialize_aws_json_1_1(
            value["delete_agents"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteAgentsRequest:
    out: BatchDeleteAgentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("deleteAgents") is not None:
        import capo_application_discovery_service.types.delete_agents

        out["delete_agents"] = (
            capo_application_discovery_service.types.delete_agents.deserialize_aws_json_1_1(
                data["deleteAgents"]
            )
        )
    else:
        out["delete_agents"] = []
    return out
