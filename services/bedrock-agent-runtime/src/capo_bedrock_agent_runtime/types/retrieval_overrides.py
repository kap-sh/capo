"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalOverrides``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_filter


class RetrievalOverrides(TypedDict, closed=True):
    filter: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_filter.RetrievalFilter"
    ]
    """<p>A filter to apply to the retrieval results.</p>"""
    max_number_of_results: NotRequired["int"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalOverrides) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.serialize_json(
                value["filter"]
            )
        )
    if "max_number_of_results" in value:
        out["maxNumberOfResults"] = value["max_number_of_results"]
    return out


def deserialize_json(data: dict) -> RetrievalOverrides:
    out: RetrievalOverrides = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("maxNumberOfResults") is not None:
        out["max_number_of_results"] = data["maxNumberOfResults"]
    return out


def redact_sensitive(value: RetrievalOverrides) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter" in value:
        out["filter"] = "*** Sensitive Data Redacted ***"
    return out
