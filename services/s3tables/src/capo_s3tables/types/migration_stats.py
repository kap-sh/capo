"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationStats``."""

from typing_extensions import NotRequired, TypedDict


class MigrationStats(TypedDict, closed=True):
    objects_migrated: NotRequired["int"]
    """<p>The number of source objects whose data the migration wrote to the destination table. Migrated data can be queried after the migration commits it. If the migration fails or is cancelled, some migrated objects might not be committed.</p>"""
    objects_failed_migration: NotRequired["int"]
    """<p>The number of source objects that didn't migrate, because they failed or because another object, such as an object in the same partition, failed. The object migration report lists the cause for each object.</p>"""
    objects_pending_migration: NotRequired["int"]
    """<p>The number of source objects that haven't migrated or failed yet. When a migration fails or is cancelled, these are the objects that it didn't migrate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationStats) -> dict:
    out: dict = {}
    if "objects_migrated" in value:
        out["objectsMigrated"] = value["objects_migrated"]
    if "objects_failed_migration" in value:
        out["objectsFailedMigration"] = value["objects_failed_migration"]
    if "objects_pending_migration" in value:
        out["objectsPendingMigration"] = value["objects_pending_migration"]
    return out


def deserialize_json(data: dict) -> MigrationStats:
    out: MigrationStats = {}  # type: ignore[typeddict-item]
    if data.get("objectsMigrated") is not None:
        out["objects_migrated"] = data["objectsMigrated"]
    if data.get("objectsFailedMigration") is not None:
        out["objects_failed_migration"] = data["objectsFailedMigration"]
    if data.get("objectsPendingMigration") is not None:
        out["objects_pending_migration"] = data["objectsPendingMigration"]
    return out
