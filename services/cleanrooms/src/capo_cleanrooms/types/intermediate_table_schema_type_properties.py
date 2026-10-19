"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableSchemaTypeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.uuid


class IntermediateTableSchemaTypeProperties(TypedDict, closed=True):
    intermediate_table_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableSchemaTypeProperties) -> dict:
    out: dict = {}
    out["intermediateTableId"] = value["intermediate_table_id"]
    return out


def deserialize_json(data: dict) -> IntermediateTableSchemaTypeProperties:
    out: IntermediateTableSchemaTypeProperties = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTableId") is not None:
        out["intermediate_table_id"] = data["intermediateTableId"]
    else:
        out["intermediate_table_id"] = ""
    return out
