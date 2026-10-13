"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_map_field_wells
    import capo_quicksight.types.geospatial_map_style_options
    import capo_quicksight.types.geospatial_point_style_options
    import capo_quicksight.types.geospatial_window_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class GeospatialMapConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.geospatial_map_field_wells.GeospatialMapFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    window_options: NotRequired[
        "capo_quicksight.types.geospatial_window_options.GeospatialWindowOptions"
    ]
    """<p>The window options of the geospatial map.</p>"""
    map_style_options: NotRequired[
        "capo_quicksight.types.geospatial_map_style_options.GeospatialMapStyleOptions"
    ]
    """<p>The map style options of the geospatial map.</p>"""
    point_style_options: NotRequired[
        "capo_quicksight.types.geospatial_point_style_options.GeospatialPointStyleOptions"
    ]
    """<p>The point style options of the geospatial map.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.geospatial_map_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.geospatial_map_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "window_options" in value:
        import capo_quicksight.types.geospatial_window_options

        out["WindowOptions"] = (
            capo_quicksight.types.geospatial_window_options.serialize_json(
                value["window_options"]
            )
        )
    if "map_style_options" in value:
        import capo_quicksight.types.geospatial_map_style_options

        out["MapStyleOptions"] = (
            capo_quicksight.types.geospatial_map_style_options.serialize_json(
                value["map_style_options"]
            )
        )
    if "point_style_options" in value:
        import capo_quicksight.types.geospatial_point_style_options

        out["PointStyleOptions"] = (
            capo_quicksight.types.geospatial_point_style_options.serialize_json(
                value["point_style_options"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapConfiguration:
    out: GeospatialMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.geospatial_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.geospatial_map_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("WindowOptions") is not None:
        import capo_quicksight.types.geospatial_window_options

        out["window_options"] = (
            capo_quicksight.types.geospatial_window_options.deserialize_json(
                data["WindowOptions"]
            )
        )
    if data.get("MapStyleOptions") is not None:
        import capo_quicksight.types.geospatial_map_style_options

        out["map_style_options"] = (
            capo_quicksight.types.geospatial_map_style_options.deserialize_json(
                data["MapStyleOptions"]
            )
        )
    if data.get("PointStyleOptions") is not None:
        import capo_quicksight.types.geospatial_point_style_options

        out["point_style_options"] = (
            capo_quicksight.types.geospatial_point_style_options.deserialize_json(
                data["PointStyleOptions"]
            )
        )
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: GeospatialMapConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.geospatial_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.geospatial_map_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
