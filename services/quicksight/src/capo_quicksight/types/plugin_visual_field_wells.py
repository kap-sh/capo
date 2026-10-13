"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualFieldWells``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.plugin_visual_field_well

PluginVisualFieldWells: TypeAlias = list[
    "capo_quicksight.types.plugin_visual_field_well.PluginVisualFieldWell"
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualFieldWells) -> list:
    import capo_quicksight.types.plugin_visual_field_well

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.plugin_visual_field_well.serialize_json(item))
    return out


def deserialize_json(data: list) -> PluginVisualFieldWells:
    import capo_quicksight.types.plugin_visual_field_well

    out: PluginVisualFieldWells = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.plugin_visual_field_well.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PluginVisualFieldWells) -> list[Any]:
    import capo_quicksight.types.plugin_visual_field_well

    return [
        capo_quicksight.types.plugin_visual_field_well.redact_sensitive(item)
        for item in value
    ]
