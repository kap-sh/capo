"""Generated from Smithy shape ``com.amazonaws.codebuild#TargetTrackingScalingConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.target_tracking_scaling_configuration

TargetTrackingScalingConfigurations: TypeAlias = list[
    "capo_codebuild.types.target_tracking_scaling_configuration.TargetTrackingScalingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingScalingConfigurations) -> list:
    import capo_codebuild.types.target_tracking_scaling_configuration

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.target_tracking_scaling_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetTrackingScalingConfigurations:
    import capo_codebuild.types.target_tracking_scaling_configuration

    out: TargetTrackingScalingConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.target_tracking_scaling_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetTrackingScalingConfigurations) -> list:
    import capo_codebuild.types.target_tracking_scaling_configuration

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.target_tracking_scaling_configuration.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> TargetTrackingScalingConfigurations:
    import capo_codebuild.types.target_tracking_scaling_configuration

    out: TargetTrackingScalingConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.target_tracking_scaling_configuration.deserialize_cbor(
                item
            )
        )
    return out
