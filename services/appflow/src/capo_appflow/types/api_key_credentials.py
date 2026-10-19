"""Generated from Smithy shape ``com.amazonaws.appflow#ApiKeyCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.api_key
    import capo_appflow.types.api_secret_key


class ApiKeyCredentials(TypedDict, closed=True):
    api_key: "capo_appflow.types.api_key.ApiKey"
    """<p>The API key required for API key authentication.</p>"""
    api_secret_key: NotRequired["capo_appflow.types.api_secret_key.ApiSecretKey"]
    """<p>The API secret key required for API key authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    if "api_secret_key" in value:
        out["apiSecretKey"] = value["api_secret_key"]
    return out


def deserialize_json(data: dict) -> ApiKeyCredentials:
    out: ApiKeyCredentials = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        out["api_key"] = ""
    if data.get("apiSecretKey") is not None:
        out["api_secret_key"] = data["apiSecretKey"]
    return out


def redact_sensitive(value: ApiKeyCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    if "api_secret_key" in value:
        out["api_secret_key"] = "*** Sensitive Data Redacted ***"
    return out
