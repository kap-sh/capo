"""Generated from Smithy shape ``com.amazonaws.quicksight#MaximumMinimumComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.maximum_minimum_computation_type
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class MaximumMinimumComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    type: "capo_quicksight.types.maximum_minimum_computation_type.MaximumMinimumComputationType"
    """<p>The type of computation. Choose one of the following options:</p> <ul> <li> <p>MAXIMUM: A maximum computation.</p> </li> <li> <p>MINIMUM: A minimum computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaximumMinimumComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["Time"] = capo_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["Value"] = capo_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    import capo_quicksight.types.maximum_minimum_computation_type

    out["Type"] = capo_quicksight.types.maximum_minimum_computation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> MaximumMinimumComputation:
    out: MaximumMinimumComputation = {}  # type: ignore[typeddict-item]
    if data.get("ComputationId") is not None:
        out["computation_id"] = data["ComputationId"]
    else:
        out["computation_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Time") is not None:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.maximum_minimum_computation_type

        out["type"] = (
            capo_quicksight.types.maximum_minimum_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.maximum_minimum_computation_type.MaximumMinimumComputationType",
            "",
        )
    return out


def redact_sensitive(value: MaximumMinimumComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["time"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.redact_sensitive(
            value["value"]
        )
    return out
