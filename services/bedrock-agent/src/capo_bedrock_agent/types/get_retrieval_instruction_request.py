"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetRetrievalInstructionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_version_selector


class GetRetrievalInstructionRequest(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction to get.</p>"""
    retrieval_instruction_version: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_version_selector.RetrievalInstructionVersionSelector"
    ]
    """<p>The version to return: a version number, or DRAFT for the retrieval instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent: omitting retrievalInstructionVersion will never resolve to a numbered version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrievalInstructionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRetrievalInstructionRequest:
    out: GetRetrievalInstructionRequest = {}  # type: ignore[typeddict-item]
    return out
