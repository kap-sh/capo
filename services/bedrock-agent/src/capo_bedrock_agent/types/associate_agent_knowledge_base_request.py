"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AssociateAgentKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_state


class AssociateAgentKnowledgeBaseRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent with which you want to associate the knowledge base.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent with which you want to associate the knowledge base.</p>"""
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to associate with the agent.</p>"""
    description: "capo_bedrock_agent.types.description.Description"
    """<p>A description of what the agent should use the knowledge base for.</p>"""
    knowledge_base_state: NotRequired[
        "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
    ]
    """<p>Specifies whether to use the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAgentKnowledgeBaseRequest) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["description"] = value["description"]
    if "knowledge_base_state" in value:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledgeBaseState"] = (
            capo_bedrock_agent.types.knowledge_base_state.serialize_json(
                value["knowledge_base_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateAgentKnowledgeBaseRequest:
    out: AssociateAgentKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "AssociateAgentKnowledgeBaseRequest.knowledge_base_id required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AssociateAgentKnowledgeBaseRequest.description required"
        )
    if data.get("knowledgeBaseState") is not None:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledge_base_state"] = (
            capo_bedrock_agent.types.knowledge_base_state.deserialize_json(
                data["knowledgeBaseState"]
            )
        )
    return out
