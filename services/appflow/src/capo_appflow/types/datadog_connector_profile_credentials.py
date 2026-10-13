"""Generated from Smithy shape ``com.amazonaws.appflow#DatadogConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_key
    import capo_appflow.types.application_key


class DatadogConnectorProfileCredentials(TypedDict, closed=True):
    api_key: "capo_appflow.types.api_key.ApiKey"
    """<p> A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API. </p>"""
    application_key: "capo_appflow.types.application_key.ApplicationKey"
    """<p> Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatadogConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    out["applicationKey"] = value["application_key"]
    return out


def deserialize_json(data: dict) -> DatadogConnectorProfileCredentials:
    out: DatadogConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError(
            "DatadogConnectorProfileCredentials.api_key required"
        )
    if data.get("applicationKey") is not None:
        out["application_key"] = data["applicationKey"]
    else:
        raise DeserializationError(
            "DatadogConnectorProfileCredentials.application_key required"
        )
    return out


def redact_sensitive(value: DatadogConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
