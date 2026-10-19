"""Generated from Smithy shape ``com.amazonaws.s3files#ListMountTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.mount_targets


class ListMountTargetsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token to use in a subsequent request if more results are available.</p>"""
    mount_targets: "capo_s3files.types.mount_targets.MountTargets"
    """<p>An array of mount target descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMountTargetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_s3files.types.mount_targets

    out["mountTargets"] = capo_s3files.types.mount_targets.serialize_json(
        value["mount_targets"]
    )
    return out


def deserialize_json(data: dict) -> ListMountTargetsResponse:
    out: ListMountTargetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("mountTargets") is not None:
        import capo_s3files.types.mount_targets

        out["mount_targets"] = capo_s3files.types.mount_targets.deserialize_json(
            data["mountTargets"]
        )
    else:
        out["mount_targets"] = []
    return out
