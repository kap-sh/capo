"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimeVersionsByCapacityProviderOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list


class ListAgentRuntimeVersionsByCapacityProviderOutput(TypedDict, closed=True):
    agent_runtimes: "capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list.AgentRuntimeVersionSummaryList"
    """<p>The list of agent runtime versions that are associated with the capacity provider.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimeVersionsByCapacityProviderOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list

    out["agentRuntimes"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list.serialize_json(
            value["agent_runtimes"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRuntimeVersionsByCapacityProviderOutput:
    out: ListAgentRuntimeVersionsByCapacityProviderOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimes") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list

        out["agent_runtimes"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_version_summary_list.deserialize_json(
                data["agentRuntimes"]
            )
        )
    else:
        out["agent_runtimes"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
