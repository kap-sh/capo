"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentActionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.id


class DeleteAgentActionGroupRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the action group belongs to.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent that the action group belongs to.</p>"""
    action_group_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group to delete.</p>"""
    skip_resource_in_use_check: NotRequired["bool"]
    """<p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentActionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentActionGroupRequest:
    out: DeleteAgentActionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
