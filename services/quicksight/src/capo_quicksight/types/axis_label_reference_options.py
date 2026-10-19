"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLabelReferenceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.field_id


class AxisLabelReferenceOptions(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field that the axis label is targeted to.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the axis label is targeted to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLabelReferenceOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    return out


def deserialize_json(data: dict) -> AxisLabelReferenceOptions:
    out: AxisLabelReferenceOptions = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("AxisLabelReferenceOptions.column required")
    return out
