"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationAttributeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_attribute_filter

GenerationAttributeFilterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.generation_attribute_filter.GenerationAttributeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationAttributeFilterList) -> list:
    import capo_bedrock_agentcore.types.generation_attribute_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.generation_attribute_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GenerationAttributeFilterList:
    import capo_bedrock_agentcore.types.generation_attribute_filter

    out: GenerationAttributeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.generation_attribute_filter.deserialize_json(
                item
            )
        )
    return out
