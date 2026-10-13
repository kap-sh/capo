"""Generated from Smithy shape ``com.amazonaws.appflow#SingularConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_key


class SingularConnectorProfileCredentials(TypedDict, closed=True):
    api_key: "capo_appflow.types.api_key.ApiKey"
    """<p> A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingularConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> SingularConnectorProfileCredentials:
    out: SingularConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError(
            "SingularConnectorProfileCredentials.api_key required"
        )
    return out


def redact_sensitive(value: SingularConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
