"""Generated from Smithy shape ``com.amazonaws.s3files#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.gid
    import capo_s3files.types.secondary_gids
    import capo_s3files.types.uid


class PosixUser(TypedDict, closed=True):
    uid: "capo_s3files.types.uid.Uid"
    """<p>The POSIX user ID.</p>"""
    gid: "capo_s3files.types.gid.Gid"
    """<p>The POSIX group ID.</p>"""
    secondary_gids: NotRequired["capo_s3files.types.secondary_gids.SecondaryGids"]
    """<p>An array of secondary POSIX group IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["uid"] = value["uid"]
    out["gid"] = value["gid"]
    if "secondary_gids" in value:
        import capo_s3files.types.secondary_gids

        out["secondaryGids"] = capo_s3files.types.secondary_gids.serialize_json(
            value["secondary_gids"]
        )
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    else:
        out["uid"] = 0
    if data.get("gid") is not None:
        out["gid"] = data["gid"]
    else:
        out["gid"] = 0
    if data.get("secondaryGids") is not None:
        import capo_s3files.types.secondary_gids

        out["secondary_gids"] = capo_s3files.types.secondary_gids.deserialize_json(
            data["secondaryGids"]
        )
    return out
