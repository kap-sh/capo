"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateChatResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.resource_id


class CreateChatResponse(TypedDict, closed=True):
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for the created execution</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the chat was created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateChatResponse:
    out: CreateChatResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
