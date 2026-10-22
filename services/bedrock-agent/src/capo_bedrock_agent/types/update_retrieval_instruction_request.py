"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateRetrievalInstructionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_content
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_id


class UpdateRetrievalInstructionRequest(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction to update.</p>"""
    instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent"
    """<p>The replacement instruction content. This is a full replacement of all four fields, not a patch. During UPDATING, Get continues to return the previously-served content until the update review passes.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>A replacement description; applied together with the content when the review passes. Omit to clear.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRetrievalInstructionRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.retrieval_instruction_content

    out["instruction"] = (
        capo_bedrock_agent.types.retrieval_instruction_content.serialize_json(
            value["instruction"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRetrievalInstructionRequest:
    out: UpdateRetrievalInstructionRequest = {}  # type: ignore[typeddict-item]
    if data.get("instruction") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_content

        out["instruction"] = (
            capo_bedrock_agent.types.retrieval_instruction_content.deserialize_json(
                data["instruction"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRetrievalInstructionRequest.instruction required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: UpdateRetrievalInstructionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
