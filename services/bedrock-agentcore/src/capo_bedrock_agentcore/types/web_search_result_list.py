"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#WebSearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.web_search_result

WebSearchResultList: TypeAlias = list[
    "capo_bedrock_agentcore.types.web_search_result.WebSearchResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: WebSearchResultList) -> list:
    import capo_bedrock_agentcore.types.web_search_result

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.web_search_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> WebSearchResultList:
    import capo_bedrock_agentcore.types.web_search_result

    out: WebSearchResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.web_search_result.deserialize_json(item)
        )
    return out
