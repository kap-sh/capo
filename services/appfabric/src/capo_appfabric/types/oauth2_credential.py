"""Generated from Smithy shape ``com.amazonaws.appfabric#Oauth2Credential``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.sensitive_string2048
    import capo_appfabric.types.string2048


class Oauth2Credential(TypedDict, closed=True):
    client_id: "capo_appfabric.types.string2048.String2048"
    """<p>The client ID of the client application.</p>"""
    client_secret: "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    """<p>The client secret of the client application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2Credential) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    return out


def deserialize_json(data: dict) -> Oauth2Credential:
    out: Oauth2Credential = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("Oauth2Credential.client_id required")
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError("Oauth2Credential.client_secret required")
    return out


def redact_sensitive(value: Oauth2Credential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
