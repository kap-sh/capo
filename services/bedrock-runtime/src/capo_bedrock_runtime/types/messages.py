"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Messages``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.message

Messages: TypeAlias = list["capo_bedrock_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import capo_bedrock_runtime.types.message

    out: list = []
    for item in value:
        out.append(capo_bedrock_runtime.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import capo_bedrock_runtime.types.message

    out: Messages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_runtime.types.message.deserialize_json(item))
    return out


def redact_sensitive(value: Messages) -> list[Any]:
    import capo_bedrock_runtime.types.message

    return [capo_bedrock_runtime.types.message.redact_sensitive(item) for item in value]
