"""Generated from Smithy shape ``com.amazonaws.deadline#CreateStorageProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.file_system_locations_list
    import capo_deadline.types.resource_name
    import capo_deadline.types.storage_profile_operating_system_family


class CreateStorageProfileRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the storage profile.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The type of operating system (OS) for the storage profile.</p>"""
    file_system_locations: NotRequired[
        "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>File system paths to include in the storage profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStorageProfileRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import capo_deadline.types.storage_profile_operating_system_family

    out["osFamily"] = (
        capo_deadline.types.storage_profile_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    if "file_system_locations" in value:
        import capo_deadline.types.file_system_locations_list

        out["fileSystemLocations"] = (
            capo_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateStorageProfileRequest:
    out: CreateStorageProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("osFamily") is not None:
        import capo_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            capo_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        import typing

        out["os_family"] = typing.cast(
            "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
            "",
        )
    if data.get("fileSystemLocations") is not None:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            capo_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocations"]
            )
        )
    return out


def redact_sensitive(value: CreateStorageProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_system_locations" in value:
        import capo_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            capo_deadline.types.file_system_locations_list.redact_sensitive(
                value["file_system_locations"]
            )
        )
    return out
