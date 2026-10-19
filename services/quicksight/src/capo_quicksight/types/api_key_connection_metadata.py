"""Generated from Smithy shape ``com.amazonaws.quicksight#APIKeyConnectionMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.api_key
    import capo_quicksight.types.email
    import capo_quicksight.types.endpoint


class APIKeyConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    api_key: "capo_quicksight.types.api_key.APIKey"
    """<p>The API key used for authentication.</p>"""
    email: NotRequired["capo_quicksight.types.email.Email"]
    """<p>The email address associated with the API key, if required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: APIKeyConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["ApiKey"] = value["api_key"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_json(data: dict) -> APIKeyConnectionMetadata:
    out: APIKeyConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("ApiKey") is not None:
        out["api_key"] = data["ApiKey"]
    else:
        out["api_key"] = ""
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    return out


def redact_sensitive(value: APIKeyConnectionMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
