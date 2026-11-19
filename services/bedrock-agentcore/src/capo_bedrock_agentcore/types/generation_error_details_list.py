"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationErrorDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_error_detail

GenerationErrorDetailsList: TypeAlias = list[
    "capo_bedrock_agentcore.types.generation_error_detail.GenerationErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationErrorDetailsList) -> list:
    import capo_bedrock_agentcore.types.generation_error_detail

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.generation_error_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GenerationErrorDetailsList:
    import capo_bedrock_agentcore.types.generation_error_detail

    out: GenerationErrorDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.generation_error_detail.deserialize_json(item)
        )
    return out
