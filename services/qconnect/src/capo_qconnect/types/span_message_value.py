"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessageValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.span_reasoning_value
    import capo_qconnect.types.span_text_value
    import capo_qconnect.types.span_tool_result_value
    import capo_qconnect.types.span_tool_use_value


class _SpanMessageValue_text(TypedDict, closed=True):
    text: "capo_qconnect.types.span_text_value.SpanTextValue"


class _SpanMessageValue_toolUse(TypedDict, closed=True):
    toolUse: "capo_qconnect.types.span_tool_use_value.SpanToolUseValue"


class _SpanMessageValue_toolResult(TypedDict, closed=True):
    toolResult: "capo_qconnect.types.span_tool_result_value.SpanToolResultValue"


class _SpanMessageValue_reasoning(TypedDict, closed=True):
    reasoning: "capo_qconnect.types.span_reasoning_value.SpanReasoningValue"


SpanMessageValue: TypeAlias = (
    _SpanMessageValue_text
    | _SpanMessageValue_toolUse
    | _SpanMessageValue_toolResult
    | _SpanMessageValue_reasoning
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessageValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SpanMessageValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        import capo_qconnect.types.span_text_value

        return {
            "text": capo_qconnect.types.span_text_value.serialize_json(value["text"])
        }
    elif "toolUse" in value:
        import capo_qconnect.types.span_tool_use_value

        return {
            "toolUse": capo_qconnect.types.span_tool_use_value.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_qconnect.types.span_tool_result_value

        return {
            "toolResult": capo_qconnect.types.span_tool_result_value.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoning" in value:
        import capo_qconnect.types.span_reasoning_value

        return {
            "reasoning": capo_qconnect.types.span_reasoning_value.serialize_json(
                value["reasoning"]
            )
        }
    else:
        raise SerializationError("SpanMessageValue: no variant present")


def deserialize_json(data: dict) -> SpanMessageValue:
    if data.get("text") is not None:
        import capo_qconnect.types.span_text_value

        return {
            "text": capo_qconnect.types.span_text_value.deserialize_json(data["text"])
        }
    elif data.get("toolUse") is not None:
        import capo_qconnect.types.span_tool_use_value

        return {
            "toolUse": capo_qconnect.types.span_tool_use_value.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_qconnect.types.span_tool_result_value

        return {
            "toolResult": capo_qconnect.types.span_tool_result_value.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("reasoning") is not None:
        import capo_qconnect.types.span_reasoning_value

        return {
            "reasoning": capo_qconnect.types.span_reasoning_value.deserialize_json(
                data["reasoning"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SpanMessageValue: no recognized variant key")


def redact_sensitive(value: SpanMessageValue) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        import capo_qconnect.types.span_text_value

        out["text"] = capo_qconnect.types.span_text_value.redact_sensitive(
            value["text"]
        )
    if "toolUse" in value:
        import capo_qconnect.types.span_tool_use_value

        out["toolUse"] = capo_qconnect.types.span_tool_use_value.redact_sensitive(
            value["toolUse"]
        )
    if "toolResult" in value:
        import capo_qconnect.types.span_tool_result_value

        out["toolResult"] = capo_qconnect.types.span_tool_result_value.redact_sensitive(
            value["toolResult"]
        )
    if "reasoning" in value:
        import capo_qconnect.types.span_reasoning_value

        out["reasoning"] = capo_qconnect.types.span_reasoning_value.redact_sensitive(
            value["reasoning"]
        )
    return out
