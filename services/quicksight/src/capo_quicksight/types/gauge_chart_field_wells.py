"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field_list


class GaugeChartFieldWells(TypedDict, closed=True):
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a <code>GaugeChartVisual</code>.</p>"""
    target_values: NotRequired[
        "capo_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The target value field wells of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "target_values" in value:
        import capo_quicksight.types.measure_field_list

        out["TargetValues"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["target_values"]
        )
    return out


def deserialize_json(data: dict) -> GaugeChartFieldWells:
    out: GaugeChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if data.get("TargetValues") is not None:
        import capo_quicksight.types.measure_field_list

        out["target_values"] = (
            capo_quicksight.types.measure_field_list.deserialize_json(
                data["TargetValues"]
            )
        )
    return out


def redact_sensitive(value: GaugeChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["values"]
        )
    if "target_values" in value:
        import capo_quicksight.types.measure_field_list

        out["target_values"] = (
            capo_quicksight.types.measure_field_list.redact_sensitive(
                value["target_values"]
            )
        )
    return out
