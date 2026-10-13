"""Generated from Smithy shape ``com.amazonaws.quicksight#Computation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.forecast_computation
    import capo_quicksight.types.growth_rate_computation
    import capo_quicksight.types.maximum_minimum_computation
    import capo_quicksight.types.metric_comparison_computation
    import capo_quicksight.types.period_over_period_computation
    import capo_quicksight.types.period_to_date_computation
    import capo_quicksight.types.top_bottom_movers_computation
    import capo_quicksight.types.top_bottom_ranked_computation
    import capo_quicksight.types.total_aggregation_computation
    import capo_quicksight.types.unique_values_computation


class Computation(TypedDict, closed=True):
    top_bottom_ranked: NotRequired[
        "capo_quicksight.types.top_bottom_ranked_computation.TopBottomRankedComputation"
    ]
    """<p>The top ranked and bottom ranked computation configuration.</p>"""
    top_bottom_movers: NotRequired[
        "capo_quicksight.types.top_bottom_movers_computation.TopBottomMoversComputation"
    ]
    """<p>The top movers and bottom movers computation configuration.</p>"""
    total_aggregation: NotRequired[
        "capo_quicksight.types.total_aggregation_computation.TotalAggregationComputation"
    ]
    """<p>The total aggregation computation configuration.</p>"""
    maximum_minimum: NotRequired[
        "capo_quicksight.types.maximum_minimum_computation.MaximumMinimumComputation"
    ]
    """<p>The maximum and minimum computation configuration.</p>"""
    metric_comparison: NotRequired[
        "capo_quicksight.types.metric_comparison_computation.MetricComparisonComputation"
    ]
    """<p>The metric comparison computation configuration.</p>"""
    period_over_period: NotRequired[
        "capo_quicksight.types.period_over_period_computation.PeriodOverPeriodComputation"
    ]
    """<p>The period over period computation configuration.</p>"""
    period_to_date: NotRequired[
        "capo_quicksight.types.period_to_date_computation.PeriodToDateComputation"
    ]
    """<p>The period to <code>DataSetIdentifier</code> computation configuration.</p>"""
    growth_rate: NotRequired[
        "capo_quicksight.types.growth_rate_computation.GrowthRateComputation"
    ]
    """<p>The growth rate computation configuration.</p>"""
    unique_values: NotRequired[
        "capo_quicksight.types.unique_values_computation.UniqueValuesComputation"
    ]
    """<p>The unique values computation configuration.</p>"""
    forecast: NotRequired[
        "capo_quicksight.types.forecast_computation.ForecastComputation"
    ]
    """<p>The forecast computation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Computation) -> dict:
    out: dict = {}
    if "top_bottom_ranked" in value:
        import capo_quicksight.types.top_bottom_ranked_computation

        out["TopBottomRanked"] = (
            capo_quicksight.types.top_bottom_ranked_computation.serialize_json(
                value["top_bottom_ranked"]
            )
        )
    if "top_bottom_movers" in value:
        import capo_quicksight.types.top_bottom_movers_computation

        out["TopBottomMovers"] = (
            capo_quicksight.types.top_bottom_movers_computation.serialize_json(
                value["top_bottom_movers"]
            )
        )
    if "total_aggregation" in value:
        import capo_quicksight.types.total_aggregation_computation

        out["TotalAggregation"] = (
            capo_quicksight.types.total_aggregation_computation.serialize_json(
                value["total_aggregation"]
            )
        )
    if "maximum_minimum" in value:
        import capo_quicksight.types.maximum_minimum_computation

        out["MaximumMinimum"] = (
            capo_quicksight.types.maximum_minimum_computation.serialize_json(
                value["maximum_minimum"]
            )
        )
    if "metric_comparison" in value:
        import capo_quicksight.types.metric_comparison_computation

        out["MetricComparison"] = (
            capo_quicksight.types.metric_comparison_computation.serialize_json(
                value["metric_comparison"]
            )
        )
    if "period_over_period" in value:
        import capo_quicksight.types.period_over_period_computation

        out["PeriodOverPeriod"] = (
            capo_quicksight.types.period_over_period_computation.serialize_json(
                value["period_over_period"]
            )
        )
    if "period_to_date" in value:
        import capo_quicksight.types.period_to_date_computation

        out["PeriodToDate"] = (
            capo_quicksight.types.period_to_date_computation.serialize_json(
                value["period_to_date"]
            )
        )
    if "growth_rate" in value:
        import capo_quicksight.types.growth_rate_computation

        out["GrowthRate"] = (
            capo_quicksight.types.growth_rate_computation.serialize_json(
                value["growth_rate"]
            )
        )
    if "unique_values" in value:
        import capo_quicksight.types.unique_values_computation

        out["UniqueValues"] = (
            capo_quicksight.types.unique_values_computation.serialize_json(
                value["unique_values"]
            )
        )
    if "forecast" in value:
        import capo_quicksight.types.forecast_computation

        out["Forecast"] = capo_quicksight.types.forecast_computation.serialize_json(
            value["forecast"]
        )
    return out


def deserialize_json(data: dict) -> Computation:
    out: Computation = {}  # type: ignore[typeddict-item]
    if data.get("TopBottomRanked") is not None:
        import capo_quicksight.types.top_bottom_ranked_computation

        out["top_bottom_ranked"] = (
            capo_quicksight.types.top_bottom_ranked_computation.deserialize_json(
                data["TopBottomRanked"]
            )
        )
    if data.get("TopBottomMovers") is not None:
        import capo_quicksight.types.top_bottom_movers_computation

        out["top_bottom_movers"] = (
            capo_quicksight.types.top_bottom_movers_computation.deserialize_json(
                data["TopBottomMovers"]
            )
        )
    if data.get("TotalAggregation") is not None:
        import capo_quicksight.types.total_aggregation_computation

        out["total_aggregation"] = (
            capo_quicksight.types.total_aggregation_computation.deserialize_json(
                data["TotalAggregation"]
            )
        )
    if data.get("MaximumMinimum") is not None:
        import capo_quicksight.types.maximum_minimum_computation

        out["maximum_minimum"] = (
            capo_quicksight.types.maximum_minimum_computation.deserialize_json(
                data["MaximumMinimum"]
            )
        )
    if data.get("MetricComparison") is not None:
        import capo_quicksight.types.metric_comparison_computation

        out["metric_comparison"] = (
            capo_quicksight.types.metric_comparison_computation.deserialize_json(
                data["MetricComparison"]
            )
        )
    if data.get("PeriodOverPeriod") is not None:
        import capo_quicksight.types.period_over_period_computation

        out["period_over_period"] = (
            capo_quicksight.types.period_over_period_computation.deserialize_json(
                data["PeriodOverPeriod"]
            )
        )
    if data.get("PeriodToDate") is not None:
        import capo_quicksight.types.period_to_date_computation

        out["period_to_date"] = (
            capo_quicksight.types.period_to_date_computation.deserialize_json(
                data["PeriodToDate"]
            )
        )
    if data.get("GrowthRate") is not None:
        import capo_quicksight.types.growth_rate_computation

        out["growth_rate"] = (
            capo_quicksight.types.growth_rate_computation.deserialize_json(
                data["GrowthRate"]
            )
        )
    if data.get("UniqueValues") is not None:
        import capo_quicksight.types.unique_values_computation

        out["unique_values"] = (
            capo_quicksight.types.unique_values_computation.deserialize_json(
                data["UniqueValues"]
            )
        )
    if data.get("Forecast") is not None:
        import capo_quicksight.types.forecast_computation

        out["forecast"] = capo_quicksight.types.forecast_computation.deserialize_json(
            data["Forecast"]
        )
    return out


def redact_sensitive(value: Computation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "top_bottom_ranked" in value:
        import capo_quicksight.types.top_bottom_ranked_computation

        out["top_bottom_ranked"] = (
            capo_quicksight.types.top_bottom_ranked_computation.redact_sensitive(
                value["top_bottom_ranked"]
            )
        )
    if "top_bottom_movers" in value:
        import capo_quicksight.types.top_bottom_movers_computation

        out["top_bottom_movers"] = (
            capo_quicksight.types.top_bottom_movers_computation.redact_sensitive(
                value["top_bottom_movers"]
            )
        )
    if "total_aggregation" in value:
        import capo_quicksight.types.total_aggregation_computation

        out["total_aggregation"] = (
            capo_quicksight.types.total_aggregation_computation.redact_sensitive(
                value["total_aggregation"]
            )
        )
    if "maximum_minimum" in value:
        import capo_quicksight.types.maximum_minimum_computation

        out["maximum_minimum"] = (
            capo_quicksight.types.maximum_minimum_computation.redact_sensitive(
                value["maximum_minimum"]
            )
        )
    if "metric_comparison" in value:
        import capo_quicksight.types.metric_comparison_computation

        out["metric_comparison"] = (
            capo_quicksight.types.metric_comparison_computation.redact_sensitive(
                value["metric_comparison"]
            )
        )
    if "period_over_period" in value:
        import capo_quicksight.types.period_over_period_computation

        out["period_over_period"] = (
            capo_quicksight.types.period_over_period_computation.redact_sensitive(
                value["period_over_period"]
            )
        )
    if "period_to_date" in value:
        import capo_quicksight.types.period_to_date_computation

        out["period_to_date"] = (
            capo_quicksight.types.period_to_date_computation.redact_sensitive(
                value["period_to_date"]
            )
        )
    if "growth_rate" in value:
        import capo_quicksight.types.growth_rate_computation

        out["growth_rate"] = (
            capo_quicksight.types.growth_rate_computation.redact_sensitive(
                value["growth_rate"]
            )
        )
    if "unique_values" in value:
        import capo_quicksight.types.unique_values_computation

        out["unique_values"] = (
            capo_quicksight.types.unique_values_computation.redact_sensitive(
                value["unique_values"]
            )
        )
    if "forecast" in value:
        import capo_quicksight.types.forecast_computation

        out["forecast"] = capo_quicksight.types.forecast_computation.redact_sensitive(
            value["forecast"]
        )
    return out
