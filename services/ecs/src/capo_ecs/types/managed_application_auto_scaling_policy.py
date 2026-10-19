"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedApplicationAutoScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.double
    import capo_ecs.types.managed_resource_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ManagedApplicationAutoScalingPolicy(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Application Auto Scaling policy associated with the Express service.</p>"""
    status: "capo_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of Application Auto Scaling policy creation.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the Application Auto Scaling policy is in the current status.</p>"""
    updated_at: "capo_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the Application Auto Scaling policy was last updated.</p>"""
    policy_type: "capo_ecs.types.string.String"
    """<p>The type of Application Auto Scaling policy associated with the Express service. Valid values are <code>TargetTrackingScaling</code>, <code>StepScaling</code>, and <code>PredictiveScaling</code>.</p>"""
    target_value: "capo_ecs.types.double.Double"
    """<p>The target value for the auto scaling metric.</p>"""
    metric: "capo_ecs.types.string.String"
    """<p>The metric used for auto scaling decisions. The available metrics are <code>ECSServiceAverageCPUUtilization</code>, <code>ECSServiceAverageMemoryUtilization</code>, and <code>ALBRequestCOuntPerTarget</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedApplicationAutoScalingPolicy) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import capo_ecs.types.managed_resource_status

    out["status"] = capo_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_ecs.types.timestamp

    out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    out["policyType"] = value["policy_type"]
    out["targetValue"] = (
        "NaN"
        if value.get("target_value", 0) != value.get("target_value", 0)
        else "Infinity"
        if value.get("target_value", 0) == float("inf")
        else "-Infinity"
        if value.get("target_value", 0) == float("-inf")
        else value.get("target_value", 0)
    )
    out["metric"] = value["metric"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedApplicationAutoScalingPolicy:
    out: ManagedApplicationAutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        import capo_ecs.types.managed_resource_status

        out["status"] = capo_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ecs.types.managed_resource_status.ManagedResourceStatus", ""
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("policyType") is not None:
        out["policy_type"] = data["policyType"]
    else:
        out["policy_type"] = ""
    if data.get("targetValue") is not None:
        out["target_value"] = float(data["targetValue"])
    else:
        out["target_value"] = 0
    if data.get("metric") is not None:
        out["metric"] = data["metric"]
    else:
        out["metric"] = ""
    return out
