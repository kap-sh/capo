"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_collaboration
    import capo_bedrock_agent.types.agent_role_arn
    import capo_bedrock_agent.types.custom_orchestration
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.instruction
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.memory_configuration
    import capo_bedrock_agent.types.model_identifier
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.orchestration_type
    import capo_bedrock_agent.types.prompt_override_configuration
    import capo_bedrock_agent.types.session_ttl


class UpdateAgentRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_name: "capo_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the agent.</p>"""
    instruction: NotRequired["capo_bedrock_agent.types.instruction.Instruction"]
    """<p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>"""
    foundation_model: NotRequired[
        "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
    ]
    """<p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description of the agent.</p>"""
    orchestration_type: NotRequired[
        "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
    ]
    """<p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>"""
    custom_orchestration: NotRequired[
        "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
    ]
    """<p> Contains details of the custom orchestration configured for the agent. </p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_bedrock_agent.types.session_ttl.SessionTTL"
    ]
    """<p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>"""
    agent_resource_role_arn: "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>"""
    prompt_override_configuration: NotRequired[
        "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
    ]
    """<p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>The unique Guardrail configuration assigned to the agent when it is updated.</p>"""
    memory_configuration: NotRequired[
        "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
    ]
    """<p>Specifies the new memory configuration for the agent. </p>"""
    agent_collaboration: NotRequired[
        "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
    ]
    """<p>The agent's collaboration role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequest) -> dict:
    out: dict = {}
    out["agentName"] = value["agent_name"]
    if "instruction" in value:
        out["instruction"] = value["instruction"]
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
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    out["agentResourceRoleArn"] = value["agent_resource_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
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


def deserialize_json(data: dict) -> UpdateAgentRequest:
    out: UpdateAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentName") is not None:
        out["agent_name"] = data["agentName"]
    else:
        raise DeserializationError("UpdateAgentRequest.agent_name required")
    if data.get("instruction") is not None:
        out["instruction"] = data["instruction"]
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
    if data.get("agentResourceRoleArn") is not None:
        out["agent_resource_role_arn"] = data["agentResourceRoleArn"]
    else:
        raise DeserializationError(
            "UpdateAgentRequest.agent_resource_role_arn required"
        )
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
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
