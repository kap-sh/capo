"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Agent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_arn
    import capo_bedrock_agent.types.agent_collaboration
    import capo_bedrock_agent.types.agent_role_arn
    import capo_bedrock_agent.types.agent_status
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.custom_orchestration
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.failure_reasons
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.instruction
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.memory_configuration
    import capo_bedrock_agent.types.model_identifier
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.orchestration_type
    import capo_bedrock_agent.types.prompt_override_configuration
    import capo_bedrock_agent.types.recommended_actions
    import capo_bedrock_agent.types.session_ttl


class Agent(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the agent.</p>"""
    agent_arn: "capo_bedrock_agent.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    instruction: NotRequired["capo_bedrock_agent.types.instruction.Instruction"]
    """<p>Instructions that tell the agent what it should do and how it should interact with users.</p>"""
    agent_status: "capo_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent and whether it is ready for use. The following statuses are possible:</p> <ul> <li> <p>CREATING – The agent is being created.</p> </li> <li> <p>PREPARING – The agent is being prepared.</p> </li> <li> <p>PREPARED – The agent is prepared and ready to be invoked.</p> </li> <li> <p>NOT_PREPARED – The agent has been created but not yet prepared.</p> </li> <li> <p>FAILED – The agent API operation failed.</p> </li> <li> <p>UPDATING – The agent is being updated.</p> </li> <li> <p>DELETING – The agent is being deleted.</p> </li> </ul>"""
    foundation_model: NotRequired[
        "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
    ]
    """<p>The foundation model used for orchestration by the agent.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the agent.</p>"""
    orchestration_type: NotRequired[
        "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
    ]
    """<p> Specifies the orchestration strategy for the agent. </p>"""
    custom_orchestration: NotRequired[
        "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
    ]
    """<p> Contains custom orchestration configurations for the agent. </p>"""
    idle_session_ttl_in_seconds: "capo_bedrock_agent.types.session_ttl.SessionTTL"
    """<p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>"""
    agent_resource_role_arn: "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key that encrypts the agent.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the agent was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the agent was last updated.</p>"""
    prepared_at: NotRequired["capo_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The time at which the agent was last prepared.</p>"""
    failure_reasons: NotRequired[
        "capo_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>Contains reasons that the agent-related API that you invoked failed.</p>"""
    recommended_actions: NotRequired[
        "capo_bedrock_agent.types.recommended_actions.RecommendedActions"
    ]
    """<p>Contains recommended actions to take for the agent-related API that you invoked to succeed.</p>"""
    prompt_override_configuration: NotRequired[
        "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
    ]
    """<p>Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Details about the guardrail associated with the agent.</p>"""
    memory_configuration: NotRequired[
        "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
    ]
    """<p>Contains memory configuration for the agent.</p>"""
    agent_collaboration: NotRequired[
        "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
    ]
    """<p>The agent's collaboration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Agent) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentName"] = value["agent_name"]
    out["agentArn"] = value["agent_arn"]
    out["agentVersion"] = value["agent_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "instruction" in value:
        out["instruction"] = value["instruction"]
    import capo_bedrock_agent.types.agent_status

    out["agentStatus"] = capo_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    if "foundation_model" in value:
        out["foundationModel"] = value["foundation_model"]
    if "description" in value:
        out["description"] = value["description"]
    if "orchestration_type" in value:
        import capo_bedrock_agent.types.orchestration_type

        out["orchestrationType"] = (
            capo_bedrock_agent.types.orchestration_type.serialize_json(
                value["orchestration_type"]
            )
        )
    if "custom_orchestration" in value:
        import capo_bedrock_agent.types.custom_orchestration

        out["customOrchestration"] = (
            capo_bedrock_agent.types.custom_orchestration.serialize_json(
                value["custom_orchestration"]
            )
        )
    out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    out["agentResourceRoleArn"] = value["agent_resource_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "prepared_at" in value:
        import capo_bedrock_agent.types.date_timestamp

        out["preparedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
            value["prepared_at"]
        )
    if "failure_reasons" in value:
        import capo_bedrock_agent.types.failure_reasons

        out["failureReasons"] = capo_bedrock_agent.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    if "recommended_actions" in value:
        import capo_bedrock_agent.types.recommended_actions

        out["recommendedActions"] = (
            capo_bedrock_agent.types.recommended_actions.serialize_json(
                value["recommended_actions"]
            )
        )
    if "prompt_override_configuration" in value:
        import capo_bedrock_agent.types.prompt_override_configuration

        out["promptOverrideConfiguration"] = (
            capo_bedrock_agent.types.prompt_override_configuration.serialize_json(
                value["prompt_override_configuration"]
            )
        )
    if "guardrail_configuration" in value:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            capo_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "memory_configuration" in value:
        import capo_bedrock_agent.types.memory_configuration

        out["memoryConfiguration"] = (
            capo_bedrock_agent.types.memory_configuration.serialize_json(
                value["memory_configuration"]
            )
        )
    if "agent_collaboration" in value:
        import capo_bedrock_agent.types.agent_collaboration

        out["agentCollaboration"] = (
            capo_bedrock_agent.types.agent_collaboration.serialize_json(
                value["agent_collaboration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Agent:
    out: Agent = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("Agent.agent_id required")
    if data.get("agentName") is not None:
        out["agent_name"] = data["agentName"]
    else:
        raise DeserializationError("Agent.agent_name required")
    if data.get("agentArn") is not None:
        out["agent_arn"] = data["agentArn"]
    else:
        raise DeserializationError("Agent.agent_arn required")
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("Agent.agent_version required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("instruction") is not None:
        out["instruction"] = data["instruction"]
    if data.get("agentStatus") is not None:
        import capo_bedrock_agent.types.agent_status

        out["agent_status"] = capo_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("Agent.agent_status required")
    if data.get("foundationModel") is not None:
        out["foundation_model"] = data["foundationModel"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("orchestrationType") is not None:
        import capo_bedrock_agent.types.orchestration_type

        out["orchestration_type"] = (
            capo_bedrock_agent.types.orchestration_type.deserialize_json(
                data["orchestrationType"]
            )
        )
    if data.get("customOrchestration") is not None:
        import capo_bedrock_agent.types.custom_orchestration

        out["custom_orchestration"] = (
            capo_bedrock_agent.types.custom_orchestration.deserialize_json(
                data["customOrchestration"]
            )
        )
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    else:
        raise DeserializationError("Agent.idle_session_ttl_in_seconds required")
    if data.get("agentResourceRoleArn") is not None:
        out["agent_resource_role_arn"] = data["agentResourceRoleArn"]
    else:
        raise DeserializationError("Agent.agent_resource_role_arn required")
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Agent.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Agent.updated_at required")
    if data.get("preparedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["prepared_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["preparedAt"]
        )
    if data.get("failureReasons") is not None:
        import capo_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            capo_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if data.get("recommendedActions") is not None:
        import capo_bedrock_agent.types.recommended_actions

        out["recommended_actions"] = (
            capo_bedrock_agent.types.recommended_actions.deserialize_json(
                data["recommendedActions"]
            )
        )
    if data.get("promptOverrideConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_override_configuration

        out["prompt_override_configuration"] = (
            capo_bedrock_agent.types.prompt_override_configuration.deserialize_json(
                data["promptOverrideConfiguration"]
            )
        )
    if data.get("guardrailConfiguration") is not None:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            capo_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if data.get("memoryConfiguration") is not None:
        import capo_bedrock_agent.types.memory_configuration

        out["memory_configuration"] = (
            capo_bedrock_agent.types.memory_configuration.deserialize_json(
                data["memoryConfiguration"]
            )
        )
    if data.get("agentCollaboration") is not None:
        import capo_bedrock_agent.types.agent_collaboration

        out["agent_collaboration"] = (
            capo_bedrock_agent.types.agent_collaboration.deserialize_json(
                data["agentCollaboration"]
            )
        )
    return out
