"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version


class AgentRuntimeVersionSummary(TypedDict, closed=True):
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the agent runtime.</p>"""
    agent_runtime_version: (
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The version of the agent runtime.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the agent runtime version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeVersionSummary) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentRuntimeVersionSummary:
    out: AgentRuntimeVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        out["agent_runtime_version"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus",
            "",
        )
    return out
