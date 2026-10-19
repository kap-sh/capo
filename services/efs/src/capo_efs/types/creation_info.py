"""Generated from Smithy shape ``com.amazonaws.efs#CreationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.owner_gid
    import capo_efs.types.owner_uid
    import capo_efs.types.permissions


class CreationInfo(TypedDict, closed=True):
    owner_uid: "capo_efs.types.owner_uid.OwnerUid"
    """<p>Specifies the POSIX user ID to apply to the <code>RootDirectory</code>. Accepts values from 0 to 2^32 (4294967295).</p>"""
    owner_gid: "capo_efs.types.owner_gid.OwnerGid"
    """<p>Specifies the POSIX group ID to apply to the <code>RootDirectory</code>. Accepts values from 0 to 2^32 (4294967295).</p>"""
    permissions: "capo_efs.types.permissions.Permissions"
    """<p>Specifies the POSIX permissions to apply to the <code>RootDirectory</code>, in the format of an octal number representing the file's mode bits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreationInfo) -> dict:
    out: dict = {}
    out["OwnerUid"] = value["owner_uid"]
    out["OwnerGid"] = value["owner_gid"]
    out["Permissions"] = value["permissions"]
    return out


def deserialize_json(data: dict) -> CreationInfo:
    out: CreationInfo = {}  # type: ignore[typeddict-item]
    if data.get("OwnerUid") is not None:
        out["owner_uid"] = data["OwnerUid"]
    else:
        out["owner_uid"] = 0
    if data.get("OwnerGid") is not None:
        out["owner_gid"] = data["OwnerGid"]
    else:
        out["owner_gid"] = 0
    if data.get("Permissions") is not None:
        out["permissions"] = data["Permissions"]
    else:
        out["permissions"] = ""
    return out
