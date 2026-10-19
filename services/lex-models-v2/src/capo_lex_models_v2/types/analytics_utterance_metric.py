"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_metric_statistic
    import capo_lex_models_v2.types.analytics_sort_order
    import capo_lex_models_v2.types.analytics_utterance_metric_name


class AnalyticsUtteranceMetric(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_utterance_metric_name.AnalyticsUtteranceMetricName"
    """<p>The metric for which you want to get utterance summary statistics.</p> <ul> <li> <p> <code>Count</code> – The number of utterances.</p> </li> <li> <p> <code>Missed</code> – The number of utterances that Amazon Lex failed to recognize.</p> </li> <li> <p> <code>Detected</code> – The number of utterances that Amazon Lex managed to detect.</p> </li> <li> <p> <code>UtteranceTimestamp</code> – The date and time of the utterance.</p> </li> </ul>"""
    statistic: (
        "capo_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    )
    """<p>The summary statistic to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of utterances in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    order: NotRequired[
        "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetric) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_utterance_metric_name

    out["name"] = (
        capo_lex_models_v2.types.analytics_utterance_metric_name.serialize_json(
            value["name"]
        )
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


def deserialize_json(data: dict) -> AnalyticsUtteranceMetric:
    out: AnalyticsUtteranceMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_utterance_metric_name

        out["name"] = (
            capo_lex_models_v2.types.analytics_utterance_metric_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_utterance_metric_name.AnalyticsUtteranceMetricName",
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
