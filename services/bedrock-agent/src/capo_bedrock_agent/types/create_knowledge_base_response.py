"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base


class CreateKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base: "capo_bedrock_agent.types.knowledge_base.KnowledgeBase"
    """<p>Contains details about the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base

    out["knowledgeBase"] = capo_bedrock_agent.types.knowledge_base.serialize_json(
        value["knowledge_base"]
    )
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseResponse:
    out: CreateKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBase") is not None:
        import capo_bedrock_agent.types.knowledge_base

        out["knowledge_base"] = (
            capo_bedrock_agent.types.knowledge_base.deserialize_json(
                data["knowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseResponse.knowledge_base required"
        )
    return out


def redact_sensitive(value: CreateKnowledgeBaseResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base" in value:
        import capo_bedrock_agent.types.knowledge_base

        out["knowledge_base"] = (
            capo_bedrock_agent.types.knowledge_base.redact_sensitive(
                value["knowledge_base"]
            )
        )
    return out
