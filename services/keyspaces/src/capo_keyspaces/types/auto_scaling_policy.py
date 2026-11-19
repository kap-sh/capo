"""Generated from Smithy shape ``com.amazonaws.keyspaces#AutoScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.target_tracking_scaling_policy_configuration


class AutoScalingPolicy(TypedDict, closed=True):
    target_tracking_scaling_policy_configuration: NotRequired[
        "capo_keyspaces.types.target_tracking_scaling_policy_configuration.TargetTrackingScalingPolicyConfiguration"
    ]
    """<p>Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A <code>double</code> between 20 and 90.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingPolicy) -> dict:
    out: dict = {}
    if "target_tracking_scaling_policy_configuration" in value:
        import capo_keyspaces.types.target_tracking_scaling_policy_configuration

        out["targetTrackingScalingPolicyConfiguration"] = (
            capo_keyspaces.types.target_tracking_scaling_policy_configuration.serialize_aws_json_1_0(
                value["target_tracking_scaling_policy_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingPolicy:
    out: AutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("targetTrackingScalingPolicyConfiguration") is not None:
        import capo_keyspaces.types.target_tracking_scaling_policy_configuration

        out["target_tracking_scaling_policy_configuration"] = (
            capo_keyspaces.types.target_tracking_scaling_policy_configuration.deserialize_aws_json_1_0(
                data["targetTrackingScalingPolicyConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingPolicy) -> dict:
    out: dict = {}
    if "target_tracking_scaling_policy_configuration" in value:
        import capo_keyspaces.types.target_tracking_scaling_policy_configuration

        out["targetTrackingScalingPolicyConfiguration"] = (
            capo_keyspaces.types.target_tracking_scaling_policy_configuration.serialize_cbor(
                value["target_tracking_scaling_policy_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutoScalingPolicy:
    out: AutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("targetTrackingScalingPolicyConfiguration") is not None:
        import capo_keyspaces.types.target_tracking_scaling_policy_configuration

        out["target_tracking_scaling_policy_configuration"] = (
            capo_keyspaces.types.target_tracking_scaling_policy_configuration.deserialize_cbor(
                data["targetTrackingScalingPolicyConfiguration"]
            )
        )
    return out
