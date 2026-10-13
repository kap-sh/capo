"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.histogram_aggregated_field_wells


class HistogramFieldWells(TypedDict, closed=True):
    histogram_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.histogram_aggregated_field_wells.HistogramAggregatedFieldWells"
    ]
    """<p>The field well configuration of a histogram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramFieldWells) -> dict:
    out: dict = {}
    if "histogram_aggregated_field_wells" in value:
        import capo_quicksight.types.histogram_aggregated_field_wells

        out["HistogramAggregatedFieldWells"] = (
            capo_quicksight.types.histogram_aggregated_field_wells.serialize_json(
                value["histogram_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistogramFieldWells:
    out: HistogramFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("HistogramAggregatedFieldWells") is not None:
        import capo_quicksight.types.histogram_aggregated_field_wells

        out["histogram_aggregated_field_wells"] = (
            capo_quicksight.types.histogram_aggregated_field_wells.deserialize_json(
                data["HistogramAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: HistogramFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "histogram_aggregated_field_wells" in value:
        import capo_quicksight.types.histogram_aggregated_field_wells

        out["histogram_aggregated_field_wells"] = (
            capo_quicksight.types.histogram_aggregated_field_wells.redact_sensitive(
                value["histogram_aggregated_field_wells"]
            )
        )
    return out
