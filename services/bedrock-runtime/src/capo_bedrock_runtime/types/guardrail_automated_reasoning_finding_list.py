"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningFindingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding

GuardrailAutomatedReasoningFindingList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_finding.GuardrailAutomatedReasoningFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningFindingList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningFindingList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding

    out: GuardrailAutomatedReasoningFindingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_finding.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GuardrailAutomatedReasoningFindingList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_finding

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_finding.redact_sensitive(
            item
        )
        for item in value
    ]
