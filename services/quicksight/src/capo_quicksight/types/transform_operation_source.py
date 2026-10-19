"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_column_id_mapping_list
    import capo_quicksight.types.data_set_entity_resource_id


class TransformOperationSource(TypedDict, closed=True):
    transform_operation_id: (
        "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the transform operation that provides input data.</p>"""
    column_id_mappings: NotRequired[
        "capo_quicksight.types.data_set_column_id_mapping_list.DataSetColumnIdMappingList"
    ]
    """<p>The mappings between source column identifiers and target column identifiers for this transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformOperationSource) -> dict:
    out: dict = {}
    out["TransformOperationId"] = value["transform_operation_id"]
    if "column_id_mappings" in value:
        import capo_quicksight.types.data_set_column_id_mapping_list

        out["ColumnIdMappings"] = (
            capo_quicksight.types.data_set_column_id_mapping_list.serialize_json(
                value["column_id_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformOperationSource:
    out: TransformOperationSource = {}  # type: ignore[typeddict-item]
    if data.get("TransformOperationId") is not None:
        out["transform_operation_id"] = data["TransformOperationId"]
    else:
        out["transform_operation_id"] = ""
    if data.get("ColumnIdMappings") is not None:
        import capo_quicksight.types.data_set_column_id_mapping_list

        out["column_id_mappings"] = (
            capo_quicksight.types.data_set_column_id_mapping_list.deserialize_json(
                data["ColumnIdMappings"]
            )
        )
    return out
