"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveAppliedInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_instruction_id
    import capo_bedrock_agent_runtime.types.retrieval_instruction_version


class AgenticRetrieveAppliedInstruction(TypedDict, closed=True):
    id: "capo_bedrock_agent_runtime.types.retrieval_instruction_id.RetrievalInstructionId"
    """<p>The identifier of the retrieval instruction applied.</p>"""
    version: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_instruction_version.RetrievalInstructionVersion"
    ]
    """<p>The version that was applied: a version number, or DRAFT. The service reports this version whenever it reports appliedInstruction, including DRAFT when the request did not specify a version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveAppliedInstruction) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveAppliedInstruction:
    out: AgenticRetrieveAppliedInstruction = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
