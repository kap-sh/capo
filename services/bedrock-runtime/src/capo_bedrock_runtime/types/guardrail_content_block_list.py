"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentBlockList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_content_block

GuardrailContentBlockList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_content_block.GuardrailContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentBlockList) -> list:
    import capo_bedrock_runtime.types.guardrail_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailContentBlockList:
    import capo_bedrock_runtime.types.guardrail_content_block

    out: GuardrailContentBlockList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_content_block.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailContentBlockList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_content_block

    return [
        capo_bedrock_runtime.types.guardrail_content_block.redact_sensitive(item)
        for item in value
    ]
