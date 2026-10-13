"""Generated from Smithy shape ``com.amazonaws.quicksight#BasicAuthConnectionMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.action_password
    import capo_quicksight.types.action_user_name
    import capo_quicksight.types.endpoint


class BasicAuthConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    username: "capo_quicksight.types.action_user_name.ActionUserName"
    """<p>The username for basic authentication.</p>"""
    password: "capo_quicksight.types.action_password.ActionPassword"
    """<p>The password for basic authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> BasicAuthConnectionMetadata:
    out: BasicAuthConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.base_endpoint required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.username required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.password required")
    return out


def redact_sensitive(value: BasicAuthConnectionMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
