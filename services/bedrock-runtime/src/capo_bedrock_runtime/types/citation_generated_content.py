"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationGeneratedContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class _CitationGeneratedContent_text(TypedDict, closed=True):
    text: "str"


CitationGeneratedContent: TypeAlias = (
    _CitationGeneratedContent_text | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CitationGeneratedContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CitationGeneratedContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CitationGeneratedContent: no variant present")


def deserialize_json(data: dict) -> CitationGeneratedContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CitationGeneratedContent: no recognized variant key"
        )
