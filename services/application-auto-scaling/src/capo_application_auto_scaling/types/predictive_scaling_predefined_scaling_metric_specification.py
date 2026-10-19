"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingPredefinedScalingMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_metric_type
    import capo_application_auto_scaling.types.resource_label


class PredictiveScalingPredefinedScalingMetricSpecification(TypedDict, closed=True):
    predefined_metric_type: "capo_application_auto_scaling.types.predictive_scaling_metric_type.PredictiveScalingMetricType"
    """<p> The metric type. </p>"""
    resource_label: NotRequired[
        "capo_application_auto_scaling.types.resource_label.ResourceLabel"
    ]
    """<p> A label that uniquely identifies a specific target group from which to determine the average request count. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PredictiveScalingPredefinedScalingMetricSpecification,
) -> dict:
    out: dict = {}
    out["PredefinedMetricType"] = value["predefined_metric_type"]
    if "resource_label" in value:
        out["ResourceLabel"] = value["resource_label"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PredictiveScalingPredefinedScalingMetricSpecification:
    out: PredictiveScalingPredefinedScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("PredefinedMetricType") is not None:
        out["predefined_metric_type"] = data["PredefinedMetricType"]
    else:
        out["predefined_metric_type"] = ""
    if data.get("ResourceLabel") is not None:
        out["resource_label"] = data["ResourceLabel"]
    return out
