"""Generated from Smithy shape ``com.amazonaws.datazone#UserDetails``."""

from typing_extensions import TypedDict


class UserDetails(TypedDict, closed=True):
    user_id: "str"
    """<p>The identifier of the Amazon DataZone user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDetails) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserDetails:
    out: UserDetails = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
