"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.applied_guardrail_details
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment
    import capo_bedrock_runtime.types.guardrail_content_policy_assessment
    import capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment
    import capo_bedrock_runtime.types.guardrail_invocation_metrics
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment
    import capo_bedrock_runtime.types.guardrail_topic_policy_assessment
    import capo_bedrock_runtime.types.guardrail_word_policy_assessment


class GuardrailAssessment(TypedDict, closed=True):
    topic_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_topic_policy_assessment.GuardrailTopicPolicyAssessment"
    ]
    """<p>The topic policy.</p>"""
    content_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_content_policy_assessment.GuardrailContentPolicyAssessment"
    ]
    """<p>The content policy.</p>"""
    word_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_word_policy_assessment.GuardrailWordPolicyAssessment"
    ]
    """<p>The word policy.</p>"""
    sensitive_information_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.GuardrailSensitiveInformationPolicyAssessment"
    ]
    """<p>The sensitive information policy.</p>"""
    contextual_grounding_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.GuardrailContextualGroundingPolicyAssessment"
    ]
    """<p>The contextual grounding policy used for the guardrail assessment.</p>"""
    automated_reasoning_policy: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.GuardrailAutomatedReasoningPolicyAssessment"
    ]
    """<p>The automated reasoning policy assessment results, including logical validation findings for the input content.</p>"""
    invocation_metrics: NotRequired[
        "capo_bedrock_runtime.types.guardrail_invocation_metrics.GuardrailInvocationMetrics"
    ]
    """<p>The invocation metrics for the guardrail assessment.</p>"""
    applied_guardrail_details: NotRequired[
        "capo_bedrock_runtime.types.applied_guardrail_details.AppliedGuardrailDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAssessment) -> dict:
    out: dict = {}
    if "topic_policy" in value:
        import capo_bedrock_runtime.types.guardrail_topic_policy_assessment

        out["topicPolicy"] = (
            capo_bedrock_runtime.types.guardrail_topic_policy_assessment.serialize_json(
                value["topic_policy"]
            )
        )
    if "content_policy" in value:
        import capo_bedrock_runtime.types.guardrail_content_policy_assessment

        out["contentPolicy"] = (
            capo_bedrock_runtime.types.guardrail_content_policy_assessment.serialize_json(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import capo_bedrock_runtime.types.guardrail_word_policy_assessment

        out["wordPolicy"] = (
            capo_bedrock_runtime.types.guardrail_word_policy_assessment.serialize_json(
                value["word_policy"]
            )
        )
    if "sensitive_information_policy" in value:
        import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitiveInformationPolicy"] = (
            capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.serialize_json(
                value["sensitive_information_policy"]
            )
        )
    if "contextual_grounding_policy" in value:
        import capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment

        out["contextualGroundingPolicy"] = (
            capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.serialize_json(
                value["contextual_grounding_policy"]
            )
        )
    if "automated_reasoning_policy" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment

        out["automatedReasoningPolicy"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.serialize_json(
                value["automated_reasoning_policy"]
            )
        )
    if "invocation_metrics" in value:
        import capo_bedrock_runtime.types.guardrail_invocation_metrics

        out["invocationMetrics"] = (
            capo_bedrock_runtime.types.guardrail_invocation_metrics.serialize_json(
                value["invocation_metrics"]
            )
        )
    if "applied_guardrail_details" in value:
        import capo_bedrock_runtime.types.applied_guardrail_details

        out["appliedGuardrailDetails"] = (
            capo_bedrock_runtime.types.applied_guardrail_details.serialize_json(
                value["applied_guardrail_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessment:
    out: GuardrailAssessment = {}  # type: ignore[typeddict-item]
    if data.get("topicPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_topic_policy_assessment

        out["topic_policy"] = (
            capo_bedrock_runtime.types.guardrail_topic_policy_assessment.deserialize_json(
                data["topicPolicy"]
            )
        )
    if data.get("contentPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_content_policy_assessment

        out["content_policy"] = (
            capo_bedrock_runtime.types.guardrail_content_policy_assessment.deserialize_json(
                data["contentPolicy"]
            )
        )
    if data.get("wordPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_word_policy_assessment

        out["word_policy"] = (
            capo_bedrock_runtime.types.guardrail_word_policy_assessment.deserialize_json(
                data["wordPolicy"]
            )
        )
    if data.get("sensitiveInformationPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitive_information_policy"] = (
            capo_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.deserialize_json(
                data["sensitiveInformationPolicy"]
            )
        )
    if data.get("contextualGroundingPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment

        out["contextual_grounding_policy"] = (
            capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.deserialize_json(
                data["contextualGroundingPolicy"]
            )
        )
    if data.get("automatedReasoningPolicy") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment

        out["automated_reasoning_policy"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.deserialize_json(
                data["automatedReasoningPolicy"]
            )
        )
    if data.get("invocationMetrics") is not None:
        import capo_bedrock_runtime.types.guardrail_invocation_metrics

        out["invocation_metrics"] = (
            capo_bedrock_runtime.types.guardrail_invocation_metrics.deserialize_json(
                data["invocationMetrics"]
            )
        )
    if data.get("appliedGuardrailDetails") is not None:
        import capo_bedrock_runtime.types.applied_guardrail_details

        out["applied_guardrail_details"] = (
            capo_bedrock_runtime.types.applied_guardrail_details.deserialize_json(
                data["appliedGuardrailDetails"]
            )
        )
    return out


def redact_sensitive(value: GuardrailAssessment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "automated_reasoning_policy" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment

        out["automated_reasoning_policy"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.redact_sensitive(
                value["automated_reasoning_policy"]
            )
        )
    return out
