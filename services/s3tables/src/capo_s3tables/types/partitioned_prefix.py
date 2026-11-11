"""Generated from Smithy shape ``com.amazonaws.s3tables#PartitionedPrefix``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.partition_date_source


class PartitionedPrefix(TypedDict, closed=True):
    partition_date_source: (
        "capo_s3tables.types.partition_date_source.PartitionDateSource"
    )
    """<p>The date to use for the log object key partitions. Valid values are <code>EventTime</code>, the time that the requests in the log were made, and <code>DeliveryTime</code>, the time that the log was delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionedPrefix) -> dict:
    out: dict = {}
    import capo_s3tables.types.partition_date_source

    out["partitionDateSource"] = (
        capo_s3tables.types.partition_date_source.serialize_json(
            value["partition_date_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> PartitionedPrefix:
    out: PartitionedPrefix = {}  # type: ignore[typeddict-item]
    if data.get("partitionDateSource") is not None:
        import capo_s3tables.types.partition_date_source

        out["partition_date_source"] = (
            capo_s3tables.types.partition_date_source.deserialize_json(
                data["partitionDateSource"]
            )
        )
    else:
        import typing

        out["partition_date_source"] = typing.cast(
            "capo_s3tables.types.partition_date_source.PartitionDateSource", ""
        )
    return out
