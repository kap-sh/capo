"""Generated from Smithy shape ``com.amazonaws.deadline#StorageProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.resource_name
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.storage_profile_operating_system_family


class StorageProfileSummary(TypedDict, closed=True):
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The operating system (OS) family.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageProfileSummary) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    out["displayName"] = value["display_name"]
    import capo_deadline.types.storage_profile_operating_system_family

    out["osFamily"] = (
        capo_deadline.types.storage_profile_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    return out


def deserialize_json(data: dict) -> StorageProfileSummary:
    out: StorageProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        out["storage_profile_id"] = ""
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
    return out
