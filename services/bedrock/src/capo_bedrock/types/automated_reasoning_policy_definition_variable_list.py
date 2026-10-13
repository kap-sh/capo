"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionVariableList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

AutomatedReasoningPolicyDefinitionVariableList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionVariableList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionVariableList:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

    out: AutomatedReasoningPolicyDefinitionVariableList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionVariableList,
) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

    return [
        capo_bedrock.types.automated_reasoning_policy_definition_variable.redact_sensitive(
            item
        )
        for item in value
    ]
