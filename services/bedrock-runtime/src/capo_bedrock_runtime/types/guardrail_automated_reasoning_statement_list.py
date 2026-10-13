"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningStatementList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement

GuardrailAutomatedReasoningStatementList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement.GuardrailAutomatedReasoningStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningStatementList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningStatementList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement

    out: GuardrailAutomatedReasoningStatementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GuardrailAutomatedReasoningStatementList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_statement.redact_sensitive(
            item
        )
        for item in value
    ]
