"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_status


class DeleteKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that was deleted.</p>"""
    status: "capo_bedrock_agent.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base and whether it has been successfully deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKnowledgeBaseResponse) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    import capo_bedrock_agent.types.knowledge_base_status

    out["status"] = capo_bedrock_agent.types.knowledge_base_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteKnowledgeBaseResponse:
    out: DeleteKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.knowledge_base_status

        out["status"] = capo_bedrock_agent.types.knowledge_base_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.knowledge_base_status.KnowledgeBaseStatus", ""
        )
    return out
