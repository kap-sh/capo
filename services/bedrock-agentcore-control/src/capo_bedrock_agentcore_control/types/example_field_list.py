"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_field

ExampleFieldList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.example_field.ExampleField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleFieldList) -> list:
    import capo_bedrock_agentcore_control.types.example_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.example_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExampleFieldList:
    import capo_bedrock_agentcore_control.types.example_field

    out: ExampleFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.example_field.deserialize_json(item)
        )
    return out
