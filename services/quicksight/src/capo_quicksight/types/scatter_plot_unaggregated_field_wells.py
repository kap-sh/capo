"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotUnaggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class ScatterPlotUnaggregatedFieldWells(TypedDict, closed=True):
    x_axis: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The x-axis field well of a scatter plot.</p> <p>The x-axis is a dimension field and cannot be aggregated.</p>"""
    y_axis: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The y-axis field well of a scatter plot.</p> <p>The y-axis is a dimension field and cannot be aggregated.</p>"""
    size: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The size field well of a scatter plot.</p>"""
    category: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field well of a scatter plot.</p>"""
    label: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The label field well of a scatter plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotUnaggregatedFieldWells) -> dict:
    out: dict = {}
    if "x_axis" in value:
        import capo_quicksight.types.dimension_field_list

        out["XAxis"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["x_axis"]
        )
    if "y_axis" in value:
        import capo_quicksight.types.dimension_field_list

        out["YAxis"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["y_axis"]
        )
    if "size" in value:
        import capo_quicksight.types.measure_field_list

        out["Size"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["size"]
        )
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["Category"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "label" in value:
        import capo_quicksight.types.dimension_field_list

        out["Label"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotUnaggregatedFieldWells:
    out: ScatterPlotUnaggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("XAxis") is not None:
        import capo_quicksight.types.dimension_field_list

        out["x_axis"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["XAxis"]
        )
    if data.get("YAxis") is not None:
        import capo_quicksight.types.dimension_field_list

        out["y_axis"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["YAxis"]
        )
    if data.get("Size") is not None:
        import capo_quicksight.types.measure_field_list

        out["size"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Size"]
        )
    if data.get("Category") is not None:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Category"]
        )
    if data.get("Label") is not None:
        import capo_quicksight.types.dimension_field_list

        out["label"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Label"]
        )
    return out


def redact_sensitive(value: ScatterPlotUnaggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "x_axis" in value:
        import capo_quicksight.types.dimension_field_list

        out["x_axis"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["x_axis"]
        )
    if "y_axis" in value:
        import capo_quicksight.types.dimension_field_list

        out["y_axis"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["y_axis"]
        )
    if "size" in value:
        import capo_quicksight.types.measure_field_list

        out["size"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["size"]
        )
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["category"]
        )
    if "label" in value:
        import capo_quicksight.types.dimension_field_list

        out["label"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["label"]
        )
    return out
