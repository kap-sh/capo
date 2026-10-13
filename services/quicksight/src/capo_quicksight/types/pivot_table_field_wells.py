"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_aggregated_field_wells


class PivotTableFieldWells(TypedDict, closed=True):
    pivot_table_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.pivot_table_aggregated_field_wells.PivotTableAggregatedFieldWells"
    ]
    """<p>The aggregated field well for the pivot table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldWells) -> dict:
    out: dict = {}
    if "pivot_table_aggregated_field_wells" in value:
        import capo_quicksight.types.pivot_table_aggregated_field_wells

        out["PivotTableAggregatedFieldWells"] = (
            capo_quicksight.types.pivot_table_aggregated_field_wells.serialize_json(
                value["pivot_table_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldWells:
    out: PivotTableFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("PivotTableAggregatedFieldWells") is not None:
        import capo_quicksight.types.pivot_table_aggregated_field_wells

        out["pivot_table_aggregated_field_wells"] = (
            capo_quicksight.types.pivot_table_aggregated_field_wells.deserialize_json(
                data["PivotTableAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: PivotTableFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pivot_table_aggregated_field_wells" in value:
        import capo_quicksight.types.pivot_table_aggregated_field_wells

        out["pivot_table_aggregated_field_wells"] = (
            capo_quicksight.types.pivot_table_aggregated_field_wells.redact_sensitive(
                value["pivot_table_aggregated_field_wells"]
            )
        )
    return out
