"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedMeasureField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.expression
    import capo_quicksight.types.field_id


class CalculatedMeasureField(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression in the table calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedMeasureField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CalculatedMeasureField:
    out: CalculatedMeasureField = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    return out


def redact_sensitive(value: CalculatedMeasureField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
