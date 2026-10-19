"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetAgentSpacesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id_list


class BatchGetAgentSpacesInput(TypedDict, closed=True):
    agent_space_ids: "capo_securityagent.types.agent_space_id_list.AgentSpaceIdList"
    """<p>The list of agent space identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAgentSpacesInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.agent_space_id_list

    out["agentSpaceIds"] = capo_securityagent.types.agent_space_id_list.serialize_json(
        value["agent_space_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAgentSpacesInput:
    out: BatchGetAgentSpacesInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceIds") is not None:
        import capo_securityagent.types.agent_space_id_list

        out["agent_space_ids"] = (
            capo_securityagent.types.agent_space_id_list.deserialize_json(
                data["agentSpaceIds"]
            )
        )
    else:
        out["agent_space_ids"] = []
    return out
