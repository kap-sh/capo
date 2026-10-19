"""Generated from Smithy shape ``com.amazonaws.appflow#BasicAuthCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.username


class BasicAuthCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The username to use to connect to a resource. </p>"""
    password: "capo_appflow.types.password.Password"
    """<p> The password to use to connect to a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> BasicAuthCredentials:
    out: BasicAuthCredentials = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("password") is not None:
        out["password"] = data["password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(value: BasicAuthCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
