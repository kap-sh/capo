"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.limit_id


class CreateLimitResponse(TypedDict, closed=True):
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>A unique identifier for the limit. Use this identifier in other operations, such as <code>CreateQueueLimitAssociation</code> and <code>DeleteLimit</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLimitResponse) -> dict:
    out: dict = {}
    out["limitId"] = value["limit_id"]
    return out


def deserialize_json(data: dict) -> CreateLimitResponse:
    out: CreateLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("limitId") is not None:
        out["limit_id"] = data["limitId"]
    else:
        out["limit_id"] = ""
    return out
