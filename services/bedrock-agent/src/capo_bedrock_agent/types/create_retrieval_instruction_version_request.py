"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateRetrievalInstructionVersionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_id


class CreateRetrievalInstructionVersionRequest(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction to version.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>A description of this version. Independent of the retrieval instruction's own description.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A caller-supplied token that makes a retried call return the version created by the first call rather than a second version. The window is 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRetrievalInstructionVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRetrievalInstructionVersionRequest:
    out: CreateRetrievalInstructionVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateRetrievalInstructionVersionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
