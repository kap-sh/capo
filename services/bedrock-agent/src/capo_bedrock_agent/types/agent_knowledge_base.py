"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentKnowledgeBase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_state
    import capo_bedrock_agent.types.version


class AgentKnowledgeBase(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent with which the knowledge base is associated.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent with which the knowledge base is associated.</p>"""
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the association between the agent and the knowledge base.</p>"""
    description: "capo_bedrock_agent.types.description.Description"
    """<p>The description of the association between the agent and the knowledge base.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the association between the agent and the knowledge base was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the association between the agent and the knowledge base was last updated.</p>"""
    knowledge_base_state: (
        "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
    )
    """<p>Specifies whether to use the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentKnowledgeBase) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["description"] = value["description"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_bedrock_agent.types.knowledge_base_state

    out["knowledgeBaseState"] = (
        capo_bedrock_agent.types.knowledge_base_state.serialize_json(
            value["knowledge_base_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentKnowledgeBase:
    out: AgentKnowledgeBase = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentKnowledgeBase.agent_id required")
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentKnowledgeBase.agent_version required")
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("AgentKnowledgeBase.knowledge_base_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AgentKnowledgeBase.description required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentKnowledgeBase.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentKnowledgeBase.updated_at required")
    if data.get("knowledgeBaseState") is not None:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledge_base_state"] = (
            capo_bedrock_agent.types.knowledge_base_state.deserialize_json(
                data["knowledgeBaseState"]
            )
        )
    else:
        raise DeserializationError("AgentKnowledgeBase.knowledge_base_state required")
    return out
