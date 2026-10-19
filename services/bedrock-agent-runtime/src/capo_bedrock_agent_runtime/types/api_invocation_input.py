"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiInvocationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.action_invocation_type
    import capo_bedrock_agent_runtime.types.api_parameters
    import capo_bedrock_agent_runtime.types.api_path
    import capo_bedrock_agent_runtime.types.api_request_body
    import capo_bedrock_agent_runtime.types.name


class ApiInvocationInput(TypedDict, closed=True):
    action_group: "str"
    """<p>The action group that the API operation belongs to.</p>"""
    http_method: NotRequired["str"]
    """<p>The HTTP method of the API operation.</p>"""
    api_path: NotRequired["capo_bedrock_agent_runtime.types.api_path.ApiPath"]
    """<p>The path to the API operation.</p>"""
    parameters: NotRequired[
        "capo_bedrock_agent_runtime.types.api_parameters.ApiParameters"
    ]
    """<p>The parameters to provide for the API request, as the agent elicited from the user.</p>"""
    request_body: NotRequired[
        "capo_bedrock_agent_runtime.types.api_request_body.ApiRequestBody"
    ]
    """<p>The request body to provide for the API request, as the agent elicited from the user.</p>"""
    action_invocation_type: NotRequired[
        "capo_bedrock_agent_runtime.types.action_invocation_type.ActionInvocationType"
    ]
    """<p>Contains information about the API operation to invoke.</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""
    collaborator_name: NotRequired["capo_bedrock_agent_runtime.types.name.Name"]
    """<p>The agent collaborator's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiInvocationInput) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "api_path" in value:
        out["apiPath"] = value["api_path"]
    if "parameters" in value:
        import capo_bedrock_agent_runtime.types.api_parameters

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.api_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "request_body" in value:
        import capo_bedrock_agent_runtime.types.api_request_body

        out["requestBody"] = (
            capo_bedrock_agent_runtime.types.api_request_body.serialize_json(
                value["request_body"]
            )
        )
    if "action_invocation_type" in value:
        import capo_bedrock_agent_runtime.types.action_invocation_type

        out["actionInvocationType"] = (
            capo_bedrock_agent_runtime.types.action_invocation_type.serialize_json(
                value["action_invocation_type"]
            )
        )
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "collaborator_name" in value:
        out["collaboratorName"] = value["collaborator_name"]
    return out


def deserialize_json(data: dict) -> ApiInvocationInput:
    out: ApiInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("actionGroup") is not None:
        out["action_group"] = data["actionGroup"]
    else:
        out["action_group"] = ""
    if data.get("httpMethod") is not None:
        out["http_method"] = data["httpMethod"]
    if data.get("apiPath") is not None:
        out["api_path"] = data["apiPath"]
    if data.get("parameters") is not None:
        import capo_bedrock_agent_runtime.types.api_parameters

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.api_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("requestBody") is not None:
        import capo_bedrock_agent_runtime.types.api_request_body

        out["request_body"] = (
            capo_bedrock_agent_runtime.types.api_request_body.deserialize_json(
                data["requestBody"]
            )
        )
    if data.get("actionInvocationType") is not None:
        import capo_bedrock_agent_runtime.types.action_invocation_type

        out["action_invocation_type"] = (
            capo_bedrock_agent_runtime.types.action_invocation_type.deserialize_json(
                data["actionInvocationType"]
            )
        )
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    if data.get("collaboratorName") is not None:
        out["collaborator_name"] = data["collaboratorName"]
    return out


def redact_sensitive(value: ApiInvocationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_path" in value:
        out["api_path"] = "*** Sensitive Data Redacted ***"
    if "collaborator_name" in value:
        out["collaborator_name"] = "*** Sensitive Data Redacted ***"
    return out
