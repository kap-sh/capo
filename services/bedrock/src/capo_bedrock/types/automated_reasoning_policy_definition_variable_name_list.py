"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionVariableNameList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name

AutomatedReasoningPolicyDefinitionVariableNameList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionVariableNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionVariableNameList:
    return [item for item in data if item is not None]


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionVariableNameList,
) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
