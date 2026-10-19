"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeEndpointResponse``."""

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


class GetAgentRuntimeEndpointResponse(TypedDict, closed=True):
    live_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The currently deployed version of the AgentCore Runtime on the endpoint.</p>"""
    target_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The target version of the AgentCore Runtime for the endpoint.</p>"""
    agent_runtime_endpoint_arn: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.</p>"""
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
    ]
    """<p>The description of the AgentCore Runtime endpoint.</p>"""
    status: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the AgentCore Runtime endpoint.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime endpoint was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime endpoint was last updated.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the AgentCore Runtime endpoint is in a failed state.</p>"""
    name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint.</p>"""
    id: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_id.AgentRuntimeEndpointId"
    """<p>The unique identifier of the AgentCore Runtime endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeEndpointResponse) -> dict:
    out: dict = {}
    if "live_version" in value:
        out["liveVersion"] = value["live_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    if "description" in value:
        out["description"] = value["description"]
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
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeEndpointResponse:
    out: GetAgentRuntimeEndpointResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
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
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out


def redact_sensitive(value: GetAgentRuntimeEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
