"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_endpoint_description
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_id
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.endpoint_name


class AgentRuntimeEndpoint(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the agent runtime endpoint.</p>"""
    live_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The live version of the agent runtime endpoint. This is the version that is currently serving requests.</p>"""
    target_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The target version of the agent runtime endpoint. This is the version that the endpoint is being updated to.</p>"""
    agent_runtime_endpoint_arn: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime endpoint.</p>"""
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the agent runtime associated with the endpoint.</p>"""
    status: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the agent runtime endpoint.</p>"""
    id: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_id.AgentRuntimeEndpointId"
    """<p>The unique identifier of the agent runtime endpoint.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
    ]
    """<p>The description of the agent runtime endpoint.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime endpoint was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime endpoint was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "live_version" in value:
        out["liveVersion"] = value["live_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(
            value["status"]
        )
    )
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentRuntimeEndpoint:
    out: AgentRuntimeEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("liveVersion") is not None:
        out["live_version"] = data["liveVersion"]
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    if data.get("agentRuntimeEndpointArn") is not None:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        out["agent_runtime_endpoint_arn"] = ""
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus",
            "",
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    return out


def redact_sensitive(value: AgentRuntimeEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
