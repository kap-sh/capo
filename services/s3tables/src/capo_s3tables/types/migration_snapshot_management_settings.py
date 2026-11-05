"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationSnapshotManagementSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_min_snapshots_to_keep
    import capo_s3tables.types.positive_integer


class MigrationSnapshotManagementSettings(TypedDict, closed=True):
    min_snapshots_to_keep: "capo_s3tables.types.migration_min_snapshots_to_keep.MigrationMinSnapshotsToKeep"
    """<p>The minimum number of snapshots to keep. The value must be 3 or more. The default is 3.</p>"""
    max_snapshot_age_hours: "capo_s3tables.types.positive_integer.PositiveInteger"
    """<p>The maximum age, in hours, of a snapshot before it can be expired. The default is 120.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSnapshotManagementSettings) -> dict:
    out: dict = {}
    out["minSnapshotsToKeep"] = value.get("min_snapshots_to_keep", 3)
    out["maxSnapshotAgeHours"] = value.get("max_snapshot_age_hours", 120)
    return out


def deserialize_json(data: dict) -> MigrationSnapshotManagementSettings:
    out: MigrationSnapshotManagementSettings = {}  # type: ignore[typeddict-item]
    if data.get("minSnapshotsToKeep") is not None:
        out["min_snapshots_to_keep"] = data["minSnapshotsToKeep"]
    else:
        out["min_snapshots_to_keep"] = 3
    if data.get("maxSnapshotAgeHours") is not None:
        out["max_snapshot_age_hours"] = data["maxSnapshotAgeHours"]
    else:
        out["max_snapshot_age_hours"] = 120
    return out
