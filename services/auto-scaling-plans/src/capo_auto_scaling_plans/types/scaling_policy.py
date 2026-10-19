"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.policy_name
    import capo_auto_scaling_plans.types.policy_type
    import capo_auto_scaling_plans.types.target_tracking_configuration


class ScalingPolicy(TypedDict, closed=True):
    policy_name: "capo_auto_scaling_plans.types.policy_name.PolicyName"
    """<p>The name of the scaling policy.</p>"""
    policy_type: "capo_auto_scaling_plans.types.policy_type.PolicyType"
    """<p>The type of scaling policy.</p>"""
    target_tracking_configuration: NotRequired[
        "capo_auto_scaling_plans.types.target_tracking_configuration.TargetTrackingConfiguration"
    ]
    """<p>The target tracking scaling policy. Includes support for predefined or customized metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicy) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    import capo_auto_scaling_plans.types.policy_type

    out["PolicyType"] = (
        capo_auto_scaling_plans.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "target_tracking_configuration" in value:
        import capo_auto_scaling_plans.types.target_tracking_configuration

        out["TargetTrackingConfiguration"] = (
            capo_auto_scaling_plans.types.target_tracking_configuration.serialize_aws_json_1_1(
                value["target_tracking_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicy:
    out: ScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("PolicyType") is not None:
        import capo_auto_scaling_plans.types.policy_type

        out["policy_type"] = (
            capo_auto_scaling_plans.types.policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        import typing

        out["policy_type"] = typing.cast(
            "capo_auto_scaling_plans.types.policy_type.PolicyType", ""
        )
    if data.get("TargetTrackingConfiguration") is not None:
        import capo_auto_scaling_plans.types.target_tracking_configuration

        out["target_tracking_configuration"] = (
            capo_auto_scaling_plans.types.target_tracking_configuration.deserialize_aws_json_1_1(
                data["TargetTrackingConfiguration"]
            )
        )
    return out
