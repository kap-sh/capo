"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserSuccessResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.user_id


class BatchUserSuccessResponseItem(TypedDict, closed=True):
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The user ID that was successfully processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserSuccessResponseItem) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> BatchUserSuccessResponseItem:
    out: BatchUserSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
