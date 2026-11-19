"""Generated from Smithy shape ``com.amazonaws.codebuild#TargetTrackingScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_scaling_metric_type
    import capo_codebuild.types.wrapper_double


class TargetTrackingScalingConfiguration(TypedDict, closed=True):
    metric_type: NotRequired[
        "capo_codebuild.types.fleet_scaling_metric_type.FleetScalingMetricType"
    ]
    """<p>The metric type to determine auto-scaling.</p>"""
    target_value: NotRequired["capo_codebuild.types.wrapper_double.WrapperDouble"]
    """<p>The value of <code>metricType</code> when to start scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingScalingConfiguration) -> dict:
    out: dict = {}
    if "metric_type" in value:
        import capo_codebuild.types.fleet_scaling_metric_type

        out["metricType"] = (
            capo_codebuild.types.fleet_scaling_metric_type.serialize_aws_json_1_1(
                value["metric_type"]
            )
        )
    if "target_value" in value:
        out["targetValue"] = (
            "NaN"
            if value["target_value"] != value["target_value"]
            else "Infinity"
            if value["target_value"] == float("inf")
            else "-Infinity"
            if value["target_value"] == float("-inf")
            else value["target_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingScalingConfiguration:
    out: TargetTrackingScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metricType") is not None:
        import capo_codebuild.types.fleet_scaling_metric_type

        out["metric_type"] = (
            capo_codebuild.types.fleet_scaling_metric_type.deserialize_aws_json_1_1(
                data["metricType"]
            )
        )
    if data.get("targetValue") is not None:
        out["target_value"] = float(data["targetValue"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetTrackingScalingConfiguration) -> dict:
    out: dict = {}
    if "metric_type" in value:
        import capo_codebuild.types.fleet_scaling_metric_type

        out["metricType"] = (
            capo_codebuild.types.fleet_scaling_metric_type.serialize_cbor(
                value["metric_type"]
            )
        )
    if "target_value" in value:
        out["targetValue"] = value["target_value"]
    return out


def deserialize_cbor(data: dict) -> TargetTrackingScalingConfiguration:
    out: TargetTrackingScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metricType") is not None:
        import capo_codebuild.types.fleet_scaling_metric_type

        out["metric_type"] = (
            capo_codebuild.types.fleet_scaling_metric_type.deserialize_cbor(
                data["metricType"]
            )
        )
    if data.get("targetValue") is not None:
        out["target_value"] = float(data["targetValue"])
    return out
