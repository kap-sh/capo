"""Generated from Smithy shape ``com.amazonaws.devopsagent#Message``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.assistant_message
    import capo_devops_agent.types.user_message


class MessageUserMessageMember(TypedDict, closed=True):
    userMessage: "capo_devops_agent.types.user_message.UserMessage"


class MessageAssistantMessageMember(TypedDict, closed=True):
    assistantMessage: "capo_devops_agent.types.assistant_message.AssistantMessage"


Message: TypeAlias = (
    MessageUserMessageMember | MessageAssistantMessageMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Message: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "userMessage" in value:
        import capo_devops_agent.types.user_message

        return {
            "userMessage": capo_devops_agent.types.user_message.serialize_json(
                value["userMessage"]
            )
        }
    elif "assistantMessage" in value:
        import capo_devops_agent.types.assistant_message

        return {
            "assistantMessage": capo_devops_agent.types.assistant_message.serialize_json(
                value["assistantMessage"]
            )
        }
    else:
        raise SerializationError("Message: no variant present")


def deserialize_json(data: dict) -> Message:
    if data.get("userMessage") is not None:
        import capo_devops_agent.types.user_message

        return {
            "userMessage": capo_devops_agent.types.user_message.deserialize_json(
                data["userMessage"]
            )
        }
    elif data.get("assistantMessage") is not None:
        import capo_devops_agent.types.assistant_message

        return {
            "assistantMessage": capo_devops_agent.types.assistant_message.deserialize_json(
                data["assistantMessage"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Message: no recognized variant key")
