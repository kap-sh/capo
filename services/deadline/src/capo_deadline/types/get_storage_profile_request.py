"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.storage_profile_id


class GetStorageProfileRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the storage profile."""
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """The storage profile ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStorageProfileRequest:
    out: GetStorageProfileRequest = {}  # type: ignore[typeddict-item]
    return out
