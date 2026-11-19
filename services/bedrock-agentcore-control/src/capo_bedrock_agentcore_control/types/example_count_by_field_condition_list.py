"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleCountByFieldConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_count_by_field_condition

ExampleCountByFieldConditionList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.example_count_by_field_condition.ExampleCountByFieldCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleCountByFieldConditionList) -> list:
    import capo_bedrock_agentcore_control.types.example_count_by_field_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.example_count_by_field_condition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExampleCountByFieldConditionList:
    import capo_bedrock_agentcore_control.types.example_count_by_field_condition

    out: ExampleCountByFieldConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.example_count_by_field_condition.deserialize_json(
                item
            )
        )
    return out
