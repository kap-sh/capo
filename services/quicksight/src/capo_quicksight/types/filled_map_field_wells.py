"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filled_map_aggregated_field_wells


class FilledMapFieldWells(TypedDict, closed=True):
    filled_map_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.filled_map_aggregated_field_wells.FilledMapAggregatedFieldWells"
    ]
    """<p>The aggregated field well of the filled map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapFieldWells) -> dict:
    out: dict = {}
    if "filled_map_aggregated_field_wells" in value:
        import capo_quicksight.types.filled_map_aggregated_field_wells

        out["FilledMapAggregatedFieldWells"] = (
            capo_quicksight.types.filled_map_aggregated_field_wells.serialize_json(
                value["filled_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapFieldWells:
    out: FilledMapFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("FilledMapAggregatedFieldWells") is not None:
        import capo_quicksight.types.filled_map_aggregated_field_wells

        out["filled_map_aggregated_field_wells"] = (
            capo_quicksight.types.filled_map_aggregated_field_wells.deserialize_json(
                data["FilledMapAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: FilledMapFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filled_map_aggregated_field_wells" in value:
        import capo_quicksight.types.filled_map_aggregated_field_wells

        out["filled_map_aggregated_field_wells"] = (
            capo_quicksight.types.filled_map_aggregated_field_wells.redact_sensitive(
                value["filled_map_aggregated_field_wells"]
            )
        )
    return out
