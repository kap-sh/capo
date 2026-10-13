"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_aggregated_field_wells
    import capo_quicksight.types.table_unaggregated_field_wells


class TableFieldWells(TypedDict, closed=True):
    table_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.table_aggregated_field_wells.TableAggregatedFieldWells"
    ]
    """<p>The aggregated field well for the table.</p>"""
    table_unaggregated_field_wells: NotRequired[
        "capo_quicksight.types.table_unaggregated_field_wells.TableUnaggregatedFieldWells"
    ]
    """<p>The unaggregated field well for the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldWells) -> dict:
    out: dict = {}
    if "table_aggregated_field_wells" in value:
        import capo_quicksight.types.table_aggregated_field_wells

        out["TableAggregatedFieldWells"] = (
            capo_quicksight.types.table_aggregated_field_wells.serialize_json(
                value["table_aggregated_field_wells"]
            )
        )
    if "table_unaggregated_field_wells" in value:
        import capo_quicksight.types.table_unaggregated_field_wells

        out["TableUnaggregatedFieldWells"] = (
            capo_quicksight.types.table_unaggregated_field_wells.serialize_json(
                value["table_unaggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldWells:
    out: TableFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("TableAggregatedFieldWells") is not None:
        import capo_quicksight.types.table_aggregated_field_wells

        out["table_aggregated_field_wells"] = (
            capo_quicksight.types.table_aggregated_field_wells.deserialize_json(
                data["TableAggregatedFieldWells"]
            )
        )
    if data.get("TableUnaggregatedFieldWells") is not None:
        import capo_quicksight.types.table_unaggregated_field_wells

        out["table_unaggregated_field_wells"] = (
            capo_quicksight.types.table_unaggregated_field_wells.deserialize_json(
                data["TableUnaggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: TableFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "table_aggregated_field_wells" in value:
        import capo_quicksight.types.table_aggregated_field_wells

        out["table_aggregated_field_wells"] = (
            capo_quicksight.types.table_aggregated_field_wells.redact_sensitive(
                value["table_aggregated_field_wells"]
            )
        )
    if "table_unaggregated_field_wells" in value:
        import capo_quicksight.types.table_unaggregated_field_wells

        out["table_unaggregated_field_wells"] = (
            capo_quicksight.types.table_unaggregated_field_wells.redact_sensitive(
                value["table_unaggregated_field_wells"]
            )
        )
    return out
