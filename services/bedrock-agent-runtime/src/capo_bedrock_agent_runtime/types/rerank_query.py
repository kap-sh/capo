"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rerank_query_content_type
    import capo_bedrock_agent_runtime.types.rerank_text_document


class RerankQuery(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.rerank_query_content_type.RerankQueryContentType"
    """<p>The type of the query.</p>"""
    text_query: (
        "capo_bedrock_agent_runtime.types.rerank_text_document.RerankTextDocument"
    )
    """<p>Contains information about a text query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankQuery) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.rerank_query_content_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.rerank_query_content_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_agent_runtime.types.rerank_text_document

    out["textQuery"] = (
        capo_bedrock_agent_runtime.types.rerank_text_document.serialize_json(
            value["text_query"]
        )
    )
    return out


def deserialize_json(data: dict) -> RerankQuery:
    out: RerankQuery = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.rerank_query_content_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.rerank_query_content_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.rerank_query_content_type.RerankQueryContentType",
            "",
        )
    if data.get("textQuery") is not None:
        import capo_bedrock_agent_runtime.types.rerank_text_document

        out["text_query"] = (
            capo_bedrock_agent_runtime.types.rerank_text_document.deserialize_json(
                data["textQuery"]
            )
        )
    else:
        raise DeserializationError("RerankQuery.text_query required")
    return out
