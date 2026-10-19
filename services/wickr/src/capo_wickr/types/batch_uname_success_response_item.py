"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameSuccessResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.uname


class BatchUnameSuccessResponseItem(TypedDict, closed=True):
    uname: "capo_wickr.types.uname.Uname"
    """<p>The username hash that was successfully resolved.</p>"""
    username: "capo_wickr.types.generic_string.GenericString"
    """<p>The email address or username corresponding to the username hash.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameSuccessResponseItem) -> dict:
    out: dict = {}
    out["uname"] = value["uname"]
    out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> BatchUnameSuccessResponseItem:
    out: BatchUnameSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("uname") is not None:
        out["uname"] = data["uname"]
    else:
        out["uname"] = ""
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    return out
