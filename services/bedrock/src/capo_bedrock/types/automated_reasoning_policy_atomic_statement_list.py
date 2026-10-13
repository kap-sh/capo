"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAtomicStatementList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement

AutomatedReasoningPolicyAtomicStatementList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_atomic_statement.AutomatedReasoningPolicyAtomicStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAtomicStatementList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_atomic_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAtomicStatementList:
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement

    out: AutomatedReasoningPolicyAtomicStatementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_atomic_statement.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAtomicStatementList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement

    return [
        capo_bedrock.types.automated_reasoning_policy_atomic_statement.redact_sensitive(
            item
        )
        for item in value
    ]
