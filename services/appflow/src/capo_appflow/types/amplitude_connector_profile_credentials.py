"""Generated from Smithy shape ``com.amazonaws.appflow#AmplitudeConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.api_key
    import capo_appflow.types.secret_key


class AmplitudeConnectorProfileCredentials(TypedDict, closed=True):
    api_key: "capo_appflow.types.api_key.ApiKey"
    """<p> A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API. </p>"""
    secret_key: "capo_appflow.types.secret_key.SecretKey"
    """<p> The Secret Access Key portion of the credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmplitudeConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    out["secretKey"] = value["secret_key"]
    return out


def deserialize_json(data: dict) -> AmplitudeConnectorProfileCredentials:
    out: AmplitudeConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        out["api_key"] = ""
    if data.get("secretKey") is not None:
        out["secret_key"] = data["secretKey"]
    else:
        out["secret_key"] = ""
    return out


def redact_sensitive(value: AmplitudeConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    if "secret_key" in value:
        out["secret_key"] = "*** Sensitive Data Redacted ***"
    return out
