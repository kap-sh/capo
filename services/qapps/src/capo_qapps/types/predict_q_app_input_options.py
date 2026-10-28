"""Generated from Smithy shape ``com.amazonaws.qapps#PredictQAppInputOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError, SerializationError
from capo_qapps.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qapps.types.message_list


class PredictQAppInputOptionsConversationMember(TypedDict, closed=True):
    conversation: "capo_qapps.types.message_list.MessageList"


class PredictQAppInputOptionsProblemStatementMember(TypedDict, closed=True):
    problemStatement: "str"


PredictQAppInputOptions: TypeAlias = (
    PredictQAppInputOptionsConversationMember
    | PredictQAppInputOptionsProblemStatementMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAppInputOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PredictQAppInputOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "conversation" in value:
        import capo_qapps.types.message_list

        return {
            "conversation": capo_qapps.types.message_list.serialize_json(
                value["conversation"]
            )
        }
    elif "problemStatement" in value:
        return {"problemStatement": value["problemStatement"]}
    else:
        raise SerializationError("PredictQAppInputOptions: no variant present")


def deserialize_json(data: dict) -> PredictQAppInputOptions:
    if data.get("conversation") is not None:
        import capo_qapps.types.message_list

        return {
            "conversation": capo_qapps.types.message_list.deserialize_json(
                data["conversation"]
            )
        }
    elif data.get("problemStatement") is not None:
        return {"problemStatement": data["problemStatement"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PredictQAppInputOptions: no recognized variant key")
