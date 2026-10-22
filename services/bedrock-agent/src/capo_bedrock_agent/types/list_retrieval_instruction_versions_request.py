"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListRetrievalInstructionVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_max_results


class ListRetrievalInstructionVersionsRequest(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction whose versions to list.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
    ]
    """<p>Specifies the maximum number of versions to return in a single page. The service enforces the effective upper bound.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>The pagination token from a previous ListRetrievalInstructionVersions response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievalInstructionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRetrievalInstructionVersionsRequest:
    out: ListRetrievalInstructionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
