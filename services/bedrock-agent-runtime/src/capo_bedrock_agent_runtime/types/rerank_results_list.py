"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankResultsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rerank_result

RerankResultsList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.rerank_result.RerankResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankResultsList) -> list:
    import capo_bedrock_agent_runtime.types.rerank_result

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.rerank_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> RerankResultsList:
    import capo_bedrock_agent_runtime.types.rerank_result

    out: RerankResultsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.rerank_result.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RerankResultsList) -> list[Any]:
    import capo_bedrock_agent_runtime.types.rerank_result

    return [
        capo_bedrock_agent_runtime.types.rerank_result.redact_sensitive(item)
        for item in value
    ]
