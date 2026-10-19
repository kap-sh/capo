"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailAutomatedReasoningPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_confidence_filter_threshold
    import capo_bedrock.types.automated_reasoning_policy_arn_list


class GuardrailAutomatedReasoningPolicyConfig(TypedDict, closed=True):
    policies: "capo_bedrock.types.automated_reasoning_policy_arn_list.AutomatedReasoningPolicyArnList"
    """<p>The list of Automated Reasoning policy ARNs to include in the guardrail configuration.</p>"""
    confidence_threshold: NotRequired[
        "capo_bedrock.types.automated_reasoning_confidence_filter_threshold.AutomatedReasoningConfidenceFilterThreshold"
    ]
    """<p>The confidence threshold for triggering guardrail actions based on Automated Reasoning policy violations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningPolicyConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_arn_list

    out["policies"] = (
        capo_bedrock.types.automated_reasoning_policy_arn_list.serialize_json(
            value["policies"]
        )
    )
    if "confidence_threshold" in value:
        out["confidenceThreshold"] = (
            "NaN"
            if value["confidence_threshold"] != value["confidence_threshold"]
            else "Infinity"
            if value["confidence_threshold"] == float("inf")
            else "-Infinity"
            if value["confidence_threshold"] == float("-inf")
            else value["confidence_threshold"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningPolicyConfig:
    out: GuardrailAutomatedReasoningPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("policies") is not None:
        import capo_bedrock.types.automated_reasoning_policy_arn_list

        out["policies"] = (
            capo_bedrock.types.automated_reasoning_policy_arn_list.deserialize_json(
                data["policies"]
            )
        )
    else:
        out["policies"] = []
    if data.get("confidenceThreshold") is not None:
        out["confidence_threshold"] = float(data["confidenceThreshold"])
    return out
