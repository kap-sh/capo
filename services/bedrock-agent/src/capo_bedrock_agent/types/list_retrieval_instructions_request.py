"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListRetrievalInstructionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.retrieval_instruction_max_results
    import capo_bedrock_agent.types.retrieval_instruction_status


class ListRetrievalInstructionsRequest(TypedDict, closed=True):
    status: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_status.RetrievalInstructionStatus"
    ]
    """<p>Return only instructions with this availability status.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
    ]
    """<p>The maximum number of results to return in a single page. The effective upper bound is enforced service-side.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>The pagination token from a previous ListRetrievalInstructions response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievalInstructionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRetrievalInstructionsRequest:
    out: ListRetrievalInstructionsRequest = {}  # type: ignore[typeddict-item]
    return out
