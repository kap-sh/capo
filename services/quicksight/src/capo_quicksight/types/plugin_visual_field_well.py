"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualFieldWell``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list
    import capo_quicksight.types.plugin_visual_axis_name
    import capo_quicksight.types.unaggregated_field_list


class PluginVisualFieldWell(TypedDict, closed=True):
    axis_name: NotRequired[
        "capo_quicksight.types.plugin_visual_axis_name.PluginVisualAxisName"
    ]
    """<p>The semantic axis name for the field well.</p>"""
    dimensions: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>A list of dimensions for the field well.</p>"""
    measures: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>A list of measures that exist in the field well.</p>"""
    unaggregated: NotRequired[
        "capo_quicksight.types.unaggregated_field_list.UnaggregatedFieldList"
    ]
    """<p>A list of unaggregated fields that exist in the field well.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualFieldWell) -> dict:
    out: dict = {}
    if "axis_name" in value:
        import capo_quicksight.types.plugin_visual_axis_name

        out["AxisName"] = capo_quicksight.types.plugin_visual_axis_name.serialize_json(
            value["axis_name"]
        )
    if "dimensions" in value:
        import capo_quicksight.types.dimension_field_list

        out["Dimensions"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["dimensions"]
        )
    if "measures" in value:
        import capo_quicksight.types.measure_field_list

        out["Measures"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["measures"]
        )
    if "unaggregated" in value:
        import capo_quicksight.types.unaggregated_field_list

        out["Unaggregated"] = (
            capo_quicksight.types.unaggregated_field_list.serialize_json(
                value["unaggregated"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualFieldWell:
    out: PluginVisualFieldWell = {}  # type: ignore[typeddict-item]
    if data.get("AxisName") is not None:
        import capo_quicksight.types.plugin_visual_axis_name

        out["axis_name"] = (
            capo_quicksight.types.plugin_visual_axis_name.deserialize_json(
                data["AxisName"]
            )
        )
    if data.get("Dimensions") is not None:
        import capo_quicksight.types.dimension_field_list

        out["dimensions"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Dimensions"]
        )
    if data.get("Measures") is not None:
        import capo_quicksight.types.measure_field_list

        out["measures"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Measures"]
        )
    if data.get("Unaggregated") is not None:
        import capo_quicksight.types.unaggregated_field_list

        out["unaggregated"] = (
            capo_quicksight.types.unaggregated_field_list.deserialize_json(
                data["Unaggregated"]
            )
        )
    return out


def redact_sensitive(value: PluginVisualFieldWell) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dimensions" in value:
        import capo_quicksight.types.dimension_field_list

        out["dimensions"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["dimensions"]
        )
    if "measures" in value:
        import capo_quicksight.types.measure_field_list

        out["measures"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["measures"]
        )
    if "unaggregated" in value:
        import capo_quicksight.types.unaggregated_field_list

        out["unaggregated"] = (
            capo_quicksight.types.unaggregated_field_list.redact_sensitive(
                value["unaggregated"]
            )
        )
    return out
