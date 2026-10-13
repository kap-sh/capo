"""Generated from Smithy shape ``com.amazonaws.appfabric#ApiKeyCredential``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.sensitive_string2048


class ApiKeyCredential(TypedDict, closed=True):
    api_key: "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    """<p>An API key for an application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredential) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> ApiKeyCredential:
    out: ApiKeyCredential = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("ApiKeyCredential.api_key required")
    return out


def redact_sensitive(value: ApiKeyCredential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
