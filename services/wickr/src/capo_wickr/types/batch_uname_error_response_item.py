"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameErrorResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.uname


class BatchUnameErrorResponseItem(TypedDict, closed=True):
    field: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The field that caused the error.</p>"""
    reason: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A description of why the username hash lookup failed.</p>"""
    uname: "capo_wickr.types.uname.Uname"
    """<p>The username hash that failed to be looked up.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameErrorResponseItem) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    out["uname"] = value["uname"]
    return out


def deserialize_json(data: dict) -> BatchUnameErrorResponseItem:
    out: BatchUnameErrorResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("uname") is not None:
        out["uname"] = data["uname"]
    else:
        out["uname"] = ""
    return out
