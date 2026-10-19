"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopDataCollectionByAgentIdsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_ids


class StopDataCollectionByAgentIdsRequest(TypedDict, closed=True):
    agent_ids: "capo_application_discovery_service.types.agent_ids.AgentIds"
    """<p>The IDs of the agents from which to stop collecting data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDataCollectionByAgentIdsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.agent_ids

    out["agentIds"] = (
        capo_application_discovery_service.types.agent_ids.serialize_aws_json_1_1(
            value["agent_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDataCollectionByAgentIdsRequest:
    out: StopDataCollectionByAgentIdsRequest = {}  # type: ignore[typeddict-item]
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
