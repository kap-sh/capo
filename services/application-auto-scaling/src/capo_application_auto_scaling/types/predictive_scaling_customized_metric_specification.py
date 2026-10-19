"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingCustomizedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_metric_data_queries


class PredictiveScalingCustomizedMetricSpecification(TypedDict, closed=True):
    metric_data_queries: "capo_application_auto_scaling.types.predictive_scaling_metric_data_queries.PredictiveScalingMetricDataQueries"
    """<p> One or more metric data queries to provide data points for a metric specification. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PredictiveScalingCustomizedMetricSpecification,
) -> dict:
    out: dict = {}
    import capo_application_auto_scaling.types.predictive_scaling_metric_data_queries

    out["MetricDataQueries"] = (
        capo_application_auto_scaling.types.predictive_scaling_metric_data_queries.serialize_aws_json_1_1(
            value["metric_data_queries"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PredictiveScalingCustomizedMetricSpecification:
    out: PredictiveScalingCustomizedMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataQueries") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_metric_data_queries

        out["metric_data_queries"] = (
            capo_application_auto_scaling.types.predictive_scaling_metric_data_queries.deserialize_aws_json_1_1(
                data["MetricDataQueries"]
            )
        )
    else:
        out["metric_data_queries"] = []
    return out
