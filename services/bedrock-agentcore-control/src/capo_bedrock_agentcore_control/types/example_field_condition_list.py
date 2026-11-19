"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleFieldConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_field_condition

ExampleFieldConditionList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.example_field_condition.ExampleFieldCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleFieldConditionList) -> list:
    import capo_bedrock_agentcore_control.types.example_field_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.example_field_condition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExampleFieldConditionList:
    import capo_bedrock_agentcore_control.types.example_field_condition

    out: ExampleFieldConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.example_field_condition.deserialize_json(
                item
            )
        )
    return out
