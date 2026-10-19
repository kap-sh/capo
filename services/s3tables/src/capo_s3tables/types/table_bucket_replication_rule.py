"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketReplicationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.replication_destinations


class TableBucketReplicationRule(TypedDict, closed=True):
    destinations: "capo_s3tables.types.replication_destinations.ReplicationDestinations"
    """<p>An array of destination table buckets where tables should be replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketReplicationRule) -> dict:
    out: dict = {}
    import capo_s3tables.types.replication_destinations

    out["destinations"] = capo_s3tables.types.replication_destinations.serialize_json(
        value["destinations"]
    )
    return out


def deserialize_json(data: dict) -> TableBucketReplicationRule:
    out: TableBucketReplicationRule = {}  # type: ignore[typeddict-item]
    if data.get("destinations") is not None:
        import capo_s3tables.types.replication_destinations

        out["destinations"] = (
            capo_s3tables.types.replication_destinations.deserialize_json(
                data["destinations"]
            )
        )
    else:
        out["destinations"] = []
    return out
