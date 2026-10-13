"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomMoversComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string
    import capo_quicksight.types.top_bottom_computation_type
    import capo_quicksight.types.top_bottom_movers_computation_mover_size
    import capo_quicksight.types.top_bottom_sort_order


class TopBottomMoversComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    category: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    mover_size: NotRequired[
        "capo_quicksight.types.top_bottom_movers_computation_mover_size.TopBottomMoversComputationMoverSize"
    ]
    """<p>The mover size setup of the top and bottom movers computation.</p>"""
    sort_order: NotRequired[
        "capo_quicksight.types.top_bottom_sort_order.TopBottomSortOrder"
    ]
    """<p>The sort order setup of the top and bottom movers computation.</p>"""
    type: "capo_quicksight.types.top_bottom_computation_type.TopBottomComputationType"
    """<p>The computation type. Choose from the following options:</p> <ul> <li> <p>TOP: Top movers computation.</p> </li> <li> <p>BOTTOM: Bottom movers computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomMoversComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["Time"] = capo_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "category" in value:
        import capo_quicksight.types.dimension_field

        out["Category"] = capo_quicksight.types.dimension_field.serialize_json(
            value["category"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["Value"] = capo_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "mover_size" in value:
        out["MoverSize"] = value["mover_size"]
    if "sort_order" in value:
        import capo_quicksight.types.top_bottom_sort_order

        out["SortOrder"] = capo_quicksight.types.top_bottom_sort_order.serialize_json(
            value["sort_order"]
        )
    import capo_quicksight.types.top_bottom_computation_type

    out["Type"] = capo_quicksight.types.top_bottom_computation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> TopBottomMoversComputation:
    out: TopBottomMoversComputation = {}  # type: ignore[typeddict-item]
    if data.get("ComputationId") is not None:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("TopBottomMoversComputation.computation_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Time") is not None:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
    if data.get("Category") is not None:
        import capo_quicksight.types.dimension_field

        out["category"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Category"]
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if data.get("MoverSize") is not None:
        out["mover_size"] = data["MoverSize"]
    if data.get("SortOrder") is not None:
        import capo_quicksight.types.top_bottom_sort_order

        out["sort_order"] = (
            capo_quicksight.types.top_bottom_sort_order.deserialize_json(
                data["SortOrder"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.top_bottom_computation_type

        out["type"] = (
            capo_quicksight.types.top_bottom_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TopBottomMoversComputation.type required")
    return out


def redact_sensitive(value: TopBottomMoversComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["time"]
        )
    if "category" in value:
        import capo_quicksight.types.dimension_field

        out["category"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["category"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.redact_sensitive(
            value["value"]
        )
    return out
