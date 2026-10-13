"""Generated from Smithy shape ``com.amazonaws.novaact#Call``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.call_id
    import capo_nova_act.types.sensitive_document


class Call(TypedDict, closed=True):
    call_id: "capo_nova_act.types.call_id.CallId"
    """<p>A unique identifier for this tool call, used to match results back to requests.</p>"""
    input: "capo_nova_act.types.sensitive_document.SensitiveDocument"
    """<p>The input parameters for the tool call, formatted according to the tool's schema.</p>"""
    name: "str"
    """<p>The name of the tool to invoke, following the pattern 'tool.{toolName}' or 'browser.{browserAction}'.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Call) -> dict:
    out: dict = {}
    out["callId"] = value["call_id"]
    out["input"] = value["input"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Call:
    out: Call = {}  # type: ignore[typeddict-item]
    if data.get("callId") is not None:
        out["call_id"] = data["callId"]
    else:
        raise DeserializationError("Call.call_id required")
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        raise DeserializationError("Call.input required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Call.name required")
    return out


def redact_sensitive(value: Call) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        out["input"] = "*** Sensitive Data Redacted ***"
    return out
