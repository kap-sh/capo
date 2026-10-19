"""Generated from Smithy shape ``com.amazonaws.efs#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.gid
    import capo_efs.types.secondary_gids
    import capo_efs.types.uid


class PosixUser(TypedDict, closed=True):
    uid: "capo_efs.types.uid.Uid"
    """<p>The POSIX user ID used for all file system operations using this access point.</p>"""
    gid: "capo_efs.types.gid.Gid"
    """<p>The POSIX group ID used for all file system operations using this access point.</p>"""
    secondary_gids: NotRequired["capo_efs.types.secondary_gids.SecondaryGids"]
    """<p>Secondary POSIX group IDs used for all file system operations using this access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["Uid"] = value["uid"]
    out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import capo_efs.types.secondary_gids

        out["SecondaryGids"] = capo_efs.types.secondary_gids.serialize_json(
            value["secondary_gids"]
        )
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    else:
        out["uid"] = 0
    if data.get("Gid") is not None:
        out["gid"] = data["Gid"]
    else:
        out["gid"] = 0
    if data.get("SecondaryGids") is not None:
        import capo_efs.types.secondary_gids

        out["secondary_gids"] = capo_efs.types.secondary_gids.deserialize_json(
            data["SecondaryGids"]
        )
    return out
