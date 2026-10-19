"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.bounded_partition_value_list
    import capo_glue.types.partition_input


class BatchUpdatePartitionRequestEntry(TypedDict, closed=True):
    partition_value_list: (
        "capo_glue.types.bounded_partition_value_list.BoundedPartitionValueList"
    )
    """<p>A list of values defining the partitions.</p>"""
    partition_input: "capo_glue.types.partition_input.PartitionInput"
    """<p>The structure used to update a partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionRequestEntry) -> dict:
    out: dict = {}
    import capo_glue.types.bounded_partition_value_list

    out["PartitionValueList"] = (
        capo_glue.types.bounded_partition_value_list.serialize_aws_json_1_1(
            value["partition_value_list"]
        )
    )
    import capo_glue.types.partition_input

    out["PartitionInput"] = capo_glue.types.partition_input.serialize_aws_json_1_1(
        value["partition_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionRequestEntry:
    out: BatchUpdatePartitionRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("PartitionValueList") is not None:
        import capo_glue.types.bounded_partition_value_list

        out["partition_value_list"] = (
            capo_glue.types.bounded_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionValueList"]
            )
        )
    else:
        out["partition_value_list"] = []
    if data.get("PartitionInput") is not None:
        import capo_glue.types.partition_input

        out["partition_input"] = (
            capo_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdatePartitionRequestEntry.partition_input required"
        )
    return out
