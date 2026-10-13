"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningPolicyAssessment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list


class GuardrailAutomatedReasoningPolicyAssessment(TypedDict, closed=True):
    findings: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.GuardrailAutomatedReasoningFindingList"
    ]
    """<p>List of logical validation results produced by evaluating the input content against automated reasoning policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningPolicyAssessment) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list

        out["findings"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningPolicyAssessment:
    out: GuardrailAutomatedReasoningPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list

        out["findings"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.deserialize_json(
                data["findings"]
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningPolicyAssessment,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "findings" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list

        out["findings"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.redact_sensitive(
                value["findings"]
            )
        )
    return out
