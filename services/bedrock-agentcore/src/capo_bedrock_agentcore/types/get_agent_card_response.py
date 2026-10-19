"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetAgentCardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_card
    import capo_bedrock_agentcore.types.http_response_code
    import capo_bedrock_agentcore.types.session_id


class GetAgentCardResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The ID of the session associated with the AgentCore Runtime agent.</p>"""
    agent_card: "capo_bedrock_agentcore.types.agent_card.AgentCard"
    """<p>An agent card document that contains metadata and capabilities for an AgentCore Runtime agent.</p>"""
    status_code: NotRequired[
        "capo_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentCardResponse) -> dict:
    out: dict = {}
    out["agentCard"] = value["agent_card"]
    return out


def deserialize_json(data: dict) -> GetAgentCardResponse:
    out: GetAgentCardResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentCard") is not None:
        out["agent_card"] = data["agentCard"]
    else:
        out["agent_card"] = None
    return out
