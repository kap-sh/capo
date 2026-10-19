"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_policies_processed
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_units_processed
    import capo_bedrock_runtime.types.guardrail_content_policy_image_units_processed
    import capo_bedrock_runtime.types.guardrail_content_policy_units_processed
    import capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_units_processed
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_free_units_processed
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_units_processed
    import capo_bedrock_runtime.types.guardrail_topic_policy_units_processed
    import capo_bedrock_runtime.types.guardrail_word_policy_units_processed


class GuardrailUsage(TypedDict, closed=True):
    topic_policy_units: "capo_bedrock_runtime.types.guardrail_topic_policy_units_processed.GuardrailTopicPolicyUnitsProcessed"
    """<p>The topic policy units processed by the guardrail.</p>"""
    content_policy_units: "capo_bedrock_runtime.types.guardrail_content_policy_units_processed.GuardrailContentPolicyUnitsProcessed"
    """<p>The content policy units processed by the guardrail.</p>"""
    word_policy_units: "capo_bedrock_runtime.types.guardrail_word_policy_units_processed.GuardrailWordPolicyUnitsProcessed"
    """<p>The word policy units processed by the guardrail.</p>"""
    sensitive_information_policy_units: "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_units_processed.GuardrailSensitiveInformationPolicyUnitsProcessed"
    """<p>The sensitive information policy units processed by the guardrail.</p>"""
    sensitive_information_policy_free_units: "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_free_units_processed.GuardrailSensitiveInformationPolicyFreeUnitsProcessed"
    """<p>The sensitive information policy free units processed by the guardrail.</p>"""
    contextual_grounding_policy_units: "capo_bedrock_runtime.types.guardrail_contextual_grounding_policy_units_processed.GuardrailContextualGroundingPolicyUnitsProcessed"
    """<p>The contextual grounding policy units processed by the guardrail.</p>"""
    content_policy_image_units: NotRequired[
        "capo_bedrock_runtime.types.guardrail_content_policy_image_units_processed.GuardrailContentPolicyImageUnitsProcessed"
    ]
    """<p>The content policy image units processed by the guardrail.</p>"""
    automated_reasoning_policy_units: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_policy_units_processed.GuardrailAutomatedReasoningPolicyUnitsProcessed"
    ]
    """<p>The number of text units processed by the automated reasoning policy.</p>"""
    automated_reasoning_policies: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_policies_processed.GuardrailAutomatedReasoningPoliciesProcessed"
    ]
    """<p>The number of automated reasoning policies that were processed during the guardrail evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailUsage) -> dict:
    out: dict = {}
    out["topicPolicyUnits"] = value["topic_policy_units"]
    out["contentPolicyUnits"] = value["content_policy_units"]
    out["wordPolicyUnits"] = value["word_policy_units"]
    out["sensitiveInformationPolicyUnits"] = value["sensitive_information_policy_units"]
    out["sensitiveInformationPolicyFreeUnits"] = value[
        "sensitive_information_policy_free_units"
    ]
    out["contextualGroundingPolicyUnits"] = value["contextual_grounding_policy_units"]
    if "content_policy_image_units" in value:
        out["contentPolicyImageUnits"] = value["content_policy_image_units"]
    if "automated_reasoning_policy_units" in value:
        out["automatedReasoningPolicyUnits"] = value["automated_reasoning_policy_units"]
    if "automated_reasoning_policies" in value:
        out["automatedReasoningPolicies"] = value["automated_reasoning_policies"]
    return out


def deserialize_json(data: dict) -> GuardrailUsage:
    out: GuardrailUsage = {}  # type: ignore[typeddict-item]
    if data.get("topicPolicyUnits") is not None:
        out["topic_policy_units"] = data["topicPolicyUnits"]
    else:
        out["topic_policy_units"] = 0
    if data.get("contentPolicyUnits") is not None:
        out["content_policy_units"] = data["contentPolicyUnits"]
    else:
        out["content_policy_units"] = 0
    if data.get("wordPolicyUnits") is not None:
        out["word_policy_units"] = data["wordPolicyUnits"]
    else:
        out["word_policy_units"] = 0
    if data.get("sensitiveInformationPolicyUnits") is not None:
        out["sensitive_information_policy_units"] = data[
            "sensitiveInformationPolicyUnits"
        ]
    else:
        out["sensitive_information_policy_units"] = 0
    if data.get("sensitiveInformationPolicyFreeUnits") is not None:
        out["sensitive_information_policy_free_units"] = data[
            "sensitiveInformationPolicyFreeUnits"
        ]
    else:
        out["sensitive_information_policy_free_units"] = 0
    if data.get("contextualGroundingPolicyUnits") is not None:
        out["contextual_grounding_policy_units"] = data[
            "contextualGroundingPolicyUnits"
        ]
    else:
        out["contextual_grounding_policy_units"] = 0
    if data.get("contentPolicyImageUnits") is not None:
        out["content_policy_image_units"] = data["contentPolicyImageUnits"]
    if data.get("automatedReasoningPolicyUnits") is not None:
        out["automated_reasoning_policy_units"] = data["automatedReasoningPolicyUnits"]
    if data.get("automatedReasoningPolicies") is not None:
        out["automated_reasoning_policies"] = data["automatedReasoningPolicies"]
    return out
