"""Generated from Smithy shape ``com.amazonaws.account#ValidationExceptionField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account.types.sensitive_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "capo_account.types.sensitive_string.SensitiveString"
    """<p>A message about the validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


def redact_sensitive(value: ValidationExceptionField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
