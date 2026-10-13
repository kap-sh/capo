"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningLogicStatementList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_logic_statement

AutomatedReasoningLogicStatementList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_logic_statement.AutomatedReasoningLogicStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningLogicStatementList) -> list:
    import capo_bedrock.types.automated_reasoning_logic_statement

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_logic_statement.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningLogicStatementList:
    import capo_bedrock.types.automated_reasoning_logic_statement

    out: AutomatedReasoningLogicStatementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_logic_statement.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningLogicStatementList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_logic_statement

    return [
        capo_bedrock.types.automated_reasoning_logic_statement.redact_sensitive(item)
        for item in value
    ]
