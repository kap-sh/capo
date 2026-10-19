"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTableSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id


class DestinationTableSource(TypedDict, closed=True):
    transform_operation_id: (
        "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the transform operation that provides data to the destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTableSource) -> dict:
    out: dict = {}
    out["TransformOperationId"] = value["transform_operation_id"]
    return out


def deserialize_json(data: dict) -> DestinationTableSource:
    out: DestinationTableSource = {}  # type: ignore[typeddict-item]
    if data.get("TransformOperationId") is not None:
        out["transform_operation_id"] = data["TransformOperationId"]
    else:
        out["transform_operation_id"] = ""
    return out
