"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateStorageProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.file_system_locations_list
    import capo_deadline.types.resource_name
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.storage_profile_operating_system_family


class UpdateStorageProfileRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """The storage profile ID to update."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: NotRequired[
        "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    ]
    """The OS system to update."""
    file_system_locations_to_add: NotRequired[
        "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """The file system location names to add."""
    file_system_locations_to_remove: NotRequired[
        "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """The file system location names to remove."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStorageProfileRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "os_family" in value:
        import capo_deadline.types.storage_profile_operating_system_family

        out["osFamily"] = (
            capo_deadline.types.storage_profile_operating_system_family.serialize_json(
                value["os_family"]
            )
        )
    if "file_system_locations_to_add" in value:
        import capo_deadline.types.file_system_locations_list

        out["fileSystemLocationsToAdd"] = (
            capo_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations_to_add"]
            )
        )
    if "file_system_locations_to_remove" in value:
        import capo_deadline.types.file_system_locations_list

        out["fileSystemLocationsToRemove"] = (
            capo_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateStorageProfileRequest:
    out: UpdateStorageProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("osFamily") is not None:
        import capo_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            capo_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    if data.get("fileSystemLocationsToAdd") is not None:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations_to_add"] = (
            capo_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocationsToAdd"]
            )
        )
    if data.get("fileSystemLocationsToRemove") is not None:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations_to_remove"] = (
            capo_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocationsToRemove"]
            )
        )
    return out


def redact_sensitive(value: UpdateStorageProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_system_locations_to_add" in value:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations_to_add"] = (
            capo_deadline.types.file_system_locations_list.redact_sensitive(
                value["file_system_locations_to_add"]
            )
        )
    if "file_system_locations_to_remove" in value:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations_to_remove"] = (
            capo_deadline.types.file_system_locations_list.redact_sensitive(
                value["file_system_locations_to_remove"]
            )
        )
    return out
