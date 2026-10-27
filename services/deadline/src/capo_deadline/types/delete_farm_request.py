"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteFarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id


class DeleteFarmRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFarmRequest:
    out: DeleteFarmRequest = {}  # type: ignore[typeddict-item]
    return out
