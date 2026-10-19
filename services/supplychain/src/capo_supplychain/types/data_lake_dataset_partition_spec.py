"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_partition_field_list


class DataLakeDatasetPartitionSpec(TypedDict, closed=True):
    fields: "capo_supplychain.types.data_lake_dataset_partition_field_list.DataLakeDatasetPartitionFieldList"
    """<p>The fields on which to partition a dataset. The partitions will be applied hierarchically based on the order of this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPartitionSpec) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_lake_dataset_partition_field_list

    out["fields"] = (
        capo_supplychain.types.data_lake_dataset_partition_field_list.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeDatasetPartitionSpec:
    out: DataLakeDatasetPartitionSpec = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_supplychain.types.data_lake_dataset_partition_field_list

        out["fields"] = (
            capo_supplychain.types.data_lake_dataset_partition_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    return out
