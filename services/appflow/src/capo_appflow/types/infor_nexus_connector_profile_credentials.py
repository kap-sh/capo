"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.access_key_id
    import capo_appflow.types.key
    import capo_appflow.types.username


class InforNexusConnectorProfileCredentials(TypedDict, closed=True):
    access_key_id: "capo_appflow.types.access_key_id.AccessKeyId"
    """<p> The Access Key portion of the credentials. </p>"""
    user_id: "capo_appflow.types.username.Username"
    """<p> The identifier for the user. </p>"""
    secret_access_key: "capo_appflow.types.key.Key"
    """<p> The secret key used to sign requests. </p>"""
    datakey: "capo_appflow.types.key.Key"
    """<p> The encryption keys used to encrypt data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["userId"] = value["user_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["datakey"] = value["datakey"]
    return out


def deserialize_json(data: dict) -> InforNexusConnectorProfileCredentials:
    out: InforNexusConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        out["secret_access_key"] = ""
    if data.get("datakey") is not None:
        out["datakey"] = data["datakey"]
    else:
        out["datakey"] = ""
    return out


def redact_sensitive(value: InforNexusConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_key_id" in value:
        out["access_key_id"] = "*** Sensitive Data Redacted ***"
    return out
