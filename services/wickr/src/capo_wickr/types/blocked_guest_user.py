"""Generated from Smithy shape ``com.amazonaws.wickr#BlockedGuestUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class BlockedGuestUser(TypedDict, closed=True):
    username: "capo_wickr.types.generic_string.GenericString"
    """<p>The username of the blocked guest user.</p>"""
    admin: "capo_wickr.types.generic_string.GenericString"
    """<p>The username of the administrator who blocked this guest user.</p>"""
    modified: "capo_wickr.types.generic_string.GenericString"
    """<p>The timestamp when the guest user was blocked or last modified.</p>"""
    username_hash: "capo_wickr.types.generic_string.GenericString"
    """<p>The unique username hash identifier for the blocked guest user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockedGuestUser) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["admin"] = value["admin"]
    out["modified"] = value["modified"]
    out["usernameHash"] = value["username_hash"]
    return out


def deserialize_json(data: dict) -> BlockedGuestUser:
    out: BlockedGuestUser = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("admin") is not None:
        out["admin"] = data["admin"]
    else:
        out["admin"] = ""
    if data.get("modified") is not None:
        out["modified"] = data["modified"]
    else:
        out["modified"] = ""
    if data.get("usernameHash") is not None:
        out["username_hash"] = data["usernameHash"]
    else:
        out["username_hash"] = ""
    return out
