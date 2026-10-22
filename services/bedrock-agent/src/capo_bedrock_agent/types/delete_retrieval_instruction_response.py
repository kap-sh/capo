"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteRetrievalInstructionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_arn
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version


class DeleteRetrievalInstructionResponse(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the deleted retrieval instruction.</p>"""
    retrieval_instruction_arn: (
        "capo_bedrock_agent.types.retrieval_instruction_arn.RetrievalInstructionArn"
    )
    """<p>The ARN of the retrieval instruction.</p>"""
    version: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
    ]
    """<p>The version that you deleted. Absent when you deleted the whole retrieval instruction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRetrievalInstructionResponse) -> dict:
    out: dict = {}
    out["retrievalInstructionId"] = value["retrieval_instruction_id"]
    out["retrievalInstructionArn"] = value["retrieval_instruction_arn"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DeleteRetrievalInstructionResponse:
    out: DeleteRetrievalInstructionResponse = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionId") is not None:
        out["retrieval_instruction_id"] = data["retrievalInstructionId"]
    else:
        out["retrieval_instruction_id"] = ""
    if data.get("retrievalInstructionArn") is not None:
        out["retrieval_instruction_arn"] = data["retrievalInstructionArn"]
    else:
        out["retrieval_instruction_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
