"""Generated from Smithy shape ``com.amazonaws.deadline#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string


class PosixUser(TypedDict, closed=True):
    user: "capo_deadline.types.string.String"
    """The name of the POSIX user."""
    group: "capo_deadline.types.string.String"
    """The name of the POSIX user's group."""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["user"] = value["user"]
    out["group"] = value["group"]
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if data.get("user") is not None:
        out["user"] = data["user"]
    else:
        out["user"] = ""
    if data.get("group") is not None:
        out["group"] = data["group"]
    else:
        out["group"] = ""
    return out
