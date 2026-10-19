"""Generated from Smithy shape ``com.amazonaws.s3files#CreationPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.owner_gid
    import capo_s3files.types.owner_uid
    import capo_s3files.types.permissions


class CreationPermissions(TypedDict, closed=True):
    owner_uid: "capo_s3files.types.owner_uid.OwnerUid"
    """<p>The POSIX user ID to assign to newly created directories.</p>"""
    owner_gid: "capo_s3files.types.owner_gid.OwnerGid"
    """<p>The POSIX group ID to assign to newly created directories.</p>"""
    permissions: "capo_s3files.types.permissions.Permissions"
    """<p>The octal permissions to assign to newly created directories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreationPermissions) -> dict:
    out: dict = {}
    out["ownerUid"] = value["owner_uid"]
    out["ownerGid"] = value["owner_gid"]
    out["permissions"] = value["permissions"]
    return out


def deserialize_json(data: dict) -> CreationPermissions:
    out: CreationPermissions = {}  # type: ignore[typeddict-item]
    if data.get("ownerUid") is not None:
        out["owner_uid"] = data["ownerUid"]
    else:
        out["owner_uid"] = 0
    if data.get("ownerGid") is not None:
        out["owner_gid"] = data["ownerGid"]
    else:
        out["owner_gid"] = 0
    if data.get("permissions") is not None:
        out["permissions"] = data["permissions"]
    else:
        out["permissions"] = ""
    return out
