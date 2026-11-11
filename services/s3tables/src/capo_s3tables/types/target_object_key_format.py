"""Generated from Smithy shape ``com.amazonaws.s3tables#TargetObjectKeyFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.partitioned_prefix


class TargetObjectKeyFormat(TypedDict, closed=True):
    partitioned_prefix: "capo_s3tables.types.partitioned_prefix.PartitionedPrefix"
    """<p>Partitions log object keys by date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetObjectKeyFormat) -> dict:
    out: dict = {}
    import capo_s3tables.types.partitioned_prefix

    out["partitionedPrefix"] = capo_s3tables.types.partitioned_prefix.serialize_json(
        value["partitioned_prefix"]
    )
    return out


def deserialize_json(data: dict) -> TargetObjectKeyFormat:
    out: TargetObjectKeyFormat = {}  # type: ignore[typeddict-item]
    if data.get("partitionedPrefix") is not None:
        import capo_s3tables.types.partitioned_prefix

        out["partitioned_prefix"] = (
            capo_s3tables.types.partitioned_prefix.deserialize_json(
                data["partitionedPrefix"]
            )
        )
    else:
        raise DeserializationError("TargetObjectKeyFormat.partitioned_prefix required")
    return out
