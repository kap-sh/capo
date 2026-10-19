"""Generated from Smithy shape ``com.amazonaws.devopsagent#PendingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.message


class PendingMessage(TypedDict, closed=True):
    message_id: "str"
    """<p>The unique identifier for this pending message.</p>"""
    message: "capo_devops_agent.types.message.Message"
    """<p>The message content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingMessage) -> dict:
    out: dict = {}
    out["messageId"] = value["message_id"]
    import capo_devops_agent.types.message

    out["message"] = capo_devops_agent.types.message.serialize_json(value["message"])
    return out


def deserialize_json(data: dict) -> PendingMessage:
    out: PendingMessage = {}  # type: ignore[typeddict-item]
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        out["message_id"] = ""
    if data.get("message") is not None:
        import capo_devops_agent.types.message

        out["message"] = capo_devops_agent.types.message.deserialize_json(
            data["message"]
        )
    else:
        import capo_devops_agent.types._unknown

        out["message"] = capo_devops_agent.types._unknown.UnknownUnionMember("")
    return out
