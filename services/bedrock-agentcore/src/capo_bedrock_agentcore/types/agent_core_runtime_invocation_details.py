"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentCoreRuntimeInvocationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_runtime_endpoint_arn
    import capo_bedrock_agentcore.types.agent_runtime_version
    import capo_bedrock_agentcore.types.request_template


class AgentCoreRuntimeInvocationDetails(TypedDict, closed=True):
    agent_runtime_endpoint_arn: "capo_bedrock_agentcore.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime endpoint that the batch evaluation invoked.</p>"""
    agent_runtime_version: (
        "capo_bedrock_agentcore.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The version of the agent runtime that the endpoint pointed to when the batch evaluation started. If you update the endpoint after the batch evaluation starts, each later turn uses the version that the endpoint points to when the turn runs.</p>"""
    request_template: NotRequired[
        "capo_bedrock_agentcore.types.request_template.RequestTemplate"
    ]
    """<p>The request payload template that the batch evaluation used for each turn. If the request didn't specify a template, this is the default template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreRuntimeInvocationDetails) -> dict:
    out: dict = {}
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    if "request_template" in value:
        out["requestTemplate"] = value["request_template"]
    return out


def deserialize_json(data: dict) -> AgentCoreRuntimeInvocationDetails:
    out: AgentCoreRuntimeInvocationDetails = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeEndpointArn") is not None:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        out["agent_runtime_endpoint_arn"] = ""
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        out["agent_runtime_version"] = ""
    if data.get("requestTemplate") is not None:
        out["request_template"] = data["requestTemplate"]
    return out
