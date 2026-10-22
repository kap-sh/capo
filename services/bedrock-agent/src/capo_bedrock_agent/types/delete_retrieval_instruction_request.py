"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteRetrievalInstructionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version


class DeleteRetrievalInstructionRequest(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction to delete.</p>"""
    retrieval_instruction_version: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
    ]
    """<p>The version to delete. Omit this field to delete the retrieval instruction itself, which you can do only when it has no versions; while any version exists the service rejects the request with ConflictException. You cannot delete DRAFT on its own; deleting the retrieval instruction removes it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRetrievalInstructionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRetrievalInstructionRequest:
    out: DeleteRetrievalInstructionRequest = {}  # type: ignore[typeddict-item]
    return out
