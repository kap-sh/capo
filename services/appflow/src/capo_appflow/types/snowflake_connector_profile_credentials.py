"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.private_key
    import capo_appflow.types.username


class SnowflakeConnectorProfileCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The name of the user. </p>"""
    password: NotRequired["capo_appflow.types.password.Password"]
    """<p> The password that corresponds to the user name. </p>"""
    private_key: NotRequired["capo_appflow.types.private_key.PrivateKey"]
    """<p> The RSA private key used for key pair authentication with Snowflake. Provide this instead of a password when your Snowflake account uses key pair authentication. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    if "private_key" in value:
        out["privateKey"] = value["private_key"]
    return out


def deserialize_json(data: dict) -> SnowflakeConnectorProfileCredentials:
    out: SnowflakeConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("password") is not None:
        out["password"] = data["password"]
    if data.get("privateKey") is not None:
        out["private_key"] = data["privateKey"]
    return out


def redact_sensitive(value: SnowflakeConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    if "private_key" in value:
        out["private_key"] = "*** Sensitive Data Redacted ***"
    return out
