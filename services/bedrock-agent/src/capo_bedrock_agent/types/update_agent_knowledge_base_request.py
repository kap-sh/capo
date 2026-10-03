"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_state


class UpdateAgentKnowledgeBaseRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent associated with the knowledge base that you want to update.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent associated with the knowledge base that you want to update.</p>"""
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that has been associated with an agent.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the knowledge base associated with an agent.</p>"""
    knowledge_base_state: NotRequired[
        "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
    ]
    """<p>Specifies whether the agent uses the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentKnowledgeBaseRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "knowledge_base_state" in value:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledgeBaseState"] = (
            capo_bedrock_agent.types.knowledge_base_state.serialize_json(
                value["knowledge_base_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentKnowledgeBaseRequest:
    out: UpdateAgentKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("knowledgeBaseState") is not None:
        import capo_bedrock_agent.types.knowledge_base_state

        out["knowledge_base_state"] = (
            capo_bedrock_agent.types.knowledge_base_state.deserialize_json(
                data["knowledgeBaseState"]
            )
        )
    return out
