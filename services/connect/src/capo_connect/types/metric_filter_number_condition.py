"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterNumberCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.metric_filter_number_condition_comparison
    import capo_connect.types.number_value_list


class MetricFilterNumberCondition(TypedDict, closed=True):
    comparison: "capo_connect.types.metric_filter_number_condition_comparison.MetricFilterNumberConditionComparison"
    """<p>The comparison operator. Valid values: <code>LESSER</code> (less than) | <code>LESSER_OR_EQUAL</code> (less than or equal to) | <code>GREATER</code> (greater than) | <code>GREATER_OR_EQUAL</code> (greater than or equal to).</p>"""
    values: "capo_connect.types.number_value_list.NumberValueList"
    """<p>The numeric values to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterNumberCondition) -> dict:
    out: dict = {}
    import capo_connect.types.metric_filter_number_condition_comparison

    out["Comparison"] = (
        capo_connect.types.metric_filter_number_condition_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_connect.types.number_value_list

    out["Values"] = capo_connect.types.number_value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> MetricFilterNumberCondition:
    out: MetricFilterNumberCondition = {}  # type: ignore[typeddict-item]
    if data.get("Comparison") is not None:
        import capo_connect.types.metric_filter_number_condition_comparison

        out["comparison"] = (
            capo_connect.types.metric_filter_number_condition_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_connect.types.metric_filter_number_condition_comparison.MetricFilterNumberConditionComparison",
            "",
        )
    if data.get("Values") is not None:
        import capo_connect.types.number_value_list

        out["values"] = capo_connect.types.number_value_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
