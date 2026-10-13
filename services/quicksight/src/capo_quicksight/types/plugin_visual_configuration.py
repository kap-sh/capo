"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.plugin_visual_field_wells
    import capo_quicksight.types.plugin_visual_options
    import capo_quicksight.types.plugin_visual_sort_configuration


class PluginVisualConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.plugin_visual_field_wells.PluginVisualFieldWells"
    ]
    """<p>The field wells configuration of the plugin visual.</p>"""
    visual_options: NotRequired[
        "capo_quicksight.types.plugin_visual_options.PluginVisualOptions"
    ]
    """<p>The persisted properties of the plugin visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.plugin_visual_sort_configuration.PluginVisualSortConfiguration"
    ]
    """<p>The sort configuration of the plugin visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.plugin_visual_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.plugin_visual_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "visual_options" in value:
        import capo_quicksight.types.plugin_visual_options

        out["VisualOptions"] = (
            capo_quicksight.types.plugin_visual_options.serialize_json(
                value["visual_options"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.plugin_visual_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.plugin_visual_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualConfiguration:
    out: PluginVisualConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.plugin_visual_field_wells

        out["field_wells"] = (
            capo_quicksight.types.plugin_visual_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("VisualOptions") is not None:
        import capo_quicksight.types.plugin_visual_options

        out["visual_options"] = (
            capo_quicksight.types.plugin_visual_options.deserialize_json(
                data["VisualOptions"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.plugin_visual_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.plugin_visual_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PluginVisualConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.plugin_visual_field_wells

        out["field_wells"] = (
            capo_quicksight.types.plugin_visual_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    return out
