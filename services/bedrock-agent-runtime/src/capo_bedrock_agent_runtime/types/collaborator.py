"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Collaborator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_action_groups
    import capo_bedrock_agent_runtime.types.agent_collaboration
    import capo_bedrock_agent_runtime.types.collaborator_configurations
    import capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn
    import capo_bedrock_agent_runtime.types.instruction
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.knowledge_bases
    import capo_bedrock_agent_runtime.types.model_identifier
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.prompt_override_configuration
    import capo_bedrock_agent_runtime.types.session_ttl


class Collaborator(TypedDict, closed=True):
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the AWS KMS key that encrypts the inline collaborator. </p>"""
    foundation_model: (
        "capo_bedrock_agent_runtime.types.model_identifier.ModelIdentifier"
    )
    """<p> The foundation model used by the inline collaborator agent. </p>"""
    instruction: "capo_bedrock_agent_runtime.types.instruction.Instruction"
    """<p> Instruction that tell the inline collaborator agent what it should do and how it should interact with users. </p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_bedrock_agent_runtime.types.session_ttl.SessionTTL"
    ]
    """<p> The number of seconds for which the Amazon Bedrock keeps information about the user's conversation with the inline collaborator agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout. </p>"""
    action_groups: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_action_groups.AgentActionGroups"
    ]
    """<p> List of action groups with each action group defining tasks the inline collaborator agent needs to carry out. </p>"""
    knowledge_bases: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_bases.KnowledgeBases"
    ]
    """<p> Knowledge base associated with the inline collaborator agent. </p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.GuardrailConfigurationWithArn"
    ]
    """<p> Details of the guardwrail associated with the inline collaborator. </p>"""
    prompt_override_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.prompt_override_configuration.PromptOverrideConfiguration"
    ]
    """<p> Contains configurations to override prompt templates in different parts of an inline collaborator sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>. </p>"""
    agent_collaboration: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_collaboration.AgentCollaboration"
    ]
    """<p> Defines how the inline supervisor agent handles information across multiple collaborator agents to coordinate a final response. </p>"""
    collaborator_configurations: NotRequired[
        "capo_bedrock_agent_runtime.types.collaborator_configurations.CollaboratorConfigurations"
    ]
    """<p> Settings of the collaborator agent. </p>"""
    agent_name: NotRequired["capo_bedrock_agent_runtime.types.name.Name"]
    """<p> Name of the inline collaborator agent which must be the same name as specified for <code>collaboratorName</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Collaborator) -> dict:
    out: dict = {}
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    out["foundationModel"] = value["foundation_model"]
    out["instruction"] = value["instruction"]
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "action_groups" in value:
        import capo_bedrock_agent_runtime.types.agent_action_groups

        out["actionGroups"] = (
            capo_bedrock_agent_runtime.types.agent_action_groups.serialize_json(
                value["action_groups"]
            )
        )
    if "knowledge_bases" in value:
        import capo_bedrock_agent_runtime.types.knowledge_bases

        out["knowledgeBases"] = (
            capo_bedrock_agent_runtime.types.knowledge_bases.serialize_json(
                value["knowledge_bases"]
            )
        )
    if "guardrail_configuration" in value:
        import capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn

        out["guardrailConfiguration"] = (
            capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "prompt_override_configuration" in value:
        import capo_bedrock_agent_runtime.types.prompt_override_configuration

        out["promptOverrideConfiguration"] = (
            capo_bedrock_agent_runtime.types.prompt_override_configuration.serialize_json(
                value["prompt_override_configuration"]
            )
        )
    if "agent_collaboration" in value:
        import capo_bedrock_agent_runtime.types.agent_collaboration

        out["agentCollaboration"] = (
            capo_bedrock_agent_runtime.types.agent_collaboration.serialize_json(
                value["agent_collaboration"]
            )
        )
    if "collaborator_configurations" in value:
        import capo_bedrock_agent_runtime.types.collaborator_configurations

        out["collaboratorConfigurations"] = (
            capo_bedrock_agent_runtime.types.collaborator_configurations.serialize_json(
                value["collaborator_configurations"]
            )
        )
    if "agent_name" in value:
        out["agentName"] = value["agent_name"]
    return out


def deserialize_json(data: dict) -> Collaborator:
    out: Collaborator = {}  # type: ignore[typeddict-item]
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("foundationModel") is not None:
        out["foundation_model"] = data["foundationModel"]
    else:
        raise DeserializationError("Collaborator.foundation_model required")
    if data.get("instruction") is not None:
        out["instruction"] = data["instruction"]
    else:
        raise DeserializationError("Collaborator.instruction required")
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if data.get("actionGroups") is not None:
        import capo_bedrock_agent_runtime.types.agent_action_groups

        out["action_groups"] = (
            capo_bedrock_agent_runtime.types.agent_action_groups.deserialize_json(
                data["actionGroups"]
            )
        )
    if data.get("knowledgeBases") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_bases

        out["knowledge_bases"] = (
            capo_bedrock_agent_runtime.types.knowledge_bases.deserialize_json(
                data["knowledgeBases"]
            )
        )
    if data.get("guardrailConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn

        out["guardrail_configuration"] = (
            capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if data.get("promptOverrideConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.prompt_override_configuration

        out["prompt_override_configuration"] = (
            capo_bedrock_agent_runtime.types.prompt_override_configuration.deserialize_json(
                data["promptOverrideConfiguration"]
            )
        )
    if data.get("agentCollaboration") is not None:
        import capo_bedrock_agent_runtime.types.agent_collaboration

        out["agent_collaboration"] = (
            capo_bedrock_agent_runtime.types.agent_collaboration.deserialize_json(
                data["agentCollaboration"]
            )
        )
    if data.get("collaboratorConfigurations") is not None:
        import capo_bedrock_agent_runtime.types.collaborator_configurations

        out["collaborator_configurations"] = (
            capo_bedrock_agent_runtime.types.collaborator_configurations.deserialize_json(
                data["collaboratorConfigurations"]
            )
        )
    if data.get("agentName") is not None:
        out["agent_name"] = data["agentName"]
    return out
