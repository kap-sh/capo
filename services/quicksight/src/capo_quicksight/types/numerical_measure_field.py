"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericalMeasureField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.field_id
    import capo_quicksight.types.number_format_configuration
    import capo_quicksight.types.numerical_aggregation_function


class NumericalMeasureField(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>NumericalMeasureField</code>.</p>"""
    aggregation_function: NotRequired[
        "capo_quicksight.types.numerical_aggregation_function.NumericalAggregationFunction"
    ]
    """<p>The aggregation function of the measure field.</p>"""
    format_configuration: NotRequired[
        "capo_quicksight.types.number_format_configuration.NumberFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalMeasureField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "aggregation_function" in value:
        import capo_quicksight.types.numerical_aggregation_function

        out["AggregationFunction"] = (
            capo_quicksight.types.numerical_aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    if "format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.number_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericalMeasureField:
    out: NumericalMeasureField = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("NumericalMeasureField.column required")
    if data.get("AggregationFunction") is not None:
        import capo_quicksight.types.numerical_aggregation_function

        out["aggregation_function"] = (
            capo_quicksight.types.numerical_aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.number_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.number_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: NumericalMeasureField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.number_format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    return out
