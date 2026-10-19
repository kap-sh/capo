"""Generated from Smithy shape ``com.amazonaws.m2#EfsStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.string200


class EfsStorageConfiguration(TypedDict, closed=True):
    file_system_id: "capo_m2.types.string200.String200"
    """<p>The file system identifier.</p>"""
    mount_point: "capo_m2.types.string200.String200"
    """<p>The mount point for the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EfsStorageConfiguration) -> dict:
    out: dict = {}
    out["file-system-id"] = value["file_system_id"]
    out["mount-point"] = value["mount_point"]
    return out


def deserialize_json(data: dict) -> EfsStorageConfiguration:
    out: EfsStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("file-system-id") is not None:
        out["file_system_id"] = data["file-system-id"]
    else:
        out["file_system_id"] = ""
    if data.get("mount-point") is not None:
        out["mount_point"] = data["mount-point"]
    else:
        out["mount_point"] = ""
    return out
