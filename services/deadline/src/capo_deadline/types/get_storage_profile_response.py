"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.file_system_locations_list
    import capo_deadline.types.resource_name
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.storage_profile_operating_system_family
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetStorageProfileResponse(TypedDict, closed=True):
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The operating system (OS) for the storage profile.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    file_system_locations: NotRequired[
        "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>The location of the files for the storage profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileResponse) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    out["displayName"] = value["display_name"]
    import capo_deadline.types.storage_profile_operating_system_family

    out["osFamily"] = (
        capo_deadline.types.storage_profile_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "file_system_locations" in value:
        import capo_deadline.types.file_system_locations_list

        out["fileSystemLocations"] = (
            capo_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetStorageProfileResponse:
    out: GetStorageProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        raise DeserializationError(
            "GetStorageProfileResponse.storage_profile_id required"
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GetStorageProfileResponse.display_name required")
    if data.get("osFamily") is not None:
        import capo_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            capo_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        raise DeserializationError("GetStorageProfileResponse.os_family required")
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetStorageProfileResponse.created_at required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetStorageProfileResponse.created_by required")
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("fileSystemLocations") is not None:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            capo_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocations"]
            )
        )
    return out


def redact_sensitive(value: GetStorageProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_system_locations" in value:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            capo_deadline.types.file_system_locations_list.redact_sensitive(
                value["file_system_locations"]
            )
        )
    return out
