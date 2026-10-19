"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolUseResultData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.json_document
    import capo_qconnect.types.non_empty_string


class ToolUseResultData(TypedDict, closed=True):
    tool_use_id: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the tool use instance.</p>"""
    tool_name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the tool that was used.</p>"""
    tool_result: "capo_qconnect.types.json_document.JSONDocument"
    """<p>The result of the tool usage.</p>"""
    input_schema: NotRequired["capo_qconnect.types.json_document.JSONDocument"]
    """<p>The input schema for the tool use result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseResultData) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["toolName"] = value["tool_name"]
    out["toolResult"] = value["tool_result"]
    if "input_schema" in value:
        out["inputSchema"] = value["input_schema"]
    return out


def deserialize_json(data: dict) -> ToolUseResultData:
    out: ToolUseResultData = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        out["tool_use_id"] = ""
    if data.get("toolName") is not None:
        out["tool_name"] = data["toolName"]
    else:
        out["tool_name"] = ""
    if data.get("toolResult") is not None:
        out["tool_result"] = data["toolResult"]
    else:
        out["tool_result"] = None
    if data.get("inputSchema") is not None:
        out["input_schema"] = data["inputSchema"]
    return out


def redact_sensitive(value: ToolUseResultData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tool_result" in value:
        out["tool_result"] = "*** Sensitive Data Redacted ***"
    if "input_schema" in value:
        out["input_schema"] = "*** Sensitive Data Redacted ***"
    return out
