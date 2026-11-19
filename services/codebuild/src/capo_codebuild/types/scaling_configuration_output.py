"""Generated from Smithy shape ``com.amazonaws.codebuild#ScalingConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_capacity
    import capo_codebuild.types.fleet_scaling_type
    import capo_codebuild.types.target_tracking_scaling_configurations


class ScalingConfigurationOutput(TypedDict, closed=True):
    scaling_type: NotRequired[
        "capo_codebuild.types.fleet_scaling_type.FleetScalingType"
    ]
    """<p>The scaling type for a compute fleet.</p>"""
    target_tracking_scaling_configs: NotRequired[
        "capo_codebuild.types.target_tracking_scaling_configurations.TargetTrackingScalingConfigurations"
    ]
    """<p>A list of <code>TargetTrackingScalingConfiguration</code> objects.</p>"""
    max_capacity: NotRequired["capo_codebuild.types.fleet_capacity.FleetCapacity"]
    """<p>The maximum number of instances in the ﬂeet when auto-scaling.</p>"""
    desired_capacity: NotRequired["capo_codebuild.types.fleet_capacity.FleetCapacity"]
    """<p>The desired number of instances in the ﬂeet when auto-scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingConfigurationOutput) -> dict:
    out: dict = {}
    if "scaling_type" in value:
        import capo_codebuild.types.fleet_scaling_type

        out["scalingType"] = (
            capo_codebuild.types.fleet_scaling_type.serialize_aws_json_1_1(
                value["scaling_type"]
            )
        )
    if "target_tracking_scaling_configs" in value:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["targetTrackingScalingConfigs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.serialize_aws_json_1_1(
                value["target_tracking_scaling_configs"]
            )
        )
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "desired_capacity" in value:
        out["desiredCapacity"] = value["desired_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingConfigurationOutput:
    out: ScalingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("scalingType") is not None:
        import capo_codebuild.types.fleet_scaling_type

        out["scaling_type"] = (
            capo_codebuild.types.fleet_scaling_type.deserialize_aws_json_1_1(
                data["scalingType"]
            )
        )
    if data.get("targetTrackingScalingConfigs") is not None:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["target_tracking_scaling_configs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.deserialize_aws_json_1_1(
                data["targetTrackingScalingConfigs"]
            )
        )
    if data.get("maxCapacity") is not None:
        out["max_capacity"] = data["maxCapacity"]
    if data.get("desiredCapacity") is not None:
        out["desired_capacity"] = data["desiredCapacity"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScalingConfigurationOutput) -> dict:
    out: dict = {}
    if "scaling_type" in value:
        import capo_codebuild.types.fleet_scaling_type

        out["scalingType"] = capo_codebuild.types.fleet_scaling_type.serialize_cbor(
            value["scaling_type"]
        )
    if "target_tracking_scaling_configs" in value:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["targetTrackingScalingConfigs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.serialize_cbor(
                value["target_tracking_scaling_configs"]
            )
        )
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "desired_capacity" in value:
        out["desiredCapacity"] = value["desired_capacity"]
    return out


def deserialize_cbor(data: dict) -> ScalingConfigurationOutput:
    out: ScalingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("scalingType") is not None:
        import capo_codebuild.types.fleet_scaling_type

        out["scaling_type"] = capo_codebuild.types.fleet_scaling_type.deserialize_cbor(
            data["scalingType"]
        )
    if data.get("targetTrackingScalingConfigs") is not None:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["target_tracking_scaling_configs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.deserialize_cbor(
                data["targetTrackingScalingConfigs"]
            )
        )
    if data.get("maxCapacity") is not None:
        out["max_capacity"] = data["maxCapacity"]
    if data.get("desiredCapacity") is not None:
        out["desired_capacity"] = data["desiredCapacity"]
    return out
