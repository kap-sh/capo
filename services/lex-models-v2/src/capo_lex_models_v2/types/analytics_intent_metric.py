"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_metric_name
    import capo_lex_models_v2.types.analytics_metric_statistic
    import capo_lex_models_v2.types.analytics_sort_order


class AnalyticsIntentMetric(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_intent_metric_name.AnalyticsIntentMetricName"
    """<p>The metric for which you want to get intent summary statistics.</p> <ul> <li> <p> <code>Count</code> – The number of times the intent was invoked.</p> </li> <li> <p> <code>Success</code> – The number of times the intent succeeded.</p> </li> <li> <p> <code>Failure</code> – The number of times the intent failed.</p> </li> <li> <p> <code>Switched</code> – The number of times there was a switch to a different intent.</p> </li> <li> <p> <code>Dropped</code> – The number of times the user dropped the intent.</p> </li> </ul>"""
    statistic: (
        "capo_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    )
    """<p>The summary statistic to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of intents in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    order: NotRequired[
        "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetric) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_intent_metric_name

    out["name"] = capo_lex_models_v2.types.analytics_intent_metric_name.serialize_json(
        value["name"]
    )
    import capo_lex_models_v2.types.analytics_metric_statistic

    out["statistic"] = (
        capo_lex_models_v2.types.analytics_metric_statistic.serialize_json(
            value["statistic"]
        )
    )
    if "order" in value:
        import capo_lex_models_v2.types.analytics_sort_order

        out["order"] = capo_lex_models_v2.types.analytics_sort_order.serialize_json(
            value["order"]
        )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentMetric:
    out: AnalyticsIntentMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_intent_metric_name

        out["name"] = (
            capo_lex_models_v2.types.analytics_intent_metric_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_intent_metric_name.AnalyticsIntentMetricName",
            "",
        )
    if data.get("statistic") is not None:
        import capo_lex_models_v2.types.analytics_metric_statistic

        out["statistic"] = (
            capo_lex_models_v2.types.analytics_metric_statistic.deserialize_json(
                data["statistic"]
            )
        )
    else:
        import typing

        out["statistic"] = typing.cast(
            "capo_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic",
            "",
        )
    if data.get("order") is not None:
        import capo_lex_models_v2.types.analytics_sort_order

        out["order"] = capo_lex_models_v2.types.analytics_sort_order.deserialize_json(
            data["order"]
        )
    return out
