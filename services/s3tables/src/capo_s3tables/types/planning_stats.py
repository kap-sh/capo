"""Generated from Smithy shape ``com.amazonaws.s3tables#PlanningStats``."""

from typing_extensions import NotRequired, TypedDict


class PlanningStats(TypedDict, closed=True):
    objects_scanned: NotRequired["int"]
    """<p>The number of source objects that the migration found under the source table's location, whether or not it migrates them. The object compatibility report has one row for each.</p>"""
    objects_planned: NotRequired["int"]
    """<p>The number of source objects in the migration. For a start, these are the data files in the Amazon Web Services Glue table's partitions, or under the table's location if the table isn't partitioned. For a sync, these are all the data files of the table after the sync, including files that earlier migrations migrated.</p>"""
    partition_count: NotRequired["int"]
    """<p>The number of partitions in the destination table after this migration, or 0 if the source table isn't partitioned. This value is returned when planning produces a valid plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlanningStats) -> dict:
    out: dict = {}
    if "objects_scanned" in value:
        out["objectsScanned"] = value["objects_scanned"]
    if "objects_planned" in value:
        out["objectsPlanned"] = value["objects_planned"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    return out


def deserialize_json(data: dict) -> PlanningStats:
    out: PlanningStats = {}  # type: ignore[typeddict-item]
    if data.get("objectsScanned") is not None:
        out["objects_scanned"] = data["objectsScanned"]
    if data.get("objectsPlanned") is not None:
        out["objects_planned"] = data["objectsPlanned"]
    if data.get("partitionCount") is not None:
        out["partition_count"] = data["partitionCount"]
    return out
