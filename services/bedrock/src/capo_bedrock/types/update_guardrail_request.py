"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_automated_reasoning_policy_config
    import capo_bedrock.types.guardrail_blocked_messaging
    import capo_bedrock.types.guardrail_content_policy_config
    import capo_bedrock.types.guardrail_contextual_grounding_policy_config
    import capo_bedrock.types.guardrail_cross_region_config
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_identifier
    import capo_bedrock.types.guardrail_name
    import capo_bedrock.types.guardrail_sensitive_information_policy_config
    import capo_bedrock.types.guardrail_topic_policy_config
    import capo_bedrock.types.guardrail_word_policy_config
    import capo_bedrock.types.kms_key_id


class UpdateGuardrailRequest(TypedDict, closed=True):
    guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    """<p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>"""
    name: "capo_bedrock.types.guardrail_name.GuardrailName"
    """<p>A name for the guardrail.</p>"""
    description: NotRequired[
        "capo_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>A description of the guardrail.</p>"""
    topic_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
    ]
    """<p>The topic policy to configure for the guardrail.</p>"""
    content_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
    ]
    """<p>The content policy to configure for the guardrail.</p>"""
    word_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
    ]
    """<p>The word policy to configure for the guardrail.</p>"""
    sensitive_information_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
    ]
    """<p>The sensitive information policy to configure for the guardrail.</p>"""
    contextual_grounding_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
    ]
    """<p>The contextual grounding policy configuration used to update a guardrail.</p>"""
    automated_reasoning_policy_config: NotRequired[
        "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
    ]
    """<p>Updated configuration for Automated Reasoning policies associated with the guardrail.</p>"""
    cross_region_config: NotRequired[
        "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
    ]
    """<p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>"""
    blocked_input_messaging: (
        "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message to return when the guardrail blocks a prompt.</p>"""
    blocked_outputs_messaging: (
        "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message to return when the guardrail blocks a model response.</p>"""
    kms_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key with which to encrypt the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGuardrailRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "topic_policy_config" in value:
        import capo_bedrock.types.guardrail_topic_policy_config

        out["topicPolicyConfig"] = (
            capo_bedrock.types.guardrail_topic_policy_config.serialize_json(
                value["topic_policy_config"]
            )
        )
    if "content_policy_config" in value:
        import capo_bedrock.types.guardrail_content_policy_config

        out["contentPolicyConfig"] = (
            capo_bedrock.types.guardrail_content_policy_config.serialize_json(
                value["content_policy_config"]
            )
        )
    if "word_policy_config" in value:
        import capo_bedrock.types.guardrail_word_policy_config

        out["wordPolicyConfig"] = (
            capo_bedrock.types.guardrail_word_policy_config.serialize_json(
                value["word_policy_config"]
            )
        )
    if "sensitive_information_policy_config" in value:
        import capo_bedrock.types.guardrail_sensitive_information_policy_config

        out["sensitiveInformationPolicyConfig"] = (
            capo_bedrock.types.guardrail_sensitive_information_policy_config.serialize_json(
                value["sensitive_information_policy_config"]
            )
        )
    if "contextual_grounding_policy_config" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_policy_config

        out["contextualGroundingPolicyConfig"] = (
            capo_bedrock.types.guardrail_contextual_grounding_policy_config.serialize_json(
                value["contextual_grounding_policy_config"]
            )
        )
    if "automated_reasoning_policy_config" in value:
        import capo_bedrock.types.guardrail_automated_reasoning_policy_config

        out["automatedReasoningPolicyConfig"] = (
            capo_bedrock.types.guardrail_automated_reasoning_policy_config.serialize_json(
                value["automated_reasoning_policy_config"]
            )
        )
    if "cross_region_config" in value:
        import capo_bedrock.types.guardrail_cross_region_config

        out["crossRegionConfig"] = (
            capo_bedrock.types.guardrail_cross_region_config.serialize_json(
                value["cross_region_config"]
            )
        )
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> UpdateGuardrailRequest:
    out: UpdateGuardrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGuardrailRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("topicPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_topic_policy_config

        out["topic_policy_config"] = (
            capo_bedrock.types.guardrail_topic_policy_config.deserialize_json(
                data["topicPolicyConfig"]
            )
        )
    if data.get("contentPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_content_policy_config

        out["content_policy_config"] = (
            capo_bedrock.types.guardrail_content_policy_config.deserialize_json(
                data["contentPolicyConfig"]
            )
        )
    if data.get("wordPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_word_policy_config

        out["word_policy_config"] = (
            capo_bedrock.types.guardrail_word_policy_config.deserialize_json(
                data["wordPolicyConfig"]
            )
        )
    if data.get("sensitiveInformationPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_sensitive_information_policy_config

        out["sensitive_information_policy_config"] = (
            capo_bedrock.types.guardrail_sensitive_information_policy_config.deserialize_json(
                data["sensitiveInformationPolicyConfig"]
            )
        )
    if data.get("contextualGroundingPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_policy_config

        out["contextual_grounding_policy_config"] = (
            capo_bedrock.types.guardrail_contextual_grounding_policy_config.deserialize_json(
                data["contextualGroundingPolicyConfig"]
            )
        )
    if data.get("automatedReasoningPolicyConfig") is not None:
        import capo_bedrock.types.guardrail_automated_reasoning_policy_config

        out["automated_reasoning_policy_config"] = (
            capo_bedrock.types.guardrail_automated_reasoning_policy_config.deserialize_json(
                data["automatedReasoningPolicyConfig"]
            )
        )
    if data.get("crossRegionConfig") is not None:
        import capo_bedrock.types.guardrail_cross_region_config

        out["cross_region_config"] = (
            capo_bedrock.types.guardrail_cross_region_config.deserialize_json(
                data["crossRegionConfig"]
            )
        )
    if data.get("blockedInputMessaging") is not None:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        raise DeserializationError(
            "UpdateGuardrailRequest.blocked_input_messaging required"
        )
    if data.get("blockedOutputsMessaging") is not None:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        raise DeserializationError(
            "UpdateGuardrailRequest.blocked_outputs_messaging required"
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
