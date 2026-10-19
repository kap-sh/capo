"""Generated from Smithy shape ``com.amazonaws.quicksight#MetricComparisonComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class MetricComparisonComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    from_value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The field that is used in a metric comparison from value setup.</p>"""
    target_value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The field that is used in a metric comparison to value setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricComparisonComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["Time"] = capo_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "from_value" in value:
        import capo_quicksight.types.measure_field

        out["FromValue"] = capo_quicksight.types.measure_field.serialize_json(
            value["from_value"]
        )
    if "target_value" in value:
        import capo_quicksight.types.measure_field

        out["TargetValue"] = capo_quicksight.types.measure_field.serialize_json(
            value["target_value"]
        )
    return out


def deserialize_json(data: dict) -> MetricComparisonComputation:
    out: MetricComparisonComputation = {}  # type: ignore[typeddict-item]
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
    if data.get("FromValue") is not None:
        import capo_quicksight.types.measure_field

        out["from_value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["FromValue"]
        )
    if data.get("TargetValue") is not None:
        import capo_quicksight.types.measure_field

        out["target_value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["TargetValue"]
        )
    return out


def redact_sensitive(value: MetricComparisonComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["time"]
        )
    if "from_value" in value:
        import capo_quicksight.types.measure_field

        out["from_value"] = capo_quicksight.types.measure_field.redact_sensitive(
            value["from_value"]
        )
    if "target_value" in value:
        import capo_quicksight.types.measure_field

        out["target_value"] = capo_quicksight.types.measure_field.redact_sensitive(
            value["target_value"]
        )
    return out
