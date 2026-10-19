"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_search_type
    import capo_qconnect.types.knowledge_source
    import capo_qconnect.types.retrieval_filter_configuration


class RetrievalConfiguration(TypedDict, closed=True):
    knowledge_source: "capo_qconnect.types.knowledge_source.KnowledgeSource"
    """<p>The knowledge source configuration for content retrieval.</p>"""
    filter: NotRequired[
        "capo_qconnect.types.retrieval_filter_configuration.RetrievalFilterConfiguration"
    ]
    """<p>The filter configuration for content retrieval.</p>"""
    number_of_results: NotRequired["int"]
    """<p>The number of results to retrieve.</p>"""
    override_knowledge_base_search_type: NotRequired[
        "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
    ]
    """<p>Override setting for the knowledge base search type during retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalConfiguration) -> dict:
    out: dict = {}
    import capo_qconnect.types.knowledge_source

    out["knowledgeSource"] = capo_qconnect.types.knowledge_source.serialize_json(
        value["knowledge_source"]
    )
    if "filter" in value:
        import capo_qconnect.types.retrieval_filter_configuration

        out["filter"] = (
            capo_qconnect.types.retrieval_filter_configuration.serialize_json(
                value["filter"]
            )
        )
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    if "override_knowledge_base_search_type" in value:
        out["overrideKnowledgeBaseSearchType"] = value[
            "override_knowledge_base_search_type"
        ]
    return out


def deserialize_json(data: dict) -> RetrievalConfiguration:
    out: RetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeSource") is not None:
        import capo_qconnect.types.knowledge_source

        out["knowledge_source"] = capo_qconnect.types.knowledge_source.deserialize_json(
            data["knowledgeSource"]
        )
    else:
        import capo_qconnect.types._unknown

        out["knowledge_source"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    if data.get("filter") is not None:
        import capo_qconnect.types.retrieval_filter_configuration

        out["filter"] = (
            capo_qconnect.types.retrieval_filter_configuration.deserialize_json(
                data["filter"]
            )
        )
    if data.get("numberOfResults") is not None:
        out["number_of_results"] = data["numberOfResults"]
    if data.get("overrideKnowledgeBaseSearchType") is not None:
        out["override_knowledge_base_search_type"] = data[
            "overrideKnowledgeBaseSearchType"
        ]
    return out


def redact_sensitive(value: RetrievalConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter" in value:
        import capo_qconnect.types.retrieval_filter_configuration

        out["filter"] = (
            capo_qconnect.types.retrieval_filter_configuration.redact_sensitive(
                value["filter"]
            )
        )
    return out
