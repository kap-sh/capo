"""Generated from Smithy shape ``com.amazonaws.backup#BackupAccessPoints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.list_access_points_member

BackupAccessPoints: TypeAlias = list[
    "capo_backup.types.list_access_points_member.ListAccessPointsMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupAccessPoints) -> list:
    import capo_backup.types.list_access_points_member

    out: list = []
    for item in value:
        out.append(capo_backup.types.list_access_points_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupAccessPoints:
    import capo_backup.types.list_access_points_member

    out: BackupAccessPoints = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup.types.list_access_points_member.deserialize_json(item))
    return out


def redact_sensitive(value: BackupAccessPoints) -> list[Any]:
    import capo_backup.types.list_access_points_member

    return [
        capo_backup.types.list_access_points_member.redact_sensitive(item)
        for item in value
    ]
