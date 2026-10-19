"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_auto_scaler_type
    import capo_sagemaker.types.cluster_auto_scaling_mode


class ClusterAutoScalingConfig(TypedDict, closed=True):
    mode: "capo_sagemaker.types.cluster_auto_scaling_mode.ClusterAutoScalingMode"
    """<p>Describes whether autoscaling is enabled or disabled for the cluster. Valid values are <code>Enable</code> and <code>Disable</code>.</p>"""
    auto_scaler_type: NotRequired[
        "capo_sagemaker.types.cluster_auto_scaler_type.ClusterAutoScalerType"
    ]
    """<p>The type of autoscaler to use. Currently supported value is <code>Karpenter</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalingConfig) -> dict:
    out: dict = {}
    import capo_sagemaker.types.cluster_auto_scaling_mode

    out["Mode"] = capo_sagemaker.types.cluster_auto_scaling_mode.serialize_aws_json_1_1(
        value["mode"]
    )
    if "auto_scaler_type" in value:
        import capo_sagemaker.types.cluster_auto_scaler_type

        out["AutoScalerType"] = (
            capo_sagemaker.types.cluster_auto_scaler_type.serialize_aws_json_1_1(
                value["auto_scaler_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAutoScalingConfig:
    out: ClusterAutoScalingConfig = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_sagemaker.types.cluster_auto_scaling_mode

        out["mode"] = (
            capo_sagemaker.types.cluster_auto_scaling_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_sagemaker.types.cluster_auto_scaling_mode.ClusterAutoScalingMode", ""
        )
    if data.get("AutoScalerType") is not None:
        import capo_sagemaker.types.cluster_auto_scaler_type

        out["auto_scaler_type"] = (
            capo_sagemaker.types.cluster_auto_scaler_type.deserialize_aws_json_1_1(
                data["AutoScalerType"]
            )
        )
    return out
