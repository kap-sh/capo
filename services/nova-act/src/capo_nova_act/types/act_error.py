"""Generated from Smithy shape ``com.amazonaws.novaact#ActError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.sensitive_string


class ActError(TypedDict, closed=True):
    message: "capo_nova_act.types.sensitive_string.SensitiveString"
    """<p>A human-readable description of the error that occurred.</p>"""
    type: NotRequired["str"]
    """<p>The type or category of error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ActError:
    out: ActError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out


def redact_sensitive(value: ActError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
