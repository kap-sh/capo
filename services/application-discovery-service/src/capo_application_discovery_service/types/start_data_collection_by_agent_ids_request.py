"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartDataCollectionByAgentIdsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_ids


class StartDataCollectionByAgentIdsRequest(TypedDict, closed=True):
    agent_ids: "capo_application_discovery_service.types.agent_ids.AgentIds"
    """<p>The IDs of the agents from which to start collecting data. If you send a request to an agent ID that you do not have permission to contact, according to your Amazon Web Services account, the service does not throw an exception. Instead, it returns the error in the <i>Description</i> field. If you send a request to multiple agents and you do not have permission to contact some of those agents, the system does not throw an exception. Instead, the system shows <code>Failed</code> in the <i>Description</i> field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataCollectionByAgentIdsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.agent_ids

    out["agentIds"] = (
        capo_application_discovery_service.types.agent_ids.serialize_aws_json_1_1(
            value["agent_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataCollectionByAgentIdsRequest:
    out: StartDataCollectionByAgentIdsRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentIds") is not None:
        import capo_application_discovery_service.types.agent_ids

        out["agent_ids"] = (
            capo_application_discovery_service.types.agent_ids.deserialize_aws_json_1_1(
                data["agentIds"]
            )
        )
    else:
        out["agent_ids"] = []
    return out
