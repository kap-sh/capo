"""Generated from Smithy shape ``com.amazonaws.deadline#GetLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id


class GetLimitRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The unique identifier of the farm that contains the limit."""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """The unique identifier of the limit to return."""


# --- restJson1 ser/de ---
def serialize_json(value: GetLimitRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLimitRequest:
    out: GetLimitRequest = {}  # type: ignore[typeddict-item]
    return out
