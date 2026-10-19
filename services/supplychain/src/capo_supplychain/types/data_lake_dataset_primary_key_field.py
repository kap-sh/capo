"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPrimaryKeyField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_schema_field_name


class DataLakeDatasetPrimaryKeyField(TypedDict, closed=True):
    name: "capo_supplychain.types.data_lake_dataset_schema_field_name.DataLakeDatasetSchemaFieldName"
    """<p>The name of the primary key field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPrimaryKeyField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DataLakeDatasetPrimaryKeyField:
    out: DataLakeDatasetPrimaryKeyField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
