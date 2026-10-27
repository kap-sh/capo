"""Generated from Smithy shape ``com.amazonaws.deadline#WindowsUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string


class WindowsUser(TypedDict, closed=True):
    user: "capo_deadline.types.string.String"
    """The user."""
    password_arn: "capo_deadline.types.string.String"
    """The password ARN for the Windows user."""


# --- restJson1 ser/de ---
def serialize_json(value: WindowsUser) -> dict:
    out: dict = {}
    out["user"] = value["user"]
    out["passwordArn"] = value["password_arn"]
    return out


def deserialize_json(data: dict) -> WindowsUser:
    out: WindowsUser = {}  # type: ignore[typeddict-item]
    if data.get("user") is not None:
        out["user"] = data["user"]
    else:
        out["user"] = ""
    if data.get("passwordArn") is not None:
        out["password_arn"] = data["passwordArn"]
    else:
        out["password_arn"] = ""
    return out
