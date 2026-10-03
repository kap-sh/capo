"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupInvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.action_group_name
    import capo_bedrock_agent_runtime.types.api_path
    import capo_bedrock_agent_runtime.types.execution_type
    import capo_bedrock_agent_runtime.types.function
    import capo_bedrock_agent_runtime.types.parameters
    import capo_bedrock_agent_runtime.types.request_body
    import capo_bedrock_agent_runtime.types.verb


class ActionGroupInvocationInput(TypedDict, closed=True):
    action_group_name: NotRequired[
        "capo_bedrock_agent_runtime.types.action_group_name.ActionGroupName"
    ]
    """<p>The name of the action group.</p>"""
    verb: NotRequired["capo_bedrock_agent_runtime.types.verb.Verb"]
    """<p>The API method being used, based off the action group.</p>"""
    api_path: NotRequired["capo_bedrock_agent_runtime.types.api_path.ApiPath"]
    """<p>The path to the API to call, based off the action group.</p>"""
    parameters: NotRequired["capo_bedrock_agent_runtime.types.parameters.Parameters"]
    """<p>The parameters in the Lambda input event.</p>"""
    request_body: NotRequired[
        "capo_bedrock_agent_runtime.types.request_body.RequestBody"
    ]
    """<p>The parameters in the request body for the Lambda input event.</p>"""
    function: NotRequired["capo_bedrock_agent_runtime.types.function.Function"]
    """<p>The function in the action group to call.</p>"""
    execution_type: NotRequired[
        "capo_bedrock_agent_runtime.types.execution_type.ExecutionType"
    ]
    """<p>How fulfillment of the action is handled. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/action-handle.html">Handling fulfillment of the action</a>.</p>"""
    invocation_id: NotRequired["str"]
    """<p>The unique identifier of the invocation. Only returned if the <code>executionType</code> is <code>RETURN_CONTROL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupInvocationInput) -> dict:
    out: dict = {}
    if "action_group_name" in value:
        out["actionGroupName"] = value["action_group_name"]
    if "verb" in value:
        out["verb"] = value["verb"]
    if "api_path" in value:
        out["apiPath"] = value["api_path"]
    if "parameters" in value:
        import capo_bedrock_agent_runtime.types.parameters

        out["parameters"] = capo_bedrock_agent_runtime.types.parameters.serialize_json(
            value["parameters"]
        )
    if "request_body" in value:
        import capo_bedrock_agent_runtime.types.request_body

        out["requestBody"] = (
            capo_bedrock_agent_runtime.types.request_body.serialize_json(
                value["request_body"]
            )
        )
    if "function" in value:
        out["function"] = value["function"]
    if "execution_type" in value:
        import capo_bedrock_agent_runtime.types.execution_type

        out["executionType"] = (
            capo_bedrock_agent_runtime.types.execution_type.serialize_json(
                value["execution_type"]
            )
        )
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> ActionGroupInvocationInput:
    out: ActionGroupInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("actionGroupName") is not None:
        out["action_group_name"] = data["actionGroupName"]
    if data.get("verb") is not None:
        out["verb"] = data["verb"]
    if data.get("apiPath") is not None:
        out["api_path"] = data["apiPath"]
    if data.get("parameters") is not None:
        import capo_bedrock_agent_runtime.types.parameters

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.parameters.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("requestBody") is not None:
        import capo_bedrock_agent_runtime.types.request_body

        out["request_body"] = (
            capo_bedrock_agent_runtime.types.request_body.deserialize_json(
                data["requestBody"]
            )
        )
    if data.get("function") is not None:
        out["function"] = data["function"]
    if data.get("executionType") is not None:
        import capo_bedrock_agent_runtime.types.execution_type

        out["execution_type"] = (
            capo_bedrock_agent_runtime.types.execution_type.deserialize_json(
                data["executionType"]
            )
        )
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    return out
