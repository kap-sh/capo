"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateChatRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.chat_archive_status
    import capo_devops_agent.types.resource_id


class UpdateChatRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier of the agent space that contains the chat execution to update.</p>"""
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the chat execution to update.</p>"""
    summary: NotRequired["str"]
    """<p>The new summary to set for the chat execution.</p>"""
    archive_status: NotRequired[
        "capo_devops_agent.types.chat_archive_status.ChatArchiveStatus"
    ]
    """<p>The archive status to set for the chat execution. Use this parameter to archive the chat execution, hiding it from the default chat list, or to unarchive it, restoring it to the default chat list.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChatRequest) -> dict:
    out: dict = {}
    if "summary" in value:
        out["summary"] = value["summary"]
    if "archive_status" in value:
        import capo_devops_agent.types.chat_archive_status

        out["archiveStatus"] = (
            capo_devops_agent.types.chat_archive_status.serialize_json(
                value["archive_status"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateChatRequest:
    out: UpdateChatRequest = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("archiveStatus") is not None:
        import capo_devops_agent.types.chat_archive_status

        out["archive_status"] = (
            capo_devops_agent.types.chat_archive_status.deserialize_json(
                data["archiveStatus"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
