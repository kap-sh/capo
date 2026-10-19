"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanToolResultValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.span_message_value_list
    import capo_qconnect.types.uuid


class SpanToolResultValue(TypedDict, closed=True):
    tool_use_id: "capo_qconnect.types.uuid.Uuid"
    """<p>Relates this result back to the tool invocation</p>"""
    values: "capo_qconnect.types.span_message_value_list.SpanMessageValueList"
    """<p>The tool results</p>"""
    error: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The tool invocation error if failed</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanToolResultValue) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    import capo_qconnect.types.span_message_value_list

    out["values"] = capo_qconnect.types.span_message_value_list.serialize_json(
        value["values"]
    )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> SpanToolResultValue:
    out: SpanToolResultValue = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        out["tool_use_id"] = ""
    if data.get("values") is not None:
        import capo_qconnect.types.span_message_value_list

        out["values"] = capo_qconnect.types.span_message_value_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("error") is not None:
        out["error"] = data["error"]
    return out


def redact_sensitive(value: SpanToolResultValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_qconnect.types.span_message_value_list

        out["values"] = capo_qconnect.types.span_message_value_list.redact_sensitive(
            value["values"]
        )
    return out
