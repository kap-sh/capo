"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rerank_document


class RerankResult(TypedDict, closed=True):
    index: "int"
    """<p>The original index of the document from the input sources array.</p>"""
    relevance_score: "float"
    """<p>The relevance score of the document.</p>"""
    document: NotRequired[
        "capo_bedrock_agent_runtime.types.rerank_document.RerankDocument"
    ]
    """<p>Contains information about the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankResult) -> dict:
    out: dict = {}
    out["index"] = value["index"]
    out["relevanceScore"] = (
        "NaN"
        if value["relevance_score"] != value["relevance_score"]
        else "Infinity"
        if value["relevance_score"] == float("inf")
        else "-Infinity"
        if value["relevance_score"] == float("-inf")
        else value["relevance_score"]
    )
    if "document" in value:
        import capo_bedrock_agent_runtime.types.rerank_document

        out["document"] = (
            capo_bedrock_agent_runtime.types.rerank_document.serialize_json(
                value["document"]
            )
        )
    return out


def deserialize_json(data: dict) -> RerankResult:
    out: RerankResult = {}  # type: ignore[typeddict-item]
    if data.get("index") is not None:
        out["index"] = data["index"]
    else:
        out["index"] = 0
    if data.get("relevanceScore") is not None:
        out["relevance_score"] = float(data["relevanceScore"])
    else:
        out["relevance_score"] = 0.0
    if data.get("document") is not None:
        import capo_bedrock_agent_runtime.types.rerank_document

        out["document"] = (
            capo_bedrock_agent_runtime.types.rerank_document.deserialize_json(
                data["document"]
            )
        )
    return out


def redact_sensitive(value: RerankResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document" in value:
        out["document"] = "*** Sensitive Data Redacted ***"
    return out
