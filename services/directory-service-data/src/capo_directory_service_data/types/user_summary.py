"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UserSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.given_name
    import capo_directory_service_data.types.sid
    import capo_directory_service_data.types.surname
    import capo_directory_service_data.types.user_name


class UserSummary(TypedDict, closed=True):
    sid: "capo_directory_service_data.types.sid.SID"
    """<p> The unique security identifier (SID) of the user.</p>"""
    sam_account_name: "capo_directory_service_data.types.user_name.UserName"
    """<p>The name of the user.</p>"""
    given_name: NotRequired["capo_directory_service_data.types.given_name.GivenName"]
    """<p>The first name of the user. </p>"""
    surname: NotRequired["capo_directory_service_data.types.surname.Surname"]
    """<p>The last name of the user.</p>"""
    enabled: "bool"
    """<p>Indicates whether the user account is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSummary) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> UserSummary:
    out: UserSummary = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    else:
        out["sid"] = ""
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        out["sam_account_name"] = ""
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out


def redact_sensitive(value: UserSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "given_name" in value:
        out["given_name"] = "*** Sensitive Data Redacted ***"
    if "surname" in value:
        out["surname"] = "*** Sensitive Data Redacted ***"
    return out
