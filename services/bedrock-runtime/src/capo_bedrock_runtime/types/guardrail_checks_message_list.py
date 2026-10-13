"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksMessageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_message

GuardrailChecksMessageList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_message.GuardrailChecksMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksMessageList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_message

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_message.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksMessageList:
    import capo_bedrock_runtime.types.guardrail_checks_message

    out: GuardrailChecksMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_message.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailChecksMessageList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_checks_message

    return [
        capo_bedrock_runtime.types.guardrail_checks_message.redact_sensitive(item)
        for item in value
    ]
