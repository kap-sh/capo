"""Generated from Smithy shape ``com.amazonaws.connectscheduling#CreateTimeOffResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.time_off_id


class CreateTimeOffResponse(TypedDict, closed=True):
    time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId"
    """<p>The identifier of the time off request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTimeOffResponse) -> dict:
    out: dict = {}
    out["TimeOffId"] = value["time_off_id"]
    return out


def deserialize_json(data: dict) -> CreateTimeOffResponse:
    out: CreateTimeOffResponse = {}  # type: ignore[typeddict-item]
    if data.get("TimeOffId") is not None:
        out["time_off_id"] = data["TimeOffId"]
    else:
        out["time_off_id"] = ""
    return out
