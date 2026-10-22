"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListRetrievalInstructionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.retrieval_instruction_summaries


class ListRetrievalInstructionsResponse(TypedDict, closed=True):
    retrieval_instruction_summaries: "capo_bedrock_agent.types.retrieval_instruction_summaries.RetrievalInstructionSummaries"
    """<p>The retrieval instruction summaries in this page.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>The pagination token to pass to the next ListRetrievalInstructions call, absent on the last page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievalInstructionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.retrieval_instruction_summaries

    out["retrievalInstructionSummaries"] = (
        capo_bedrock_agent.types.retrieval_instruction_summaries.serialize_json(
            value["retrieval_instruction_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrievalInstructionsResponse:
    out: ListRetrievalInstructionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionSummaries") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_summaries

        out["retrieval_instruction_summaries"] = (
            capo_bedrock_agent.types.retrieval_instruction_summaries.deserialize_json(
                data["retrievalInstructionSummaries"]
            )
        )
    else:
        out["retrieval_instruction_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRetrievalInstructionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieval_instruction_summaries" in value:
        import capo_bedrock_agent.types.retrieval_instruction_summaries

        out["retrieval_instruction_summaries"] = (
            capo_bedrock_agent.types.retrieval_instruction_summaries.redact_sensitive(
                value["retrieval_instruction_summaries"]
            )
        )
    return out
