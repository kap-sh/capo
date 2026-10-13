"""Generated from Smithy shape ``com.amazonaws.glue#BasicAuthenticationCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.password
    import capo_glue.types.username


class BasicAuthenticationCredentials(TypedDict, closed=True):
    username: NotRequired["capo_glue.types.username.Username"]
    """<p>The username to connect to the data source.</p>"""
    password: NotRequired["capo_glue.types.password.Password"]
    """<p>The password to connect to the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BasicAuthenticationCredentials) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BasicAuthenticationCredentials:
    out: BasicAuthenticationCredentials = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: BasicAuthenticationCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
