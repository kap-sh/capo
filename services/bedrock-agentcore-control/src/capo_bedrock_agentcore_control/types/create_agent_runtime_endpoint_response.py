"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateAgentRuntimeEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.endpoint_name


class CreateAgentRuntimeEndpointResponse(TypedDict, closed=True):
    target_version: (
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The target version of the AgentCore Runtime for the endpoint.</p>"""
    agent_runtime_endpoint_arn: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.</p>"""
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    agent_runtime_id: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    ]
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    endpoint_name: NotRequired[
        "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    ]
    """<p>The name of the AgentCore Runtime endpoint.</p>"""
    status: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the AgentCore Runtime endpoint.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime endpoint was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRuntimeEndpointResponse) -> dict:
    out: dict = {}
    out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    if "agent_runtime_id" in value:
        out["agentRuntimeId"] = value["agent_runtime_id"]
    if "endpoint_name" in value:
        out["endpointName"] = value["endpoint_name"]
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAgentRuntimeEndpointResponse:
    out: CreateAgentRuntimeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    else:
        out["target_version"] = ""
    if data.get("agentRuntimeEndpointArn") is not None:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        out["agent_runtime_endpoint_arn"] = ""
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
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
    return out


def redact_sensitive(value: CreateAgentRuntimeEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_name" in value:
        out["endpoint_name"] = "*** Sensitive Data Redacted ***"
    return out
