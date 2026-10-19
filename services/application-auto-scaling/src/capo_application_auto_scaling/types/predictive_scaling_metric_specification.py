"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_scale
    import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification
    import capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification
    import capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification
    import capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification


class PredictiveScalingMetricSpecification(TypedDict, closed=True):
    target_value: "capo_application_auto_scaling.types.metric_scale.MetricScale"
    """<p> Specifies the target utilization. </p>"""
    predefined_metric_pair_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.PredictiveScalingPredefinedMetricPairSpecification"
    ]
    """<p> The predefined metric pair specification that determines the appropriate scaling metric and load metric to use. </p>"""
    predefined_scaling_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.PredictiveScalingPredefinedScalingMetricSpecification"
    ]
    """<p> The predefined scaling metric specification. </p>"""
    predefined_load_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.PredictiveScalingPredefinedLoadMetricSpecification"
    ]
    """<p> The predefined load metric specification. </p>"""
    customized_scaling_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized scaling metric specification. </p>"""
    customized_load_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized load metric specification. </p>"""
    customized_capacity_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized capacity metric specification. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricSpecification) -> dict:
    out: dict = {}
    out["TargetValue"] = (
        "NaN"
        if value["target_value"] != value["target_value"]
        else "Infinity"
        if value["target_value"] == float("inf")
        else "-Infinity"
        if value["target_value"] == float("-inf")
        else value["target_value"]
    )
    if "predefined_metric_pair_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification

        out["PredefinedMetricPairSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.serialize_aws_json_1_1(
                value["predefined_metric_pair_specification"]
            )
        )
    if "predefined_scaling_metric_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification

        out["PredefinedScalingMetricSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.serialize_aws_json_1_1(
                value["predefined_scaling_metric_specification"]
            )
        )
    if "predefined_load_metric_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification

        out["PredefinedLoadMetricSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.serialize_aws_json_1_1(
                value["predefined_load_metric_specification"]
            )
        )
    if "customized_scaling_metric_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedScalingMetricSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_scaling_metric_specification"]
            )
        )
    if "customized_load_metric_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedLoadMetricSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_load_metric_specification"]
            )
        )
    if "customized_capacity_metric_specification" in value:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedCapacityMetricSpecification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_capacity_metric_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingMetricSpecification:
    out: PredictiveScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    else:
        out["target_value"] = 0.0
    if data.get("PredefinedMetricPairSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification

        out["predefined_metric_pair_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.deserialize_aws_json_1_1(
                data["PredefinedMetricPairSpecification"]
            )
        )
    if data.get("PredefinedScalingMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification

        out["predefined_scaling_metric_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedScalingMetricSpecification"]
            )
        )
    if data.get("PredefinedLoadMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification

        out["predefined_load_metric_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedLoadMetricSpecification"]
            )
        )
    if data.get("CustomizedScalingMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_scaling_metric_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedScalingMetricSpecification"]
            )
        )
    if data.get("CustomizedLoadMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_load_metric_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedLoadMetricSpecification"]
            )
        )
    if data.get("CustomizedCapacityMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_capacity_metric_specification"] = (
            capo_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedCapacityMetricSpecification"]
            )
        )
    return out
