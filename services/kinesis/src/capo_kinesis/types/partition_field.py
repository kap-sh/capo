"""Generated from Smithy shape ``com.amazonaws.kinesis#PartitionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.partition_source_name
    import capo_kinesis.types.partition_transform


class PartitionField(TypedDict, closed=True):
    transform: "capo_kinesis.types.partition_transform.PartitionTransform"
    """<p>The partition transform to apply. The only valid value is <code>TIME_HOUR</code>.</p>"""
    source_name: "capo_kinesis.types.partition_source_name.PartitionSourceName"
    """<p>The name of the source column used for partitioning. This column must be of the <code>timestamptz</code> type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionField) -> dict:
    out: dict = {}
    import capo_kinesis.types.partition_transform

    out["Transform"] = capo_kinesis.types.partition_transform.serialize_aws_json_1_1(
        value["transform"]
    )
    out["SourceName"] = value["source_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionField:
    out: PartitionField = {}  # type: ignore[typeddict-item]
    if data.get("Transform") is not None:
        import capo_kinesis.types.partition_transform

        out["transform"] = (
            capo_kinesis.types.partition_transform.deserialize_aws_json_1_1(
                data["Transform"]
            )
        )
    else:
        import typing

        out["transform"] = typing.cast(
            "capo_kinesis.types.partition_transform.PartitionTransform", ""
        )
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    else:
        out["source_name"] = ""
    return out
