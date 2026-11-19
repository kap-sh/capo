"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetChatResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.chat_archive_status
    import capo_devops_agent.types.resource_id


class GetChatResponse(TypedDict, closed=True):
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the chat execution.</p>"""
    summary: NotRequired["str"]
    """<p>The summary of the chat execution.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time at which the chat execution was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time at which the chat execution was last updated.</p>"""
    archive_status: "capo_devops_agent.types.chat_archive_status.ChatArchiveStatus"
    """<p>Indicates whether the chat execution is archived or active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    if "summary" in value:
        out["summary"] = value["summary"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types._prelude.timestamp

    out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_devops_agent.types.chat_archive_status

    out["archiveStatus"] = capo_devops_agent.types.chat_archive_status.serialize_json(
        value["archive_status"]
    )
    return out


def deserialize_json(data: dict) -> GetChatResponse:
    out: GetChatResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("archiveStatus") is not None:
        import capo_devops_agent.types.chat_archive_status

        out["archive_status"] = (
            capo_devops_agent.types.chat_archive_status.deserialize_json(
                data["archiveStatus"]
            )
        )
    else:
        import typing

        out["archive_status"] = typing.cast(
            "capo_devops_agent.types.chat_archive_status.ChatArchiveStatus", ""
        )
    return out
