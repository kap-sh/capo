"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntime``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_name
    import capo_bedrock_agentcore_control.types.agent_runtime_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description


class AgentRuntime(TypedDict, closed=True):
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the agent runtime.</p>"""
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the agent runtime.</p>"""
    agent_runtime_version: (
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The version of the agent runtime.</p>"""
    agent_runtime_name: (
        "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    )
    """<p>The name of the agent runtime.</p>"""
    description: "capo_bedrock_agentcore_control.types.description.Description"
    """<p>The description of the agent runtime.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime was last updated.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the agent runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntime) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentRuntime:
    out: AgentRuntime = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        out["agent_runtime_id"] = ""
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        out["agent_runtime_version"] = ""
    if data.get("agentRuntimeName") is not None:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        out["agent_runtime_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
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


def redact_sensitive(value: AgentRuntime) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
