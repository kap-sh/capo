"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableInputReferenceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table_input_source_list


class IdMappingTableInputReferenceProperties(TypedDict, closed=True):
    id_mapping_table_input_source: "capo_cleanrooms.types.id_mapping_table_input_source_list.IdMappingTableInputSourceList"
    """<p>The input source of the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableInputReferenceProperties) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_mapping_table_input_source_list

    out["idMappingTableInputSource"] = (
        capo_cleanrooms.types.id_mapping_table_input_source_list.serialize_json(
            value["id_mapping_table_input_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdMappingTableInputReferenceProperties:
    out: IdMappingTableInputReferenceProperties = {}  # type: ignore[typeddict-item]
    if data.get("idMappingTableInputSource") is not None:
        import capo_cleanrooms.types.id_mapping_table_input_source_list

        out["id_mapping_table_input_source"] = (
            capo_cleanrooms.types.id_mapping_table_input_source_list.deserialize_json(
                data["idMappingTableInputSource"]
            )
        )
    else:
        out["id_mapping_table_input_source"] = []
    return out
