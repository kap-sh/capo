"""Generated from Smithy shape ``com.amazonaws.deadline#CreateStorageProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.storage_profile_id


class CreateStorageProfileResponse(TypedDict, closed=True):
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """The storage profile ID."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStorageProfileResponse) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    return out


def deserialize_json(data: dict) -> CreateStorageProfileResponse:
    out: CreateStorageProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        out["storage_profile_id"] = ""
    return out
