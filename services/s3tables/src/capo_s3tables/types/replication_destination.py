"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn


class ReplicationDestination(TypedDict, closed=True):
    destination_table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the destination table bucket where tables will be replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDestination) -> dict:
    out: dict = {}
    out["destinationTableBucketARN"] = value["destination_table_bucket_arn"]
    return out


def deserialize_json(data: dict) -> ReplicationDestination:
    out: ReplicationDestination = {}  # type: ignore[typeddict-item]
    if data.get("destinationTableBucketARN") is not None:
        out["destination_table_bucket_arn"] = data["destinationTableBucketARN"]
    else:
        out["destination_table_bucket_arn"] = ""
    return out
