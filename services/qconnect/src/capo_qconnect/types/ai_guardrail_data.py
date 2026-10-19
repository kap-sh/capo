"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.ai_guardrail_blocked_messaging
    import capo_qconnect.types.ai_guardrail_content_policy_config
    import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config
    import capo_qconnect.types.ai_guardrail_description
    import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config
    import capo_qconnect.types.ai_guardrail_topic_policy_config
    import capo_qconnect.types.ai_guardrail_word_policy_config
    import capo_qconnect.types.arn
    import capo_qconnect.types.name
    import capo_qconnect.types.status
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid
    import capo_qconnect.types.visibility_status


class AIGuardrailData(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_guardrail_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI Guardrail.</p>"""
    ai_guardrail_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect AI Guardrail.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Guardrail.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Guardrail.</p>"""
    blocked_input_messaging: (
        "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    )
    """<p>The message to return when the AI Guardrail blocks a prompt.</p>"""
    blocked_outputs_messaging: (
        "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    )
    """<p>The message to return when the AI Guardrail blocks a model response.</p>"""
    description: NotRequired[
        "capo_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
    ]
    """<p>A description of the AI Guardrail.</p>"""
    topic_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_topic_policy_config.AIGuardrailTopicPolicyConfig"
    ]
    """<p>Contains details about topics that the AI Guardrail should identify and deny.</p>"""
    content_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_content_policy_config.AIGuardrailContentPolicyConfig"
    ]
    """<p>Contains details about how to handle harmful content.</p>"""
    word_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_word_policy_config.AIGuardrailWordPolicyConfig"
    ]
    """<p>Contains details about the word policy to configured for the AI Guardrail.</p>"""
    sensitive_information_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.AIGuardrailSensitiveInformationPolicyConfig"
    ]
    """<p>Contains details about PII entities and regular expressions to configure for the AI Guardrail.</p>"""
    contextual_grounding_policy_config: NotRequired[
        "capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.AIGuardrailContextualGroundingPolicyConfig"
    ]
    """<p>The policy configuration details for the AI Guardrail's contextual grounding policy.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    status: NotRequired["capo_qconnect.types.status.Status"]
    """<p>The status of the AI Guardrail.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Guardrail was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiGuardrailArn"] = value["ai_guardrail_arn"]
    out["aiGuardrailId"] = value["ai_guardrail_id"]
    out["name"] = value["name"]
    out["visibilityStatus"] = value["visibility_status"]
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
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
    if "status" in value:
        out["status"] = value["status"]
    if "modified_time" in value:
        import capo_qconnect.types._prelude.timestamp

        out["modifiedTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    return out


def deserialize_json(data: dict) -> AIGuardrailData:
    out: AIGuardrailData = {}  # type: ignore[typeddict-item]
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        out["assistant_id"] = ""
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        out["assistant_arn"] = ""
    if data.get("aiGuardrailArn") is not None:
        out["ai_guardrail_arn"] = data["aiGuardrailArn"]
    else:
        out["ai_guardrail_arn"] = ""
    if data.get("aiGuardrailId") is not None:
        out["ai_guardrail_id"] = data["aiGuardrailId"]
    else:
        out["ai_guardrail_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        out["visibility_status"] = ""
    if data.get("blockedInputMessaging") is not None:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        out["blocked_input_messaging"] = ""
    if data.get("blockedOutputsMessaging") is not None:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        out["blocked_outputs_messaging"] = ""
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("modifiedTime") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["modified_time"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["modifiedTime"]
        )
    return out


def redact_sensitive(value: AIGuardrailData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blocked_input_messaging" in value:
        out["blocked_input_messaging"] = "*** Sensitive Data Redacted ***"
    if "blocked_outputs_messaging" in value:
        out["blocked_outputs_messaging"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "topic_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_topic_policy_config

        out["topic_policy_config"] = (
            capo_qconnect.types.ai_guardrail_topic_policy_config.redact_sensitive(
                value["topic_policy_config"]
            )
        )
    if "content_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_content_policy_config

        out["content_policy_config"] = (
            capo_qconnect.types.ai_guardrail_content_policy_config.redact_sensitive(
                value["content_policy_config"]
            )
        )
    if "word_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_word_policy_config

        out["word_policy_config"] = (
            capo_qconnect.types.ai_guardrail_word_policy_config.redact_sensitive(
                value["word_policy_config"]
            )
        )
    if "sensitive_information_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config

        out["sensitive_information_policy_config"] = (
            capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.redact_sensitive(
                value["sensitive_information_policy_config"]
            )
        )
    if "contextual_grounding_policy_config" in value:
        import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config

        out["contextual_grounding_policy_config"] = (
            capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.redact_sensitive(
                value["contextual_grounding_policy_config"]
            )
        )
    return out
