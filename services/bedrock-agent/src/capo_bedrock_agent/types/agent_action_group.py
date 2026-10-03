"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentActionGroup``."""

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
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.function_schema
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.version


class AgentActionGroup(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent to which the action group belongs.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent to which the action group belongs.</p>"""
    action_group_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group.</p>"""
    action_group_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the action group.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the action group.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was last updated.</p>"""
    parent_action_signature: NotRequired[
        "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
    ]
    """<p>If this field is set as <code>AMAZON.UserInput</code>, the agent can request the user for additional information when trying to complete a task. The <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields must be blank for this action group.</p> <p>During orchestration, if the agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>"""
    parent_action_group_signature_params: NotRequired[
        "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
    ]
    """<p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>"""
    action_group_executor: NotRequired[
        "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>"""
    api_schema: NotRequired["capo_bedrock_agent.types.api_schema.APISchema"]
    """<p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>"""
    function_schema: NotRequired[
        "capo_bedrock_agent.types.function_schema.FunctionSchema"
    ]
    """<p>Defines functions that each define parameters that the agent needs to invoke from the user. Each function represents an action in an action group.</p>"""
    action_group_state: "capo_bedrock_agent.types.action_group_state.ActionGroupState"
    """<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentActionGroup) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    out["actionGroupId"] = value["action_group_id"]
    out["actionGroupName"] = value["action_group_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "parent_action_signature" in value:
        import capo_bedrock_agent.types.action_group_signature

        out["parentActionSignature"] = (
            capo_bedrock_agent.types.action_group_signature.serialize_json(
                value["parent_action_signature"]
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
    if "function_schema" in value:
        import capo_bedrock_agent.types.function_schema

        out["functionSchema"] = capo_bedrock_agent.types.function_schema.serialize_json(
            value["function_schema"]
        )
    import capo_bedrock_agent.types.action_group_state

    out["actionGroupState"] = (
        capo_bedrock_agent.types.action_group_state.serialize_json(
            value["action_group_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentActionGroup:
    out: AgentActionGroup = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentActionGroup.agent_id required")
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentActionGroup.agent_version required")
    if data.get("actionGroupId") is not None:
        out["action_group_id"] = data["actionGroupId"]
    else:
        raise DeserializationError("AgentActionGroup.action_group_id required")
    if data.get("actionGroupName") is not None:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError("AgentActionGroup.action_group_name required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentActionGroup.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentActionGroup.updated_at required")
    if data.get("parentActionSignature") is not None:
        import capo_bedrock_agent.types.action_group_signature

        out["parent_action_signature"] = (
            capo_bedrock_agent.types.action_group_signature.deserialize_json(
                data["parentActionSignature"]
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
    if data.get("functionSchema") is not None:
        import capo_bedrock_agent.types.function_schema

        out["function_schema"] = (
            capo_bedrock_agent.types.function_schema.deserialize_json(
                data["functionSchema"]
            )
        )
    if data.get("actionGroupState") is not None:
        import capo_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            capo_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    else:
        raise DeserializationError("AgentActionGroup.action_group_state required")
    return out
