"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_filter

RetrievalFilterList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.retrieval_filter.RetrievalFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterList) -> list:
    import capo_bedrock_agent_runtime.types.retrieval_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.retrieval_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievalFilterList:
    import capo_bedrock_agent_runtime.types.retrieval_filter

    out: RetrievalFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.retrieval_filter.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RetrievalFilterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
