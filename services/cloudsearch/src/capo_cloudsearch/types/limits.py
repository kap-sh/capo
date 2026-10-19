"""Generated from Smithy shape ``com.amazonaws.cloudsearch#Limits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.maximum_partition_count
    import capo_cloudsearch.types.maximum_replication_count


class Limits(TypedDict, closed=True):
    maximum_replication_count: (
        "capo_cloudsearch.types.maximum_replication_count.MaximumReplicationCount"
    )
    maximum_partition_count: (
        "capo_cloudsearch.types.maximum_partition_count.MaximumPartitionCount"
    )


# --- awsQuery ser/de ---
def serialize_query(value: Limits, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (
            f"{key_prefix}MaximumReplicationCount",
            str(value["maximum_replication_count"]),
        )
    )
    pairs.append(
        (f"{key_prefix}MaximumPartitionCount", str(value["maximum_partition_count"]))
    )


def deserialize_query(el: Element) -> Limits:
    out: Limits = {}  # type: ignore[typeddict-item]
    child_maximum_replication_count = el.find("MaximumReplicationCount")
    if child_maximum_replication_count is not None:
        out["maximum_replication_count"] = int(
            child_maximum_replication_count.text or ""
        )
    else:
        out["maximum_replication_count"] = 0
    child_maximum_partition_count = el.find("MaximumPartitionCount")
    if child_maximum_partition_count is not None:
        out["maximum_partition_count"] = int(child_maximum_partition_count.text or "")
    else:
        out["maximum_partition_count"] = 0
    return out
