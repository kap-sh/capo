"""Generated from Smithy shape ``com.amazonaws.deadline#GetFarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id


class GetFarmRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm."""


# --- restJson1 ser/de ---
def serialize_json(value: GetFarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFarmRequest:
    out: GetFarmRequest = {}  # type: ignore[typeddict-item]
    return out
