"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomRankedComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string
    import capo_quicksight.types.top_bottom_computation_type
    import capo_quicksight.types.top_bottom_ranked_computation_result_size


class TopBottomRankedComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    category: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    result_size: NotRequired[
        "capo_quicksight.types.top_bottom_ranked_computation_result_size.TopBottomRankedComputationResultSize"
    ]
    """<p>The result size of a top and bottom ranked computation.</p>"""
    type: "capo_quicksight.types.top_bottom_computation_type.TopBottomComputationType"
    """<p>The computation type. Choose one of the following options:</p> <ul> <li> <p>TOP: A top ranked computation.</p> </li> <li> <p>BOTTOM: A bottom ranked computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomRankedComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "result_size" in value:
        out["ResultSize"] = value["result_size"]
    import capo_quicksight.types.top_bottom_computation_type

    out["Type"] = capo_quicksight.types.top_bottom_computation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> TopBottomRankedComputation:
    out: TopBottomRankedComputation = {}  # type: ignore[typeddict-item]
    if data.get("ComputationId") is not None:
        out["computation_id"] = data["ComputationId"]
    else:
        out["computation_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("ResultSize") is not None:
        out["result_size"] = data["ResultSize"]
    if data.get("Type") is not None:
        import capo_quicksight.types.top_bottom_computation_type

        out["type"] = (
            capo_quicksight.types.top_bottom_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.top_bottom_computation_type.TopBottomComputationType",
            "",
        )
    return out


def redact_sensitive(value: TopBottomRankedComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
