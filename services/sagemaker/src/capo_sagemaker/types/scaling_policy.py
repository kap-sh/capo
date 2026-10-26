"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScalingPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.target_tracking_scaling_policy_configuration


class _ScalingPolicy_TargetTracking(TypedDict, closed=True):
    TargetTracking: "capo_sagemaker.types.target_tracking_scaling_policy_configuration.TargetTrackingScalingPolicyConfiguration"


ScalingPolicy: TypeAlias = _ScalingPolicy_TargetTracking | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ScalingPolicy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "TargetTracking" in value:
        import capo_sagemaker.types.target_tracking_scaling_policy_configuration

        return {
            "TargetTracking": capo_sagemaker.types.target_tracking_scaling_policy_configuration.serialize_aws_json_1_1(
                value["TargetTracking"]
            )
        }
    else:
        raise SerializationError("ScalingPolicy: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicy:
    if data.get("TargetTracking") is not None:
        import capo_sagemaker.types.target_tracking_scaling_policy_configuration

        return {
            "TargetTracking": capo_sagemaker.types.target_tracking_scaling_policy_configuration.deserialize_aws_json_1_1(
                data["TargetTracking"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ScalingPolicy: no recognized variant key")
