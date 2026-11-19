"""Generated from Smithy shape ``com.amazonaws.keyspaces#TargetTrackingScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.boolean_object
    import capo_keyspaces.types.double_object
    import capo_keyspaces.types.integer_object


class TargetTrackingScalingPolicyConfiguration(TypedDict, closed=True):
    disable_scale_in: "capo_keyspaces.types.boolean_object.BooleanObject"
    """<p>Specifies if <code>scale-in</code> is enabled.</p> <p>When auto scaling automatically decreases capacity for a table, the table <i>scales in</i>. When scaling policies are set, they can't scale in the table lower than its minimum capacity.</p>"""
    scale_in_cooldown: "capo_keyspaces.types.integer_object.IntegerObject"
    """<p>Specifies a <code>scale-in</code> cool down period.</p> <p>A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts. </p>"""
    scale_out_cooldown: "capo_keyspaces.types.integer_object.IntegerObject"
    """<p>Specifies a scale out cool down period.</p> <p>A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts. </p>"""
    target_value: "capo_keyspaces.types.double_object.DoubleObject"
    """<p>Specifies the target value for the target tracking auto scaling policy.</p> <p>Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define <code>targetValue</code> as a percentage. A <code>double</code> between 20 and 90.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetTrackingScalingPolicyConfiguration) -> dict:
    out: dict = {}
    out["disableScaleIn"] = value.get("disable_scale_in", False)
    out["scaleInCooldown"] = value.get("scale_in_cooldown", 0)
    out["scaleOutCooldown"] = value.get("scale_out_cooldown", 0)
    out["targetValue"] = (
        "NaN"
        if value.get("target_value", 0) != value.get("target_value", 0)
        else "Infinity"
        if value.get("target_value", 0) == float("inf")
        else "-Infinity"
        if value.get("target_value", 0) == float("-inf")
        else value.get("target_value", 0)
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TargetTrackingScalingPolicyConfiguration:
    out: TargetTrackingScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("disableScaleIn") is not None:
        out["disable_scale_in"] = data["disableScaleIn"]
    else:
        out["disable_scale_in"] = False
    if data.get("scaleInCooldown") is not None:
        out["scale_in_cooldown"] = data["scaleInCooldown"]
    else:
        out["scale_in_cooldown"] = 0
    if data.get("scaleOutCooldown") is not None:
        out["scale_out_cooldown"] = data["scaleOutCooldown"]
    else:
        out["scale_out_cooldown"] = 0
    if data.get("targetValue") is not None:
        out["target_value"] = float(data["targetValue"])
    else:
        out["target_value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetTrackingScalingPolicyConfiguration) -> dict:
    out: dict = {}
    out["disableScaleIn"] = value.get("disable_scale_in", False)
    out["scaleInCooldown"] = value.get("scale_in_cooldown", 0)
    out["scaleOutCooldown"] = value.get("scale_out_cooldown", 0)
    out["targetValue"] = value.get("target_value", 0)
    return out


def deserialize_cbor(data: dict) -> TargetTrackingScalingPolicyConfiguration:
    out: TargetTrackingScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("disableScaleIn") is not None:
        out["disable_scale_in"] = data["disableScaleIn"]
    else:
        out["disable_scale_in"] = False
    if data.get("scaleInCooldown") is not None:
        out["scale_in_cooldown"] = data["scaleInCooldown"]
    else:
        out["scale_in_cooldown"] = 0
    if data.get("scaleOutCooldown") is not None:
        out["scale_out_cooldown"] = data["scaleOutCooldown"]
    else:
        out["scale_out_cooldown"] = 0
    if data.get("targetValue") is not None:
        out["target_value"] = float(data["targetValue"])
    else:
        out["target_value"] = 0
    return out
