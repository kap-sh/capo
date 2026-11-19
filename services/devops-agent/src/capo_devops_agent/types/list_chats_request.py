"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListChatsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.chat_archive_status
    import capo_devops_agent.types.resource_id


class ListChatsRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space to list chats from.</p>"""
    user_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>The user identifier to list chats for. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return</p>"""
    next_token: NotRequired["str"]
    """<p>Token for pagination</p>"""
    archive_status: NotRequired[
        "capo_devops_agent.types.chat_archive_status.ChatArchiveStatus"
    ]
    """<p>The archive status to filter by. Use this parameter to list only archived chat executions or only active ones.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChatsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChatsRequest:
    out: ListChatsRequest = {}  # type: ignore[typeddict-item]
    return out
