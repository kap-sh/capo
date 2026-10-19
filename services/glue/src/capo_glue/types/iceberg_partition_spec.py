"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_partition_spec_field_list
    import capo_glue.types.integer


class IcebergPartitionSpec(TypedDict, closed=True):
    fields: "capo_glue.types.iceberg_partition_spec_field_list.IcebergPartitionSpecFieldList"
    """<p>The list of partition fields that define how the table data should be partitioned, including source fields and their transformations.</p>"""
    spec_id: "capo_glue.types.integer.Integer"
    """<p>The unique identifier for this partition specification within the Iceberg table's metadata history.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionSpec) -> dict:
    out: dict = {}
    import capo_glue.types.iceberg_partition_spec_field_list

    out["Fields"] = (
        capo_glue.types.iceberg_partition_spec_field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    )
    out["SpecId"] = value.get("spec_id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergPartitionSpec:
    out: IcebergPartitionSpec = {}  # type: ignore[typeddict-item]
    if data.get("Fields") is not None:
        import capo_glue.types.iceberg_partition_spec_field_list

        out["fields"] = (
            capo_glue.types.iceberg_partition_spec_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        out["fields"] = []
    if data.get("SpecId") is not None:
        out["spec_id"] = data["SpecId"]
    else:
        out["spec_id"] = 0
    return out
