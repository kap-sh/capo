"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteStorageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.storage_profile_id


class DeleteStorageProfileRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm from which to remove the storage profile."""
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """The storage profile ID of the storage profile to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStorageProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStorageProfileRequest:
    out: DeleteStorageProfileRequest = {}  # type: ignore[typeddict-item]
    return out
