"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class ExecuteActionResponse(TypedDict, closed=True):
    action_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteActionResponse) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> ExecuteActionResponse:
    out: ExecuteActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    return out
