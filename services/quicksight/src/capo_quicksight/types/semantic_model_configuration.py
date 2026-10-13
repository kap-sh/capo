"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticModelConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_semantic_metadata_list
    import capo_quicksight.types.semantic_table_map


class SemanticModelConfiguration(TypedDict, closed=True):
    table_map: NotRequired["capo_quicksight.types.semantic_table_map.SemanticTableMap"]
    """<p>A map of semantic tables that define the analytical structure.</p>"""
    semantic_metadata: NotRequired[
        "capo_quicksight.types.data_set_semantic_metadata_list.DataSetSemanticMetadataList"
    ]
    """<p>The dataset-level semantic metadata, including a description and custom instructions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticModelConfiguration) -> dict:
    out: dict = {}
    if "table_map" in value:
        import capo_quicksight.types.semantic_table_map

        out["TableMap"] = capo_quicksight.types.semantic_table_map.serialize_json(
            value["table_map"]
        )
    if "semantic_metadata" in value:
        import capo_quicksight.types.data_set_semantic_metadata_list

        out["SemanticMetadata"] = (
            capo_quicksight.types.data_set_semantic_metadata_list.serialize_json(
                value["semantic_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticModelConfiguration:
    out: SemanticModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TableMap") is not None:
        import capo_quicksight.types.semantic_table_map

        out["table_map"] = capo_quicksight.types.semantic_table_map.deserialize_json(
            data["TableMap"]
        )
    if data.get("SemanticMetadata") is not None:
        import capo_quicksight.types.data_set_semantic_metadata_list

        out["semantic_metadata"] = (
            capo_quicksight.types.data_set_semantic_metadata_list.deserialize_json(
                data["SemanticMetadata"]
            )
        )
    return out


def redact_sensitive(value: SemanticModelConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "table_map" in value:
        import capo_quicksight.types.semantic_table_map

        out["table_map"] = capo_quicksight.types.semantic_table_map.redact_sensitive(
            value["table_map"]
        )
    if "semantic_metadata" in value:
        import capo_quicksight.types.data_set_semantic_metadata_list

        out["semantic_metadata"] = (
            capo_quicksight.types.data_set_semantic_metadata_list.redact_sensitive(
                value["semantic_metadata"]
            )
        )
    return out
