"""Generated from Smithy shape ``com.amazonaws.bedrock#RagConfigs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.rag_config

RagConfigs: TypeAlias = list["capo_bedrock.types.rag_config.RAGConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: RagConfigs) -> list:
    import capo_bedrock.types.rag_config

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.rag_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> RagConfigs:
    import capo_bedrock.types.rag_config

    out: RagConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.rag_config.deserialize_json(item))
    return out


def redact_sensitive(value: RagConfigs) -> list[Any]:
    import capo_bedrock.types.rag_config

    return [capo_bedrock.types.rag_config.redact_sensitive(item) for item in value]
