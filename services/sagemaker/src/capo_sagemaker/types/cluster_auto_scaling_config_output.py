"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_auto_scaler_type
    import capo_sagemaker.types.cluster_auto_scaling_mode
    import capo_sagemaker.types.cluster_auto_scaling_status


class ClusterAutoScalingConfigOutput(TypedDict, closed=True):
    mode: "capo_sagemaker.types.cluster_auto_scaling_mode.ClusterAutoScalingMode"
    """<p>Describes whether autoscaling is enabled or disabled for the cluster.</p>"""
    auto_scaler_type: NotRequired[
        "capo_sagemaker.types.cluster_auto_scaler_type.ClusterAutoScalerType"
    ]
    """<p>The type of autoscaler configured for the cluster.</p>"""
    status: "capo_sagemaker.types.cluster_auto_scaling_status.ClusterAutoScalingStatus"
    """<p>The current status of the autoscaling configuration. Valid values are <code>InService</code>, <code>Failed</code>, <code>Creating</code>, and <code>Deleting</code>.</p>"""
    failure_message: NotRequired["str"]
    """<p>If the autoscaling status is <code>Failed</code>, this field contains a message describing the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalingConfigOutput) -> dict:
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
    import capo_sagemaker.types.cluster_auto_scaling_status

    out["Status"] = (
        capo_sagemaker.types.cluster_auto_scaling_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAutoScalingConfigOutput:
    out: ClusterAutoScalingConfigOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("Status") is not None:
        import capo_sagemaker.types.cluster_auto_scaling_status

        out["status"] = (
            capo_sagemaker.types.cluster_auto_scaling_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_sagemaker.types.cluster_auto_scaling_status.ClusterAutoScalingStatus",
            "",
        )
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    return out
