"""Generated from Smithy shape ``com.amazonaws.datazone#SsoUserProfileDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.first_name
    import capo_datazone.types.last_name
    import capo_datazone.types.user_profile_name


class SsoUserProfileDetails(TypedDict, closed=True):
    username: NotRequired["capo_datazone.types.user_profile_name.UserProfileName"]
    """<p>The username as part of the SSO user profile detail. </p>"""
    first_name: NotRequired["capo_datazone.types.first_name.FirstName"]
    """<p>The first name as part of the SSO user profile detail.</p>"""
    last_name: NotRequired["capo_datazone.types.last_name.LastName"]
    """<p>The last name as part of the SSO user profile detail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsoUserProfileDetails) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> SsoUserProfileDetails:
    out: SsoUserProfileDetails = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    return out


def redact_sensitive(value: SsoUserProfileDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
