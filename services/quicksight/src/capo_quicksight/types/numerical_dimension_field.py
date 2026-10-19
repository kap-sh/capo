"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericalDimensionField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.field_id
    import capo_quicksight.types.hierarchy_id
    import capo_quicksight.types.number_format_configuration


class NumericalDimensionField(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>NumericalDimensionField</code>.</p>"""
    hierarchy_id: NotRequired["capo_quicksight.types.hierarchy_id.HierarchyId"]
    """<p>The custom hierarchy ID.</p>"""
    format_configuration: NotRequired[
        "capo_quicksight.types.number_format_configuration.NumberFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalDimensionField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "hierarchy_id" in value:
        out["HierarchyId"] = value["hierarchy_id"]
    if "format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.number_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericalDimensionField:
    out: NumericalDimensionField = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("NumericalDimensionField.column required")
    if data.get("HierarchyId") is not None:
        out["hierarchy_id"] = data["HierarchyId"]
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.number_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.number_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: NumericalDimensionField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.number_format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    return out
