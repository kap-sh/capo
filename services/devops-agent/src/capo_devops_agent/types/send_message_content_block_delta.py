"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_json_delta
    import capo_devops_agent.types.send_message_text_delta


class _SendMessageContentBlockDelta_textDelta(TypedDict, closed=True):
    textDelta: "capo_devops_agent.types.send_message_text_delta.SendMessageTextDelta"


class _SendMessageContentBlockDelta_jsonDelta(TypedDict, closed=True):
    jsonDelta: "capo_devops_agent.types.send_message_json_delta.SendMessageJsonDelta"


SendMessageContentBlockDelta: TypeAlias = (
    _SendMessageContentBlockDelta_textDelta
    | _SendMessageContentBlockDelta_jsonDelta
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockDelta) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SendMessageContentBlockDelta: cannot serialize unknown variant {value.name!r}"
        )
    elif "textDelta" in value:
        import capo_devops_agent.types.send_message_text_delta

        return {
            "textDelta": capo_devops_agent.types.send_message_text_delta.serialize_json(
                value["textDelta"]
            )
        }
    elif "jsonDelta" in value:
        import capo_devops_agent.types.send_message_json_delta

        return {
            "jsonDelta": capo_devops_agent.types.send_message_json_delta.serialize_json(
                value["jsonDelta"]
            )
        }
    else:
        raise SerializationError("SendMessageContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> SendMessageContentBlockDelta:
    if data.get("textDelta") is not None:
        import capo_devops_agent.types.send_message_text_delta

        return {
            "textDelta": capo_devops_agent.types.send_message_text_delta.deserialize_json(
                data["textDelta"]
            )
        }
    elif data.get("jsonDelta") is not None:
        import capo_devops_agent.types.send_message_json_delta

        return {
            "jsonDelta": capo_devops_agent.types.send_message_json_delta.deserialize_json(
                data["jsonDelta"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "SendMessageContentBlockDelta: no recognized variant key"
        )
