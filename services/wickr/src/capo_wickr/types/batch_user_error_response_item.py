"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserErrorResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.user_id


class BatchUserErrorResponseItem(TypedDict, closed=True):
    field: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The field that caused the error.</p>"""
    reason: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A description of why the user operation failed.</p>"""
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The user ID associated with the failed operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserErrorResponseItem) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> BatchUserErrorResponseItem:
    out: BatchUserErrorResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
