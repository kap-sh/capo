"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMessages``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.messages_list


class ExtractionJobMessagesMessagesListMember(TypedDict, closed=True):
    messagesList: "capo_bedrock_agentcore.types.messages_list.MessagesList"


ExtractionJobMessages: TypeAlias = (
    ExtractionJobMessagesMessagesListMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMessages) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExtractionJobMessages: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "messagesList" in value:
        import capo_bedrock_agentcore.types.messages_list

        return {
            "messagesList": capo_bedrock_agentcore.types.messages_list.serialize_json(
                value["messagesList"]
            )
        }
    else:
        raise SerializationError("ExtractionJobMessages: no variant present")


def deserialize_json(data: dict) -> ExtractionJobMessages:
    if data.get("messagesList") is not None:
        import capo_bedrock_agentcore.types.messages_list

        return {
            "messagesList": capo_bedrock_agentcore.types.messages_list.deserialize_json(
                data["messagesList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExtractionJobMessages: no recognized variant key")
