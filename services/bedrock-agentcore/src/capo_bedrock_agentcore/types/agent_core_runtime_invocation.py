"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentCoreRuntimeInvocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_runtime_endpoint_arn
    import capo_bedrock_agentcore.types.request_template


class AgentCoreRuntimeInvocation(TypedDict, closed=True):
    agent_runtime_endpoint_arn: "capo_bedrock_agentcore.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime endpoint to invoke. Specify an endpoint in the same account and Region as the batch evaluation. The service requires the endpoint and its agent runtime version to be ready. The agent runtime must use the HTTP protocol and IAM inbound authorization.</p>"""
    request_template: NotRequired[
        "capo_bedrock_agentcore.types.request_template.RequestTemplate"
    ]
    """<p>A JSON object template for the request payload sent to the agent for each turn. The template must contain the placeholder <code>{{turn.input}}</code> exactly once, as the complete value of a JSON string and not as a field name. The service replaces the placeholder with the input of the turn. If the input isn't a string, the service inserts it as a JSON value. If you don't specify a template, the service uses <code>{"prompt": "{{turn.input}}"}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreRuntimeInvocation) -> dict:
    out: dict = {}
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    if "request_template" in value:
        out["requestTemplate"] = value["request_template"]
    return out


def deserialize_json(data: dict) -> AgentCoreRuntimeInvocation:
    out: AgentCoreRuntimeInvocation = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeEndpointArn") is not None:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        out["agent_runtime_endpoint_arn"] = ""
    if data.get("requestTemplate") is not None:
        out["request_template"] = data["requestTemplate"]
    return out
