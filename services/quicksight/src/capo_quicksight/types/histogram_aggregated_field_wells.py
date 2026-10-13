"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.histogram_measure_field_list


class HistogramAggregatedFieldWells(TypedDict, closed=True):
    values: NotRequired[
        "capo_quicksight.types.histogram_measure_field_list.HistogramMeasureFieldList"
    ]
    """<p>The value field wells of a histogram. Values are aggregated by <code>COUNT</code> or <code>DISTINCT_COUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramAggregatedFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.histogram_measure_field_list

        out["Values"] = (
            capo_quicksight.types.histogram_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistogramAggregatedFieldWells:
    out: HistogramAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_quicksight.types.histogram_measure_field_list

        out["values"] = (
            capo_quicksight.types.histogram_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: HistogramAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.histogram_measure_field_list

        out["values"] = (
            capo_quicksight.types.histogram_measure_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
