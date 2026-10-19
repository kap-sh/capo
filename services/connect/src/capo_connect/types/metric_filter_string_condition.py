"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterStringCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.metric_filter_string_condition_comparison
    import capo_connect.types.string_value_list


class MetricFilterStringCondition(TypedDict, closed=True):
    comparison: "capo_connect.types.metric_filter_string_condition_comparison.MetricFilterStringConditionComparison"
    """<p>The comparison operator. Valid values: <code>MATCHES_ANY</code> (matches any of the specified values) | <code>MATCHES_NONE</code> (matches none of the specified values).</p>"""
    values: "capo_connect.types.string_value_list.StringValueList"
    """<p>The string values to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterStringCondition) -> dict:
    out: dict = {}
    import capo_connect.types.metric_filter_string_condition_comparison

    out["Comparison"] = (
        capo_connect.types.metric_filter_string_condition_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_connect.types.string_value_list

    out["Values"] = capo_connect.types.string_value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> MetricFilterStringCondition:
    out: MetricFilterStringCondition = {}  # type: ignore[typeddict-item]
    if data.get("Comparison") is not None:
        import capo_connect.types.metric_filter_string_condition_comparison

        out["comparison"] = (
            capo_connect.types.metric_filter_string_condition_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_connect.types.metric_filter_string_condition_comparison.MetricFilterStringConditionComparison",
            "",
        )
    if data.get("Values") is not None:
        import capo_connect.types.string_value_list

        out["values"] = capo_connect.types.string_value_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
