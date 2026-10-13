"""Generated from Smithy shape ``com.amazonaws.finspacedata#ResetUserPasswordResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.password
    import capo_finspace_data.types.user_id


class ResetUserPasswordResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier of the user that a new password is generated for.</p>"""
    temporary_password: NotRequired["capo_finspace_data.types.password.Password"]
    """<p>A randomly generated temporary password for the requested user. This password expires in 7 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetUserPasswordResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "temporary_password" in value:
        out["temporaryPassword"] = value["temporary_password"]
    return out


def deserialize_json(data: dict) -> ResetUserPasswordResponse:
    out: ResetUserPasswordResponse = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("temporaryPassword") is not None:
        out["temporary_password"] = data["temporaryPassword"]
    return out


def redact_sensitive(value: ResetUserPasswordResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "temporary_password" in value:
        out["temporary_password"] = "*** Sensitive Data Redacted ***"
    return out
