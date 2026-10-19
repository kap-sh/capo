"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaVolumeMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.file_system_path
    import capo_greengrassv2.types.lambda_filesystem_permission
    import capo_greengrassv2.types.optional_boolean


class LambdaVolumeMount(TypedDict, closed=True):
    source_path: "capo_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The path to the physical volume in the file system.</p>"""
    destination_path: "capo_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The path to the logical volume in the file system.</p>"""
    permission: NotRequired[
        "capo_greengrassv2.types.lambda_filesystem_permission.LambdaFilesystemPermission"
    ]
    """<p>The permission to access the volume: read/only (<code>ro</code>) or read/write (<code>rw</code>).</p> <p>Default: <code>ro</code> </p>"""
    add_group_owner: NotRequired[
        "capo_greengrassv2.types.optional_boolean.OptionalBoolean"
    ]
    """<p>Whether or not to add the IoT Greengrass user group as an owner of the volume.</p> <p>Default: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaVolumeMount) -> dict:
    out: dict = {}
    out["sourcePath"] = value["source_path"]
    out["destinationPath"] = value["destination_path"]
    if "permission" in value:
        import capo_greengrassv2.types.lambda_filesystem_permission

        out["permission"] = (
            capo_greengrassv2.types.lambda_filesystem_permission.serialize_json(
                value["permission"]
            )
        )
    if "add_group_owner" in value:
        out["addGroupOwner"] = value["add_group_owner"]
    return out


def deserialize_json(data: dict) -> LambdaVolumeMount:
    out: LambdaVolumeMount = {}  # type: ignore[typeddict-item]
    if data.get("sourcePath") is not None:
        out["source_path"] = data["sourcePath"]
    else:
        out["source_path"] = ""
    if data.get("destinationPath") is not None:
        out["destination_path"] = data["destinationPath"]
    else:
        out["destination_path"] = ""
    if data.get("permission") is not None:
        import capo_greengrassv2.types.lambda_filesystem_permission

        out["permission"] = (
            capo_greengrassv2.types.lambda_filesystem_permission.deserialize_json(
                data["permission"]
            )
        )
    if data.get("addGroupOwner") is not None:
        out["add_group_owner"] = data["addGroupOwner"]
    return out
