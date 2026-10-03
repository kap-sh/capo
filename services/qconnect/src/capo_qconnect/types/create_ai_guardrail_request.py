"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_blocked_messaging
    import capo_qconnect.types.ai_guardrail_content_policy_config
    import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config
    import capo_qconnect.types.ai_guardrail_description
    import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config
    import capo_qconnect.types.ai_guardrail_topic_policy_config
    import capo_qconnect.types.ai_guardrail_word_policy_config
    import capo_qconnect.types.client_token
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.visibility_status


class CreateAIGuardrailRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Guardrail.</p>"""
    blocked_input_messaging: (
        "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    )
    """<p>The message to return when the AI Guardrail blocks a prompt.</p>"""
    blocked_outputs_messaging: (
        "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    )
    """<p>The message to return when the AI Guardrail blocks a model response.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Guardrail.</p>"""
    description: NotRequired[
        "capo_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
    ]
    """<p>A description of the AI Guardrail.</p>"""
    topic_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_topic_policy_config.AIGuardrailTopicPolicyConfig"
    ]
    """<p>The topic policies to configure for the AI Guardrail.</p>"""
    content_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_content_policy_config.AIGuardrailContentPolicyConfig"
    ]
    """<p>The content filter policies to configure for the AI Guardrail.</p>"""
    word_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_word_policy_config.AIGuardrailWordPolicyConfig"
    ]
    """<p>The word policy you configure for the AI Guardrail.</p>"""
    sensitive_information_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.AIGuardrailSensitiveInformationPolicyConfig"
    ]
    """<p>The sensitive information policy to configure for the AI Guardrail.</p>"""
    contextual_grounding_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.AIGuardrailContextualGroundingPolicyConfig"
    ]
    """<p>The contextual grounding policy configuration used to create an AI Guardrail.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
    out["visibilityStatus"] = value["visibility_status"]
    if "description" in value:
        out["description"] = value["description"]
    if "topic_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_topic_policy_config

        out["topicPolicyConfig"] = (
            capo_qconnect.types.ai_guardrail_topic_policy_config.serialize_json(
                value["topic_policy_config"]
            )
        )
    if "content_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_content_policy_config

        out["contentPolicyConfig"] = (
            capo_qconnect.types.ai_guardrail_content_policy_config.serialize_json(
                value["content_policy_config"]
            )
        )
    if "word_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_word_policy_config

        out["wordPolicyConfig"] = (
            capo_qconnect.types.ai_guardrail_word_policy_config.serialize_json(
                value["word_policy_config"]
            )
        )
    if "sensitive_information_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config

        out["sensitiveInformationPolicyConfig"] = (
            capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.serialize_json(
                value["sensitive_information_policy_config"]
            )
        )
    if "contextual_grounding_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config

        out["contextualGroundingPolicyConfig"] = (
            capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.serialize_json(
                value["contextual_grounding_policy_config"]
            )
        )
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailRequest:
    out: CreateAIGuardrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAIGuardrailRequest.name required")
    if data.get("blockedInputMessaging") is not None:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.blocked_input_messaging required"
        )
    if data.get("blockedOutputsMessaging") is not None:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.blocked_outputs_messaging required"
        )
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.visibility_status required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("topicPolicyConfig") is not None:
        import capo_qconnect.types.ai_guardrail_topic_policy_config

        out["topic_policy_config"] = (
            capo_qconnect.types.ai_guardrail_topic_policy_config.deserialize_json(
                data["topicPolicyConfig"]
            )
        )
    if data.get("contentPolicyConfig") is not None:
        import capo_qconnect.types.ai_guardrail_content_policy_config

        out["content_policy_config"] = (
            capo_qconnect.types.ai_guardrail_content_policy_config.deserialize_json(
                data["contentPolicyConfig"]
            )
        )
    if data.get("wordPolicyConfig") is not None:
        import capo_qconnect.types.ai_guardrail_word_policy_config

        out["word_policy_config"] = (
            capo_qconnect.types.ai_guardrail_word_policy_config.deserialize_json(
                data["wordPolicyConfig"]
            )
        )
    if data.get("sensitiveInformationPolicyConfig") is not None:
        import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config

        out["sensitive_information_policy_config"] = (
            capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.deserialize_json(
                data["sensitiveInformationPolicyConfig"]
            )
        )
    if data.get("contextualGroundingPolicyConfig") is not None:
        import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config

        out["contextual_grounding_policy_config"] = (
            capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.deserialize_json(
                data["contextualGroundingPolicyConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
