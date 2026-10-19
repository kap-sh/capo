"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateDirectorySetupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.create_snapshot_before_update
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_size_update_settings
    import capo_directory_service.types.network_update_settings
    import capo_directory_service.types.os_update_settings
    import capo_directory_service.types.update_type


class UpdateDirectorySetupRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory to update.</p>"""
    update_type: "capo_directory_service.types.update_type.UpdateType"
    """<p>The type of update to perform on the directory.</p>"""
    os_update_settings: NotRequired[
        "capo_directory_service.types.os_update_settings.OSUpdateSettings"
    ]
    """<p>Operating system configuration to apply during the directory update operation.</p>"""
    directory_size_update_settings: NotRequired[
        "capo_directory_service.types.directory_size_update_settings.DirectorySizeUpdateSettings"
    ]
    """<p>Directory size configuration to apply during the update operation.</p>"""
    network_update_settings: NotRequired[
        "capo_directory_service.types.network_update_settings.NetworkUpdateSettings"
    ]
    """<p>Network configuration to apply during the directory update operation.</p>"""
    create_snapshot_before_update: NotRequired[
        "capo_directory_service.types.create_snapshot_before_update.CreateSnapshotBeforeUpdate"
    ]
    """<p>Specifies whether to create a directory snapshot before performing the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectorySetupRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.update_type

    out["UpdateType"] = capo_directory_service.types.update_type.serialize_aws_json_1_1(
        value["update_type"]
    )
    if "os_update_settings" in value:
        import capo_directory_service.types.os_update_settings

        out["OSUpdateSettings"] = (
            capo_directory_service.types.os_update_settings.serialize_aws_json_1_1(
                value["os_update_settings"]
            )
        )
    if "directory_size_update_settings" in value:
        import capo_directory_service.types.directory_size_update_settings

        out["DirectorySizeUpdateSettings"] = (
            capo_directory_service.types.directory_size_update_settings.serialize_aws_json_1_1(
                value["directory_size_update_settings"]
            )
        )
    if "network_update_settings" in value:
        import capo_directory_service.types.network_update_settings

        out["NetworkUpdateSettings"] = (
            capo_directory_service.types.network_update_settings.serialize_aws_json_1_1(
                value["network_update_settings"]
            )
        )
    if "create_snapshot_before_update" in value:
        out["CreateSnapshotBeforeUpdate"] = value["create_snapshot_before_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectorySetupRequest:
    out: UpdateDirectorySetupRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("UpdateType") is not None:
        import capo_directory_service.types.update_type

        out["update_type"] = (
            capo_directory_service.types.update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    else:
        import typing

        out["update_type"] = typing.cast(
            "capo_directory_service.types.update_type.UpdateType", ""
        )
    if data.get("OSUpdateSettings") is not None:
        import capo_directory_service.types.os_update_settings

        out["os_update_settings"] = (
            capo_directory_service.types.os_update_settings.deserialize_aws_json_1_1(
                data["OSUpdateSettings"]
            )
        )
    if data.get("DirectorySizeUpdateSettings") is not None:
        import capo_directory_service.types.directory_size_update_settings

        out["directory_size_update_settings"] = (
            capo_directory_service.types.directory_size_update_settings.deserialize_aws_json_1_1(
                data["DirectorySizeUpdateSettings"]
            )
        )
    if data.get("NetworkUpdateSettings") is not None:
        import capo_directory_service.types.network_update_settings

        out["network_update_settings"] = (
            capo_directory_service.types.network_update_settings.deserialize_aws_json_1_1(
                data["NetworkUpdateSettings"]
            )
        )
    if data.get("CreateSnapshotBeforeUpdate") is not None:
        out["create_snapshot_before_update"] = data["CreateSnapshotBeforeUpdate"]
    return out
