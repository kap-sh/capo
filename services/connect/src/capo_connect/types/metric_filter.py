"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.metric_filter_boolean_condition
    import capo_connect.types.metric_filter_key
    import capo_connect.types.metric_filter_number_condition
    import capo_connect.types.metric_filter_string_condition


class MetricFilter(TypedDict, closed=True):
    metric_filter_key: "capo_connect.types.metric_filter_key.MetricFilterKey"
    """<p>The key identifying the field to filter on.</p>"""
    negate: "capo_connect.types.boolean.Boolean"
    """<p>Specifies whether the filter condition is negated. When set to <code>true</code>, the filter excludes matching data instead of including it.</p>"""
    number_condition: NotRequired[
        "capo_connect.types.metric_filter_number_condition.MetricFilterNumberCondition"
    ]
    """<p>A numeric comparison condition.</p>"""
    string_condition: NotRequired[
        "capo_connect.types.metric_filter_string_condition.MetricFilterStringCondition"
    ]
    """<p>A string comparison condition.</p>"""
    boolean_condition: NotRequired[
        "capo_connect.types.metric_filter_boolean_condition.MetricFilterBooleanCondition"
    ]
    """<p>A boolean comparison condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilter) -> dict:
    out: dict = {}
    out["MetricFilterKey"] = value["metric_filter_key"]
    out["Negate"] = value.get("negate", False)
    if "number_condition" in value:
        import capo_connect.types.metric_filter_number_condition

        out["NumberCondition"] = (
            capo_connect.types.metric_filter_number_condition.serialize_json(
                value["number_condition"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.metric_filter_string_condition

        out["StringCondition"] = (
            capo_connect.types.metric_filter_string_condition.serialize_json(
                value["string_condition"]
            )
        )
    if "boolean_condition" in value:
        import capo_connect.types.metric_filter_boolean_condition

        out["BooleanCondition"] = (
            capo_connect.types.metric_filter_boolean_condition.serialize_json(
                value["boolean_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricFilter:
    out: MetricFilter = {}  # type: ignore[typeddict-item]
    if data.get("MetricFilterKey") is not None:
        out["metric_filter_key"] = data["MetricFilterKey"]
    else:
        out["metric_filter_key"] = ""
    if data.get("Negate") is not None:
        out["negate"] = data["Negate"]
    else:
        out["negate"] = False
    if data.get("NumberCondition") is not None:
        import capo_connect.types.metric_filter_number_condition

        out["number_condition"] = (
            capo_connect.types.metric_filter_number_condition.deserialize_json(
                data["NumberCondition"]
            )
        )
    if data.get("StringCondition") is not None:
        import capo_connect.types.metric_filter_string_condition

        out["string_condition"] = (
            capo_connect.types.metric_filter_string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    if data.get("BooleanCondition") is not None:
        import capo_connect.types.metric_filter_boolean_condition

        out["boolean_condition"] = (
            capo_connect.types.metric_filter_boolean_condition.deserialize_json(
                data["BooleanCondition"]
            )
        )
    return out
