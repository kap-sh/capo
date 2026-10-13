"""Generated from Smithy shape ``com.amazonaws.appflow#TrendmicroConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_secret_key


class TrendmicroConnectorProfileCredentials(TypedDict, closed=True):
    api_secret_key: "capo_appflow.types.api_secret_key.ApiSecretKey"
    """<p> The Secret Access Key portion of the credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrendmicroConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiSecretKey"] = value["api_secret_key"]
    return out


def deserialize_json(data: dict) -> TrendmicroConnectorProfileCredentials:
    out: TrendmicroConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("apiSecretKey") is not None:
        out["api_secret_key"] = data["apiSecretKey"]
    else:
        raise DeserializationError(
            "TrendmicroConnectorProfileCredentials.api_secret_key required"
        )
    return out


def redact_sensitive(value: TrendmicroConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_secret_key" in value:
        out["api_secret_key"] = "*** Sensitive Data Redacted ***"
    return out
