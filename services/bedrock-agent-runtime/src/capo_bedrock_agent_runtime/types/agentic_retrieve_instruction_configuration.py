"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveInstructionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_instruction_id
    import capo_bedrock_agent_runtime.types.retrieval_instruction_version


class AgenticRetrieveInstructionConfiguration(TypedDict, closed=True):
    retrieval_instruction_id: "capo_bedrock_agent_runtime.types.retrieval_instruction_id.RetrievalInstructionId"
    """<p>The identifier of the retrieval instruction. The instruction must exist in the caller's account and its status must be ACTIVE.</p>"""
    version: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_instruction_version.RetrievalInstructionVersion"
    ]
    """<p>The version of the retrieval instruction to apply: a version number, or DRAFT for the instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveInstructionConfiguration) -> dict:
    out: dict = {}
    out["retrievalInstructionId"] = value["retrieval_instruction_id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveInstructionConfiguration:
    out: AgenticRetrieveInstructionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionId") is not None:
        out["retrieval_instruction_id"] = data["retrievalInstructionId"]
    else:
        out["retrieval_instruction_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
