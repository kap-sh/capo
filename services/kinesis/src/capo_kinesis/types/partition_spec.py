"""Generated from Smithy shape ``com.amazonaws.kinesis#PartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.partition_field_list


class PartitionSpec(TypedDict, closed=True):
    partition_fields: "capo_kinesis.types.partition_field_list.PartitionFieldList"
    """<p>The list of partition fields.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionSpec) -> dict:
    out: dict = {}
    import capo_kinesis.types.partition_field_list

    out["PartitionFields"] = (
        capo_kinesis.types.partition_field_list.serialize_aws_json_1_1(
            value["partition_fields"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionSpec:
    out: PartitionSpec = {}  # type: ignore[typeddict-item]
    if data.get("PartitionFields") is not None:
        import capo_kinesis.types.partition_field_list

        out["partition_fields"] = (
            capo_kinesis.types.partition_field_list.deserialize_aws_json_1_1(
                data["PartitionFields"]
            )
        )
    else:
        out["partition_fields"] = []
    return out
