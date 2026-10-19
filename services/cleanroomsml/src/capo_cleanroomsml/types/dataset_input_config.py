"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.data_source
    import capo_cleanroomsml.types.dataset_schema_list


class DatasetInputConfig(TypedDict, closed=True):
    schema: "capo_cleanroomsml.types.dataset_schema_list.DatasetSchemaList"
    """<p>The schema information for the training data.</p>"""
    data_source: "capo_cleanroomsml.types.data_source.DataSource"
    """<p>A DataSource object that specifies the Glue data source for the training data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetInputConfig) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.dataset_schema_list

    out["schema"] = capo_cleanroomsml.types.dataset_schema_list.serialize_json(
        value["schema"]
    )
    import capo_cleanroomsml.types.data_source

    out["dataSource"] = capo_cleanroomsml.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> DatasetInputConfig:
    out: DatasetInputConfig = {}  # type: ignore[typeddict-item]
    if data.get("schema") is not None:
        import capo_cleanroomsml.types.dataset_schema_list

        out["schema"] = capo_cleanroomsml.types.dataset_schema_list.deserialize_json(
            data["schema"]
        )
    else:
        out["schema"] = []
    if data.get("dataSource") is not None:
        import capo_cleanroomsml.types.data_source

        out["data_source"] = capo_cleanroomsml.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("DatasetInputConfig.data_source required")
    return out
