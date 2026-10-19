"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableSchemaTypeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table_input_source_list
    import capo_cleanrooms.types.uuid


class IdMappingTableSchemaTypeProperties(TypedDict, closed=True):
    id_mapping_table_input_source: "capo_cleanrooms.types.id_mapping_table_input_source_list.IdMappingTableInputSourceList"
    """<p>Defines which ID namespace associations are used to create the ID mapping table.</p>"""
    id_mapping_table_id: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>The unique identifier of the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableSchemaTypeProperties) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_mapping_table_input_source_list

    out["idMappingTableInputSource"] = (
        capo_cleanrooms.types.id_mapping_table_input_source_list.serialize_json(
            value["id_mapping_table_input_source"]
        )
    )
    if "id_mapping_table_id" in value:
        out["idMappingTableId"] = value["id_mapping_table_id"]
    return out


def deserialize_json(data: dict) -> IdMappingTableSchemaTypeProperties:
    out: IdMappingTableSchemaTypeProperties = {}  # type: ignore[typeddict-item]
    if data.get("idMappingTableInputSource") is not None:
        import capo_cleanrooms.types.id_mapping_table_input_source_list

        out["id_mapping_table_input_source"] = (
            capo_cleanrooms.types.id_mapping_table_input_source_list.deserialize_json(
                data["idMappingTableInputSource"]
            )
        )
    else:
        out["id_mapping_table_input_source"] = []
    if data.get("idMappingTableId") is not None:
        out["id_mapping_table_id"] = data["idMappingTableId"]
    return out
