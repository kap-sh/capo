"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_summaries
    import capo_quicksight.types.next_token
    import capo_quicksight.types.status_code


class SearchKnowledgeBasesResponse(TypedDict, closed=True):
    knowledge_base_summaries: (
        "capo_quicksight.types.knowledge_base_summaries.KnowledgeBaseSummaries"
    )
    """<p>A list of knowledge base summaries.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["capo_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.knowledge_base_summaries

    out["KnowledgeBaseSummaries"] = (
        capo_quicksight.types.knowledge_base_summaries.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchKnowledgeBasesResponse:
    out: SearchKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseSummaries") is not None:
        import capo_quicksight.types.knowledge_base_summaries

        out["knowledge_base_summaries"] = (
            capo_quicksight.types.knowledge_base_summaries.deserialize_json(
                data["KnowledgeBaseSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "SearchKnowledgeBasesResponse.knowledge_base_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: SearchKnowledgeBasesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_summaries" in value:
        import capo_quicksight.types.knowledge_base_summaries

        out["knowledge_base_summaries"] = (
            capo_quicksight.types.knowledge_base_summaries.redact_sensitive(
                value["knowledge_base_summaries"]
            )
        )
    return out
