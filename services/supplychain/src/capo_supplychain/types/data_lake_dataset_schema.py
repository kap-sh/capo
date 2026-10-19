"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_primary_key_field_list
    import capo_supplychain.types.data_lake_dataset_schema_field_list
    import capo_supplychain.types.data_lake_dataset_schema_name


class DataLakeDatasetSchema(TypedDict, closed=True):
    name: (
        "capo_supplychain.types.data_lake_dataset_schema_name.DataLakeDatasetSchemaName"
    )
    """<p>The name of the dataset schema.</p>"""
    fields: "capo_supplychain.types.data_lake_dataset_schema_field_list.DataLakeDatasetSchemaFieldList"
    """<p>The list of field details of the dataset schema.</p>"""
    primary_keys: NotRequired[
        "capo_supplychain.types.data_lake_dataset_primary_key_field_list.DataLakeDatasetPrimaryKeyFieldList"
    ]
    """<p>The list of primary key fields for the dataset. Primary keys defined can help data ingestion methods to ensure data uniqueness: CreateDataIntegrationFlow's dedupe strategy will leverage primary keys to perform records deduplication before write to dataset; SendDataIntegrationEvent's UPSERT and DELETE can only work with dataset with primary keys. For more details, refer to those data ingestion documentations.</p> <p>Note that defining primary keys does not necessarily mean the dataset cannot have duplicate records, duplicate records can still be ingested if CreateDataIntegrationFlow's dedupe disabled or through SendDataIntegrationEvent's APPEND operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchema) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_supplychain.types.data_lake_dataset_schema_field_list

    out["fields"] = (
        capo_supplychain.types.data_lake_dataset_schema_field_list.serialize_json(
            value["fields"]
        )
    )
    if "primary_keys" in value:
        import capo_supplychain.types.data_lake_dataset_primary_key_field_list

        out["primaryKeys"] = (
            capo_supplychain.types.data_lake_dataset_primary_key_field_list.serialize_json(
                value["primary_keys"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeDatasetSchema:
    out: DataLakeDatasetSchema = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("fields") is not None:
        import capo_supplychain.types.data_lake_dataset_schema_field_list

        out["fields"] = (
            capo_supplychain.types.data_lake_dataset_schema_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    if data.get("primaryKeys") is not None:
        import capo_supplychain.types.data_lake_dataset_primary_key_field_list

        out["primary_keys"] = (
            capo_supplychain.types.data_lake_dataset_primary_key_field_list.deserialize_json(
                data["primaryKeys"]
            )
        )
    return out
