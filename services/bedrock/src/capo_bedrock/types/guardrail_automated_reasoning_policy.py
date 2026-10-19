"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailAutomatedReasoningPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_confidence_filter_threshold
    import capo_bedrock.types.automated_reasoning_policy_arn_list


class GuardrailAutomatedReasoningPolicy(TypedDict, closed=True):
    policies: "capo_bedrock.types.automated_reasoning_policy_arn_list.AutomatedReasoningPolicyArnList"
    """<p>The list of Automated Reasoning policy ARNs that should be applied as part of this guardrail configuration.</p>"""
    confidence_threshold: NotRequired[
        "capo_bedrock.types.automated_reasoning_confidence_filter_threshold.AutomatedReasoningConfidenceFilterThreshold"
    ]
    """<p>The minimum confidence level required for Automated Reasoning policy violations to trigger guardrail actions. Values range from 0.0 to 1.0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningPolicy) -> dict:
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


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningPolicy:
    out: GuardrailAutomatedReasoningPolicy = {}  # type: ignore[typeddict-item]
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
