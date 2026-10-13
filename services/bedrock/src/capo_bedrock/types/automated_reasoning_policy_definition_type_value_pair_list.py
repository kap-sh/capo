"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValuePairList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair

AutomatedReasoningPolicyDefinitionTypeValuePairList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair.AutomatedReasoningPolicyDefinitionTypeValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValuePairList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeValuePairList:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair

    out: AutomatedReasoningPolicyDefinitionTypeValuePairList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionTypeValuePairList,
) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair

    return [
        capo_bedrock.types.automated_reasoning_policy_definition_type_value_pair.redact_sensitive(
            item
        )
        for item in value
    ]
