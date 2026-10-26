"""Generated from Smithy shape ``com.amazonaws.qbusiness#CopyFromSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.conversation_source


class _CopyFromSource_conversation(TypedDict, closed=True):
    conversation: "capo_qbusiness.types.conversation_source.ConversationSource"


CopyFromSource: TypeAlias = _CopyFromSource_conversation | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CopyFromSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CopyFromSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "conversation" in value:
        import capo_qbusiness.types.conversation_source

        return {
            "conversation": capo_qbusiness.types.conversation_source.serialize_json(
                value["conversation"]
            )
        }
    else:
        raise SerializationError("CopyFromSource: no variant present")


def deserialize_json(data: dict) -> CopyFromSource:
    if data.get("conversation") is not None:
        import capo_qbusiness.types.conversation_source

        return {
            "conversation": capo_qbusiness.types.conversation_source.deserialize_json(
                data["conversation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CopyFromSource: no recognized variant key")
