"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateAgentRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.workload_identity_details


class CreateAgentRuntimeResponse(TypedDict, closed=True):
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    workload_identity_details: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    """<p>The workload identity details for the AgentCore Runtime.</p>"""
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    agent_runtime_version: (
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The version of the AgentCore Runtime.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was created.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRuntimeResponse) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    if "workload_identity_details" in value:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    out["agentRuntimeId"] = value["agent_runtime_id"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAgentRuntimeResponse:
    out: CreateAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("workloadIdentityDetails") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        out["agent_runtime_id"] = ""
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        out["agent_runtime_version"] = ""
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
