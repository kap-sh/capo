"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class _CitationSourceContent_text(TypedDict, closed=True):
    text: "str"


CitationSourceContent: TypeAlias = _CitationSourceContent_text | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CitationSourceContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CitationSourceContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CitationSourceContent: no variant present")


def deserialize_json(data: dict) -> CitationSourceContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CitationSourceContent: no recognized variant key")
