"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_schema_field_name
    import capo_supplychain.types.data_lake_dataset_schema_field_type


class DataLakeDatasetSchemaField(TypedDict, closed=True):
    name: "capo_supplychain.types.data_lake_dataset_schema_field_name.DataLakeDatasetSchemaFieldName"
    """<p>The dataset field name.</p>"""
    type: "capo_supplychain.types.data_lake_dataset_schema_field_type.DataLakeDatasetSchemaFieldType"
    """<p>The dataset field type.</p>"""
    is_required: "bool"
    """<p>Indicate if the field is required or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchemaField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_supplychain.types.data_lake_dataset_schema_field_type

    out["type"] = (
        capo_supplychain.types.data_lake_dataset_schema_field_type.serialize_json(
            value["type"]
        )
    )
    out["isRequired"] = value["is_required"]
    return out


def deserialize_json(data: dict) -> DataLakeDatasetSchemaField:
    out: DataLakeDatasetSchemaField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_supplychain.types.data_lake_dataset_schema_field_type

        out["type"] = (
            capo_supplychain.types.data_lake_dataset_schema_field_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_supplychain.types.data_lake_dataset_schema_field_type.DataLakeDatasetSchemaFieldType",
            "",
        )
    if data.get("isRequired") is not None:
        out["is_required"] = data["isRequired"]
    else:
        out["is_required"] = False
    return out
