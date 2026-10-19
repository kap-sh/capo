"""Generated from Smithy shape ``com.amazonaws.lambda#TargetTrackingScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_predefined_metric_type
    import capo_lambda.types.metric_target_value


class TargetTrackingScalingPolicy(TypedDict, closed=True):
    predefined_metric_type: "capo_lambda.types.capacity_provider_predefined_metric_type.CapacityProviderPredefinedMetricType"
    """<p>The predefined metric type to track for scaling decisions.</p>"""
    target_value: "capo_lambda.types.metric_target_value.MetricTargetValue"
    """<p>The target value for the metric that the scaling policy attempts to maintain through scaling actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetTrackingScalingPolicy) -> dict:
    out: dict = {}
    import capo_lambda.types.capacity_provider_predefined_metric_type

    out["PredefinedMetricType"] = (
        capo_lambda.types.capacity_provider_predefined_metric_type.serialize_json(
            value["predefined_metric_type"]
        )
    )
    out["TargetValue"] = (
        "NaN"
        if value["target_value"] != value["target_value"]
        else "Infinity"
        if value["target_value"] == float("inf")
        else "-Infinity"
        if value["target_value"] == float("-inf")
        else value["target_value"]
    )
    return out


def deserialize_json(data: dict) -> TargetTrackingScalingPolicy:
    out: TargetTrackingScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("PredefinedMetricType") is not None:
        import capo_lambda.types.capacity_provider_predefined_metric_type

        out["predefined_metric_type"] = (
            capo_lambda.types.capacity_provider_predefined_metric_type.deserialize_json(
                data["PredefinedMetricType"]
            )
        )
    else:
        import typing

        out["predefined_metric_type"] = typing.cast(
            "capo_lambda.types.capacity_provider_predefined_metric_type.CapacityProviderPredefinedMetricType",
            "",
        )
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    else:
        out["target_value"] = 0.0
    return out
