"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageData``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.json_document
    import capo_qconnect.types.text_message
    import capo_qconnect.types.tool_use_result_data


class _MessageData_text(TypedDict, closed=True):
    text: "capo_qconnect.types.text_message.TextMessage"


class _MessageData_toolUseResult(TypedDict, closed=True):
    toolUseResult: "capo_qconnect.types.tool_use_result_data.ToolUseResultData"


class _MessageData_data(TypedDict, closed=True):
    data: "capo_qconnect.types.json_document.JSONDocument"


MessageData: TypeAlias = (
    _MessageData_text
    | _MessageData_toolUseResult
    | _MessageData_data
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageData) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MessageData: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        import capo_qconnect.types.text_message

        return {"text": capo_qconnect.types.text_message.serialize_json(value["text"])}
    elif "toolUseResult" in value:
        import capo_qconnect.types.tool_use_result_data

        return {
            "toolUseResult": capo_qconnect.types.tool_use_result_data.serialize_json(
                value["toolUseResult"]
            )
        }
    elif "data" in value:
        return {"data": value["data"]}
    else:
        raise SerializationError("MessageData: no variant present")


def deserialize_json(data: dict) -> MessageData:
    if data.get("text") is not None:
        import capo_qconnect.types.text_message

        return {"text": capo_qconnect.types.text_message.deserialize_json(data["text"])}
    elif data.get("toolUseResult") is not None:
        import capo_qconnect.types.tool_use_result_data

        return {
            "toolUseResult": capo_qconnect.types.tool_use_result_data.deserialize_json(
                data["toolUseResult"]
            )
        }
    elif data.get("data") is not None:
        return {"data": data["data"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MessageData: no recognized variant key")


def redact_sensitive(value: MessageData) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        import capo_qconnect.types.text_message

        out["text"] = capo_qconnect.types.text_message.redact_sensitive(value["text"])
    if "toolUseResult" in value:
        import capo_qconnect.types.tool_use_result_data

        out["toolUseResult"] = (
            capo_qconnect.types.tool_use_result_data.redact_sensitive(
                value["toolUseResult"]
            )
        )
    if "data" in value:
        out["data"] = "*** Sensitive Data Redacted ***"
    return out
