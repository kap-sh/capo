"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.tree_map_aggregated_field_wells


class TreeMapFieldWells(TypedDict, closed=True):
    tree_map_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.tree_map_aggregated_field_wells.TreeMapAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a tree map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapFieldWells) -> dict:
    out: dict = {}
    if "tree_map_aggregated_field_wells" in value:
        import capo_quicksight.types.tree_map_aggregated_field_wells

        out["TreeMapAggregatedFieldWells"] = (
            capo_quicksight.types.tree_map_aggregated_field_wells.serialize_json(
                value["tree_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapFieldWells:
    out: TreeMapFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("TreeMapAggregatedFieldWells") is not None:
        import capo_quicksight.types.tree_map_aggregated_field_wells

        out["tree_map_aggregated_field_wells"] = (
            capo_quicksight.types.tree_map_aggregated_field_wells.deserialize_json(
                data["TreeMapAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: TreeMapFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tree_map_aggregated_field_wells" in value:
        import capo_quicksight.types.tree_map_aggregated_field_wells

        out["tree_map_aggregated_field_wells"] = (
            capo_quicksight.types.tree_map_aggregated_field_wells.redact_sensitive(
                value["tree_map_aggregated_field_wells"]
            )
        )
    return out
