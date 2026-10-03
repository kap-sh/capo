"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentKnowledgeBaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_state


class AgentKnowledgeBaseSummary(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base associated with an agent.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the knowledge base associated with an agent.</p>"""
    knowledge_base_state: (
        "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
    )
    """<p>Specifies whether the agent uses the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the knowledge base associated with an agent was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentKnowledgeBaseSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.knowledge_base_state

    out["knowledgeBaseState"] = (
        capo_bedrock_agent.types.knowledge_base_state.serialize_json(
            value["knowledge_base_state"]
        )
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AgentKnowledgeBaseSummary:
    out: AgentKnowledgeBaseSummary = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "AgentKnowledgeBaseSummary.knowledge_base_id required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("knowledgeBaseState") is not None:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledge_base_state"] = (
            capo_bedrock_agent.types.knowledge_base_state.deserialize_json(
                data["knowledgeBaseState"]
            )
        )
    else:
        raise DeserializationError(
            "AgentKnowledgeBaseSummary.knowledge_base_state required"
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentKnowledgeBaseSummary.updated_at required")
    return out
