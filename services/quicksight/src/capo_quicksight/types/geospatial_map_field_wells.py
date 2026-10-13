"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_map_aggregated_field_wells


class GeospatialMapFieldWells(TypedDict, closed=True):
    geospatial_map_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.geospatial_map_aggregated_field_wells.GeospatialMapAggregatedFieldWells"
    ]
    """<p>The aggregated field well for a geospatial map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapFieldWells) -> dict:
    out: dict = {}
    if "geospatial_map_aggregated_field_wells" in value:
        import capo_quicksight.types.geospatial_map_aggregated_field_wells

        out["GeospatialMapAggregatedFieldWells"] = (
            capo_quicksight.types.geospatial_map_aggregated_field_wells.serialize_json(
                value["geospatial_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapFieldWells:
    out: GeospatialMapFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("GeospatialMapAggregatedFieldWells") is not None:
        import capo_quicksight.types.geospatial_map_aggregated_field_wells

        out["geospatial_map_aggregated_field_wells"] = (
            capo_quicksight.types.geospatial_map_aggregated_field_wells.deserialize_json(
                data["GeospatialMapAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: GeospatialMapFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geospatial_map_aggregated_field_wells" in value:
        import capo_quicksight.types.geospatial_map_aggregated_field_wells

        out["geospatial_map_aggregated_field_wells"] = (
            capo_quicksight.types.geospatial_map_aggregated_field_wells.redact_sensitive(
                value["geospatial_map_aggregated_field_wells"]
            )
        )
    return out
