"""Generated from Smithy shape ``com.amazonaws.quicksight#MeasureField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_measure_field
    import capo_quicksight.types.categorical_measure_field
    import capo_quicksight.types.date_measure_field
    import capo_quicksight.types.numerical_measure_field


class MeasureField(TypedDict, closed=True):
    numerical_measure_field: NotRequired[
        "capo_quicksight.types.numerical_measure_field.NumericalMeasureField"
    ]
    """<p>The measure type field with numerical type columns.</p>"""
    categorical_measure_field: NotRequired[
        "capo_quicksight.types.categorical_measure_field.CategoricalMeasureField"
    ]
    """<p>The measure type field with categorical type columns.</p>"""
    date_measure_field: NotRequired[
        "capo_quicksight.types.date_measure_field.DateMeasureField"
    ]
    """<p>The measure type field with date type columns.</p>"""
    calculated_measure_field: NotRequired[
        "capo_quicksight.types.calculated_measure_field.CalculatedMeasureField"
    ]
    """<p>The calculated measure field only used in pivot tables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeasureField) -> dict:
    out: dict = {}
    if "numerical_measure_field" in value:
        import capo_quicksight.types.numerical_measure_field

        out["NumericalMeasureField"] = (
            capo_quicksight.types.numerical_measure_field.serialize_json(
                value["numerical_measure_field"]
            )
        )
    if "categorical_measure_field" in value:
        import capo_quicksight.types.categorical_measure_field

        out["CategoricalMeasureField"] = (
            capo_quicksight.types.categorical_measure_field.serialize_json(
                value["categorical_measure_field"]
            )
        )
    if "date_measure_field" in value:
        import capo_quicksight.types.date_measure_field

        out["DateMeasureField"] = (
            capo_quicksight.types.date_measure_field.serialize_json(
                value["date_measure_field"]
            )
        )
    if "calculated_measure_field" in value:
        import capo_quicksight.types.calculated_measure_field

        out["CalculatedMeasureField"] = (
            capo_quicksight.types.calculated_measure_field.serialize_json(
                value["calculated_measure_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> MeasureField:
    out: MeasureField = {}  # type: ignore[typeddict-item]
    if data.get("NumericalMeasureField") is not None:
        import capo_quicksight.types.numerical_measure_field

        out["numerical_measure_field"] = (
            capo_quicksight.types.numerical_measure_field.deserialize_json(
                data["NumericalMeasureField"]
            )
        )
    if data.get("CategoricalMeasureField") is not None:
        import capo_quicksight.types.categorical_measure_field

        out["categorical_measure_field"] = (
            capo_quicksight.types.categorical_measure_field.deserialize_json(
                data["CategoricalMeasureField"]
            )
        )
    if data.get("DateMeasureField") is not None:
        import capo_quicksight.types.date_measure_field

        out["date_measure_field"] = (
            capo_quicksight.types.date_measure_field.deserialize_json(
                data["DateMeasureField"]
            )
        )
    if data.get("CalculatedMeasureField") is not None:
        import capo_quicksight.types.calculated_measure_field

        out["calculated_measure_field"] = (
            capo_quicksight.types.calculated_measure_field.deserialize_json(
                data["CalculatedMeasureField"]
            )
        )
    return out


def redact_sensitive(value: MeasureField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "numerical_measure_field" in value:
        import capo_quicksight.types.numerical_measure_field

        out["numerical_measure_field"] = (
            capo_quicksight.types.numerical_measure_field.redact_sensitive(
                value["numerical_measure_field"]
            )
        )
    if "categorical_measure_field" in value:
        import capo_quicksight.types.categorical_measure_field

        out["categorical_measure_field"] = (
            capo_quicksight.types.categorical_measure_field.redact_sensitive(
                value["categorical_measure_field"]
            )
        )
    if "date_measure_field" in value:
        import capo_quicksight.types.date_measure_field

        out["date_measure_field"] = (
            capo_quicksight.types.date_measure_field.redact_sensitive(
                value["date_measure_field"]
            )
        )
    if "calculated_measure_field" in value:
        import capo_quicksight.types.calculated_measure_field

        out["calculated_measure_field"] = (
            capo_quicksight.types.calculated_measure_field.redact_sensitive(
                value["calculated_measure_field"]
            )
        )
    return out
