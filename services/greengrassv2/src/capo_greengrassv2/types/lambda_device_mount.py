"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaDeviceMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.file_system_path
    import capo_greengrassv2.types.lambda_filesystem_permission
    import capo_greengrassv2.types.optional_boolean


class LambdaDeviceMount(TypedDict, closed=True):
    path: "capo_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The mount path for the device in the file system.</p>"""
    permission: NotRequired[
        "capo_greengrassv2.types.lambda_filesystem_permission.LambdaFilesystemPermission"
    ]
    """<p>The permission to access the device: read/only (<code>ro</code>) or read/write (<code>rw</code>).</p> <p>Default: <code>ro</code> </p>"""
    add_group_owner: NotRequired[
        "capo_greengrassv2.types.optional_boolean.OptionalBoolean"
    ]
    """<p>Whether or not to add the component's system user as an owner of the device.</p> <p>Default: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDeviceMount) -> dict:
    out: dict = {}
    out["path"] = value["path"]
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


def deserialize_json(data: dict) -> LambdaDeviceMount:
    out: LambdaDeviceMount = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
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
