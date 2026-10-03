"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentActionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.action_group_executor
    import capo_bedrock_agent.types.action_group_signature
    import capo_bedrock_agent.types.action_group_signature_params
    import capo_bedrock_agent.types.action_group_state
    import capo_bedrock_agent.types.api_schema
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.function_schema
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name


class CreateAgentActionGroupRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which to create the action group.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent for which to create the action group.</p>"""
    action_group_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name to give the action group.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description of the action group.</p>"""
    parent_action_group_signature: NotRequired[
        "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
    ]
    """<p>Specify a built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul>"""
    parent_action_group_signature_params: NotRequired[
        "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
    ]
    """<p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>"""
    action_group_executor: NotRequired[
        "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>"""
    api_schema: NotRequired["capo_bedrock_agent.types.api_schema.APISchema"]
    """<p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>"""
    action_group_state: NotRequired[
        "capo_bedrock_agent.types.action_group_state.ActionGroupState"
    ]
    """<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""
    function_schema: NotRequired[
        "capo_bedrock_agent.types.function_schema.FunctionSchema"
    ]
    """<p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentActionGroupRequest) -> dict:
    out: dict = {}
    out["actionGroupName"] = value["action_group_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_action_group_signature" in value:
        import capo_bedrock_agent.types.action_group_signature

        out["parentActionGroupSignature"] = (
            capo_bedrock_agent.types.action_group_signature.serialize_json(
                value["parent_action_group_signature"]
            )
        )
    if "parent_action_group_signature_params" in value:
        import capo_bedrock_agent.types.action_group_signature_params

        out["parentActionGroupSignatureParams"] = (
            capo_bedrock_agent.types.action_group_signature_params.serialize_json(
                value["parent_action_group_signature_params"]
            )
        )
    if "action_group_executor" in value:
        import capo_bedrock_agent.types.action_group_executor

        out["actionGroupExecutor"] = (
            capo_bedrock_agent.types.action_group_executor.serialize_json(
                value["action_group_executor"]
            )
        )
    if "api_schema" in value:
        import capo_bedrock_agent.types.api_schema

        out["apiSchema"] = capo_bedrock_agent.types.api_schema.serialize_json(
            value["api_schema"]
        )
    if "action_group_state" in value:
        import capo_bedrock_agent.types.action_group_state

        out["actionGroupState"] = (
            capo_bedrock_agent.types.action_group_state.serialize_json(
                value["action_group_state"]
            )
        )
    if "function_schema" in value:
        import capo_bedrock_agent.types.function_schema

        out["functionSchema"] = capo_bedrock_agent.types.function_schema.serialize_json(
            value["function_schema"]
        )
    return out


def deserialize_json(data: dict) -> CreateAgentActionGroupRequest:
    out: CreateAgentActionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("actionGroupName") is not None:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError(
            "CreateAgentActionGroupRequest.action_group_name required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parentActionGroupSignature") is not None:
        import capo_bedrock_agent.types.action_group_signature

        out["parent_action_group_signature"] = (
            capo_bedrock_agent.types.action_group_signature.deserialize_json(
                data["parentActionGroupSignature"]
            )
        )
    if data.get("parentActionGroupSignatureParams") is not None:
        import capo_bedrock_agent.types.action_group_signature_params

        out["parent_action_group_signature_params"] = (
            capo_bedrock_agent.types.action_group_signature_params.deserialize_json(
                data["parentActionGroupSignatureParams"]
            )
        )
    if data.get("actionGroupExecutor") is not None:
        import capo_bedrock_agent.types.action_group_executor

        out["action_group_executor"] = (
            capo_bedrock_agent.types.action_group_executor.deserialize_json(
                data["actionGroupExecutor"]
            )
        )
    if data.get("apiSchema") is not None:
        import capo_bedrock_agent.types.api_schema

        out["api_schema"] = capo_bedrock_agent.types.api_schema.deserialize_json(
            data["apiSchema"]
        )
    if data.get("actionGroupState") is not None:
        import capo_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            capo_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    if data.get("functionSchema") is not None:
        import capo_bedrock_agent.types.function_schema

        out["function_schema"] = (
            capo_bedrock_agent.types.function_schema.deserialize_json(
                data["functionSchema"]
            )
        )
    return out
