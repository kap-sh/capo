"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingTargetTrackingScalingPolicyConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.double_object
    import capo_dynamodb.types.integer_object


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(TypedDict, closed=True):
    disable_scale_in: NotRequired["capo_dynamodb.types.boolean_object.BooleanObject"]
    """<p>Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.</p>"""
    scale_in_cooldown: NotRequired["capo_dynamodb.types.integer_object.IntegerObject"]
    """<p>The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately. </p>"""
    scale_out_cooldown: NotRequired["capo_dynamodb.types.integer_object.IntegerObject"]
    """<p>The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.</p>"""
    target_value: "capo_dynamodb.types.double_object.DoubleObject"
    """<p>The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: AutoScalingTargetTrackingScalingPolicyConfigurationUpdate,
) -> dict:
    out: dict = {}
    if "disable_scale_in" in value:
        out["DisableScaleIn"] = value["disable_scale_in"]
    if "scale_in_cooldown" in value:
        out["ScaleInCooldown"] = value["scale_in_cooldown"]
    if "scale_out_cooldown" in value:
        out["ScaleOutCooldown"] = value["scale_out_cooldown"]
    out["TargetValue"] = (
        "NaN"
        if value["target_value"] != value["target_value"]
        else "Infinity"
        if value["target_value"] == float("inf")
        else "-Infinity"
        if value["target_value"] == float("-inf")
        else value["target_value"]
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AutoScalingTargetTrackingScalingPolicyConfigurationUpdate:
    out: AutoScalingTargetTrackingScalingPolicyConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("DisableScaleIn") is not None:
        out["disable_scale_in"] = data["DisableScaleIn"]
    if data.get("ScaleInCooldown") is not None:
        out["scale_in_cooldown"] = data["ScaleInCooldown"]
    if data.get("ScaleOutCooldown") is not None:
        out["scale_out_cooldown"] = data["ScaleOutCooldown"]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    else:
        out["target_value"] = 0.0
    return out
