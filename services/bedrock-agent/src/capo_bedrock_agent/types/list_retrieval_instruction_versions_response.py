"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListRetrievalInstructionVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.retrieval_instruction_version_summaries


class ListRetrievalInstructionVersionsResponse(TypedDict, closed=True):
    retrieval_instruction_version_summaries: "capo_bedrock_agent.types.retrieval_instruction_version_summaries.RetrievalInstructionVersionSummaries"
    """<p>The version summaries in this page, newest first.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>The pagination token to pass to the next ListRetrievalInstructionVersions call, absent on the last page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievalInstructionVersionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.retrieval_instruction_version_summaries

    out["retrievalInstructionVersionSummaries"] = (
        capo_bedrock_agent.types.retrieval_instruction_version_summaries.serialize_json(
            value["retrieval_instruction_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrievalInstructionVersionsResponse:
    out: ListRetrievalInstructionVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionVersionSummaries") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_version_summaries

        out["retrieval_instruction_version_summaries"] = (
            capo_bedrock_agent.types.retrieval_instruction_version_summaries.deserialize_json(
                data["retrievalInstructionVersionSummaries"]
            )
        )
    else:
        out["retrieval_instruction_version_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
