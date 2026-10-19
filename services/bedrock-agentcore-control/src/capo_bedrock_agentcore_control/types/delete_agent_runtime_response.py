"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version


class DeleteAgentRuntimeResponse(TypedDict, closed=True):
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the AgentCore Runtime deletion.</p>"""
    agent_runtime_id: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    ]
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    agent_runtime_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The version of the AgentCore Runtime that was deleted. This value is present only when you delete a single version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    if "agent_runtime_id" in value:
        out["agentRuntimeId"] = value["agent_runtime_id"]
    if "agent_runtime_version" in value:
        out["agentRuntimeVersion"] = value["agent_runtime_version"]
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeResponse:
    out: DeleteAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    return out
