"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FunctionInvocationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.action_invocation_type
    import capo_bedrock_agent_runtime.types.function_parameters
    import capo_bedrock_agent_runtime.types.name


class FunctionInvocationInput(TypedDict, closed=True):
    action_group: "str"
    """<p>The action group that the function belongs to.</p>"""
    parameters: NotRequired[
        "capo_bedrock_agent_runtime.types.function_parameters.FunctionParameters"
    ]
    """<p>A list of parameters of the function.</p>"""
    function: NotRequired["str"]
    """<p>The name of the function.</p>"""
    action_invocation_type: NotRequired[
        "capo_bedrock_agent_runtime.types.action_invocation_type.ActionInvocationType"
    ]
    """<p>Contains information about the function to invoke,</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""
    collaborator_name: NotRequired["capo_bedrock_agent_runtime.types.name.Name"]
    """<p>The collaborator's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionInvocationInput) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "parameters" in value:
        import capo_bedrock_agent_runtime.types.function_parameters

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.function_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "function" in value:
        out["function"] = value["function"]
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


def deserialize_json(data: dict) -> FunctionInvocationInput:
    out: FunctionInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("actionGroup") is not None:
        out["action_group"] = data["actionGroup"]
    else:
        out["action_group"] = ""
    if data.get("parameters") is not None:
        import capo_bedrock_agent_runtime.types.function_parameters

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.function_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("function") is not None:
        out["function"] = data["function"]
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


def redact_sensitive(value: FunctionInvocationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "collaborator_name" in value:
        out["collaborator_name"] = "*** Sensitive Data Redacted ***"
    return out
