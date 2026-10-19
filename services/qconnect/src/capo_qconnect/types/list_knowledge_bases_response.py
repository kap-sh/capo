"""Generated from Smithy shape ``com.amazonaws.qconnect#ListKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_list
    import capo_qconnect.types.non_empty_string


class ListKnowledgeBasesResponse(TypedDict, closed=True):
    knowledge_base_summaries: (
        "capo_qconnect.types.knowledge_base_list.KnowledgeBaseList"
    )
    """<p>Information about the knowledge bases.</p>"""
    next_token: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.knowledge_base_list

    out["knowledgeBaseSummaries"] = (
        capo_qconnect.types.knowledge_base_list.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesResponse:
    out: ListKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseSummaries") is not None:
        import capo_qconnect.types.knowledge_base_list

        out["knowledge_base_summaries"] = (
            capo_qconnect.types.knowledge_base_list.deserialize_json(
                data["knowledgeBaseSummaries"]
            )
        )
    else:
        out["knowledge_base_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListKnowledgeBasesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_summaries" in value:
        import capo_qconnect.types.knowledge_base_list

        out["knowledge_base_summaries"] = (
            capo_qconnect.types.knowledge_base_list.redact_sensitive(
                value["knowledge_base_summaries"]
            )
        )
    return out
