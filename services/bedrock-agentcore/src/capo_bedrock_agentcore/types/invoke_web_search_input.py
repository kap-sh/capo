"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeWebSearchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.web_search_filters
    import capo_bedrock_agentcore.types.web_search_id


class InvokeWebSearchInput(TypedDict, closed=True):
    web_search_id: "capo_bedrock_agentcore.types.web_search_id.WebSearchId"
    """<p>The identifier of the web search tool to invoke. The Amazon Web Services-managed web search tool is <code>web-search.v1</code>.</p>"""
    search_query: "str"
    """<p>The text to search for.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return. Defaults to 25.</p>"""
    filters: NotRequired[
        "capo_bedrock_agentcore.types.web_search_filters.WebSearchFilters"
    ]
    """<p>The filters to apply to the search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWebSearchInput) -> dict:
    out: dict = {}
    out["searchQuery"] = value["search_query"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_bedrock_agentcore.types.web_search_filters

        out["filters"] = capo_bedrock_agentcore.types.web_search_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> InvokeWebSearchInput:
    out: InvokeWebSearchInput = {}  # type: ignore[typeddict-item]
    if data.get("searchQuery") is not None:
        out["search_query"] = data["searchQuery"]
    else:
        out["search_query"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_bedrock_agentcore.types.web_search_filters

        out["filters"] = (
            capo_bedrock_agentcore.types.web_search_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
