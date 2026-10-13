"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeNameList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name

AutomatedReasoningPolicyDefinitionTypeNameList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeNameList:
    return [item for item in data if item is not None]


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionTypeNameList,
) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
