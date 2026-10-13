"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type

AutomatedReasoningPolicyDefinitionTypeList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_definition_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeList:
    import capo_bedrock.types.automated_reasoning_policy_definition_type

    out: AutomatedReasoningPolicyDefinitionTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyDefinitionTypeList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_definition_type

    return [
        capo_bedrock.types.automated_reasoning_policy_definition_type.redact_sensitive(
            item
        )
        for item in value
    ]
