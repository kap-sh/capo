"""Generated from Smithy shape ``com.amazonaws.securityagent#UserMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.sensitive_email


class UserMetadata(TypedDict, closed=True):
    username: "str"
    """<p>The username of the user.</p>"""
    email: "capo_securityagent.types.sensitive_email.SensitiveEmail"
    """<p>The email address of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadata) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> UserMetadata:
    out: UserMetadata = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        out["email"] = ""
    return out
