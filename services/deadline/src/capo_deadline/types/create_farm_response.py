"""Generated from Smithy shape ``com.amazonaws.deadline#CreateFarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id


class CreateFarmResponse(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFarmResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    return out


def deserialize_json(data: dict) -> CreateFarmResponse:
    out: CreateFarmResponse = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    return out
