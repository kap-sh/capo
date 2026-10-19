"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterBooleanCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.metric_filter_boolean_condition_comparison


class MetricFilterBooleanCondition(TypedDict, closed=True):
    comparison: "capo_connect.types.metric_filter_boolean_condition_comparison.MetricFilterBooleanConditionComparison"
    """<p>The comparison operator. Valid values: <code>IS_TRUE</code> (matches when the field is true) | <code>IS_FALSE</code> (matches when the field is false).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterBooleanCondition) -> dict:
    out: dict = {}
    import capo_connect.types.metric_filter_boolean_condition_comparison

    out["Comparison"] = (
        capo_connect.types.metric_filter_boolean_condition_comparison.serialize_json(
            value["comparison"]
        )
    )
    return out


def deserialize_json(data: dict) -> MetricFilterBooleanCondition:
    out: MetricFilterBooleanCondition = {}  # type: ignore[typeddict-item]
    if data.get("Comparison") is not None:
        import capo_connect.types.metric_filter_boolean_condition_comparison

        out["comparison"] = (
            capo_connect.types.metric_filter_boolean_condition_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_connect.types.metric_filter_boolean_condition_comparison.MetricFilterBooleanConditionComparison",
            "",
        )
    return out
