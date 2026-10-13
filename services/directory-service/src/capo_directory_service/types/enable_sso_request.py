"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableSsoRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.connect_password
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.user_name


class EnableSsoRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to enable single-sign on.</p>"""
    user_name: NotRequired["capo_directory_service.types.user_name.UserName"]
    """<p>The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.</p> <p>If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the <i>UserName</i> and <i>Password</i> parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.</p>"""
    password: NotRequired[
        "capo_directory_service.types.connect_password.ConnectPassword"
    ]
    """<p>The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the <i>UserName</i> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableSsoRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableSsoRequest:
    out: EnableSsoRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("EnableSsoRequest.directory_id required")
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: EnableSsoRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
