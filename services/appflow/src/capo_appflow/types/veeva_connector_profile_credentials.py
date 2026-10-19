"""Generated from Smithy shape ``com.amazonaws.appflow#VeevaConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.username


class VeevaConnectorProfileCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The name of the user. </p>"""
    password: "capo_appflow.types.password.Password"
    """<p> The password that corresponds to the user name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VeevaConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> VeevaConnectorProfileCredentials:
    out: VeevaConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("password") is not None:
        out["password"] = data["password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(value: VeevaConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
