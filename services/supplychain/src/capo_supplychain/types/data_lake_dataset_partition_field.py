"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_partition_field_transform
    import capo_supplychain.types.data_lake_dataset_schema_field_name


class DataLakeDatasetPartitionField(TypedDict, closed=True):
    name: "capo_supplychain.types.data_lake_dataset_schema_field_name.DataLakeDatasetSchemaFieldName"
    """<p>The name of the partition field.</p>"""
    transform: "capo_supplychain.types.data_lake_dataset_partition_field_transform.DataLakeDatasetPartitionFieldTransform"
    """<p>The transformation of the partition field. A transformation specifies how to partition on a given field. For example, with timestamp you can specify that you'd like to partition fields by day, e.g. data record with value 2025-01-03T00:00:00Z in partition field is in 2025-01-03 partition. Also noted that data record without any value in optional partition field is in NULL partition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPartitionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_supplychain.types.data_lake_dataset_partition_field_transform

    out["transform"] = (
        capo_supplychain.types.data_lake_dataset_partition_field_transform.serialize_json(
            value["transform"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeDatasetPartitionField:
    out: DataLakeDatasetPartitionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("transform") is not None:
        import capo_supplychain.types.data_lake_dataset_partition_field_transform

        out["transform"] = (
            capo_supplychain.types.data_lake_dataset_partition_field_transform.deserialize_json(
                data["transform"]
            )
        )
    else:
        raise DeserializationError("DataLakeDatasetPartitionField.transform required")
    return out
