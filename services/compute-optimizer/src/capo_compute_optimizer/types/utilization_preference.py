"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.customizable_metric_name
    import capo_compute_optimizer.types.customizable_metric_parameters


class UtilizationPreference(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_compute_optimizer.types.customizable_metric_name.CustomizableMetricName"
    ]
    """<p> The name of the resource utilization metric name to customize. </p>"""
    metric_parameters: NotRequired[
        "capo_compute_optimizer.types.customizable_metric_parameters.CustomizableMetricParameters"
    ]
    """<p> The parameters to set when customizing the resource utilization thresholds. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationPreference) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import capo_compute_optimizer.types.customizable_metric_name

        out["metricName"] = (
            capo_compute_optimizer.types.customizable_metric_name.serialize_aws_json_1_0(
                value["metric_name"]
            )
        )
    if "metric_parameters" in value:
        import capo_compute_optimizer.types.customizable_metric_parameters

        out["metricParameters"] = (
            capo_compute_optimizer.types.customizable_metric_parameters.serialize_aws_json_1_0(
                value["metric_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UtilizationPreference:
    out: UtilizationPreference = {}  # type: ignore[typeddict-item]
    if data.get("metricName") is not None:
        import capo_compute_optimizer.types.customizable_metric_name

        out["metric_name"] = (
            capo_compute_optimizer.types.customizable_metric_name.deserialize_aws_json_1_0(
                data["metricName"]
            )
        )
    if data.get("metricParameters") is not None:
        import capo_compute_optimizer.types.customizable_metric_parameters

        out["metric_parameters"] = (
            capo_compute_optimizer.types.customizable_metric_parameters.deserialize_aws_json_1_0(
                data["metricParameters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UtilizationPreference) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import capo_compute_optimizer.types.customizable_metric_name

        out["metricName"] = (
            capo_compute_optimizer.types.customizable_metric_name.serialize_cbor(
                value["metric_name"]
            )
        )
    if "metric_parameters" in value:
        import capo_compute_optimizer.types.customizable_metric_parameters

        out["metricParameters"] = (
            capo_compute_optimizer.types.customizable_metric_parameters.serialize_cbor(
                value["metric_parameters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UtilizationPreference:
    out: UtilizationPreference = {}  # type: ignore[typeddict-item]
    if data.get("metricName") is not None:
        import capo_compute_optimizer.types.customizable_metric_name

        out["metric_name"] = (
            capo_compute_optimizer.types.customizable_metric_name.deserialize_cbor(
                data["metricName"]
            )
        )
    if data.get("metricParameters") is not None:
        import capo_compute_optimizer.types.customizable_metric_parameters

        out["metric_parameters"] = (
            capo_compute_optimizer.types.customizable_metric_parameters.deserialize_cbor(
                data["metricParameters"]
            )
        )
    return out
