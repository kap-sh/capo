"""Generated from Smithy shape ``com.amazonaws.directoryservice#ResetUserPasswordRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.customer_user_name
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.user_password


class ResetUserPasswordRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the Managed Microsoft AD or Simple AD directory in which the user resides.</p>"""
    user_name: "capo_directory_service.types.customer_user_name.CustomerUserName"
    """<p>The user name of the user whose password will be reset.</p>"""
    new_password: "capo_directory_service.types.user_password.UserPassword"
    """<p>The new password that will be reset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetUserPasswordRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["UserName"] = value["user_name"]
    out["NewPassword"] = value["new_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetUserPasswordRequest:
    out: ResetUserPasswordRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    if data.get("NewPassword") is not None:
        out["new_password"] = data["NewPassword"]
    else:
        out["new_password"] = ""
    return out


def redact_sensitive(value: ResetUserPasswordRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "new_password" in value:
        out["new_password"] = "*** Sensitive Data Redacted ***"
    return out
