"""Generated from Smithy shape ``com.amazonaws.chime#CreateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.email_address
    import capo_chime.types.non_empty_string
    import capo_chime.types.string
    import capo_chime.types.user_type


class CreateUserRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    username: NotRequired["capo_chime.types.string.String"]
    """<p>The user name.</p>"""
    email: NotRequired["capo_chime.types.email_address.EmailAddress"]
    """<p>The user's email address.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "email" in value:
        out["Email"] = value["email"]
    if "user_type" in value:
        import capo_chime.types.user_type

        out["UserType"] = capo_chime.types.user_type.serialize_json(value["user_type"])
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("UserType") is not None:
        import capo_chime.types.user_type

        out["user_type"] = capo_chime.types.user_type.deserialize_json(data["UserType"])
    return out


def redact_sensitive(value: CreateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
