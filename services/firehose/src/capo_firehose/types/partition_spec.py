"""Generated from Smithy shape ``com.amazonaws.firehose#PartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.partition_fields


class PartitionSpec(TypedDict, closed=True):
    identity: NotRequired["capo_firehose.types.partition_fields.PartitionFields"]
    """<p> List of identity <a href="https://iceberg.apache.org/spec/#partition-transforms">transforms</a> that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionSpec) -> dict:
    out: dict = {}
    if "identity" in value:
        import capo_firehose.types.partition_fields

        out["Identity"] = capo_firehose.types.partition_fields.serialize_aws_json_1_1(
            value["identity"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionSpec:
    out: PartitionSpec = {}  # type: ignore[typeddict-item]
    if data.get("Identity") is not None:
        import capo_firehose.types.partition_fields

        out["identity"] = capo_firehose.types.partition_fields.deserialize_aws_json_1_1(
            data["Identity"]
        )
    return out
