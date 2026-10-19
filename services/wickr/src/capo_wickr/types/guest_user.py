"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class GuestUser(TypedDict, closed=True):
    billing_period: "capo_wickr.types.generic_string.GenericString"
    """<p>The billing period when this guest user accessed the network (e.g., '2024-01').</p>"""
    username: "capo_wickr.types.generic_string.GenericString"
    """<p>The username of the guest user.</p>"""
    username_hash: "capo_wickr.types.generic_string.GenericString"
    """<p>The unique username hash identifier for the guest user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuestUser) -> dict:
    out: dict = {}
    out["billingPeriod"] = value["billing_period"]
    out["username"] = value["username"]
    out["usernameHash"] = value["username_hash"]
    return out


def deserialize_json(data: dict) -> GuestUser:
    out: GuestUser = {}  # type: ignore[typeddict-item]
    if data.get("billingPeriod") is not None:
        out["billing_period"] = data["billingPeriod"]
    else:
        out["billing_period"] = ""
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("usernameHash") is not None:
        out["username_hash"] = data["usernameHash"]
    else:
        out["username_hash"] = ""
    return out
