"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citations_config
    import capo_bedrock_runtime.types.search_result_content_blocks


class SearchResultBlock(TypedDict, closed=True):
    source: "str"
    """<p>The source URL or identifier for the content.</p>"""
    title: "str"
    """<p>A descriptive title for the search result.</p>"""
    content: "capo_bedrock_runtime.types.search_result_content_blocks.SearchResultContentBlocks"
    """<p>An array of search result content block.</p>"""
    citations: NotRequired[
        "capo_bedrock_runtime.types.citations_config.CitationsConfig"
    ]
    """<p>Configuration setting for citations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultBlock) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["title"] = value["title"]
    import capo_bedrock_runtime.types.search_result_content_blocks

    out["content"] = (
        capo_bedrock_runtime.types.search_result_content_blocks.serialize_json(
            value["content"]
        )
    )
    if "citations" in value:
        import capo_bedrock_runtime.types.citations_config

        out["citations"] = capo_bedrock_runtime.types.citations_config.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> SearchResultBlock:
    out: SearchResultBlock = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.search_result_content_blocks

        out["content"] = (
            capo_bedrock_runtime.types.search_result_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = []
    if data.get("citations") is not None:
        import capo_bedrock_runtime.types.citations_config

        out["citations"] = capo_bedrock_runtime.types.citations_config.deserialize_json(
            data["citations"]
        )
    return out
