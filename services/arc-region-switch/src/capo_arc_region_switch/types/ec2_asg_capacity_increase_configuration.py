"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Ec2AsgCapacityIncreaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.asg_list
    import capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach
    import capo_arc_region_switch.types.ec2_ungraceful
    import capo_arc_region_switch.types.wait_elb_target_group_healthy


class Ec2AsgCapacityIncreaseConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    asgs: "capo_arc_region_switch.types.asg_list.AsgList"
    """<p>The EC2 Auto Scaling groups for the configuration.</p>"""
    ungraceful: NotRequired["capo_arc_region_switch.types.ec2_ungraceful.Ec2Ungraceful"]
    """<p>The settings for ungraceful execution.</p>"""
    target_percent: "int"
    """<p>The target percentage that you specify for EC2 Auto Scaling groups. The default is 100.</p>"""
    capacity_monitoring_approach: "capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.Ec2AsgCapacityMonitoringApproach"
    """<p>The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.</p>"""
    wait_elb_target_group_healthy: NotRequired[
        "capo_arc_region_switch.types.wait_elb_target_group_healthy.WaitELBTargetGroupHealthy"
    ]
    """<p>If enabled, the step completes only after each attached ELB target group reports a healthy target count that matches the group's new desired capacity calculated in the step.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AsgCapacityIncreaseConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import capo_arc_region_switch.types.asg_list

    out["asgs"] = capo_arc_region_switch.types.asg_list.serialize_aws_json_1_0(
        value["asgs"]
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.ec2_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.ec2_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.serialize_aws_json_1_0(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    if "wait_elb_target_group_healthy" in value:
        import capo_arc_region_switch.types.wait_elb_target_group_healthy

        out["waitELBTargetGroupHealthy"] = (
            capo_arc_region_switch.types.wait_elb_target_group_healthy.serialize_aws_json_1_0(
                value["wait_elb_target_group_healthy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2AsgCapacityIncreaseConfiguration:
    out: Ec2AsgCapacityIncreaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("asgs") is not None:
        import capo_arc_region_switch.types.asg_list

        out["asgs"] = capo_arc_region_switch.types.asg_list.deserialize_aws_json_1_0(
            data["asgs"]
        )
    else:
        out["asgs"] = []
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.ec2_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.ec2_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if data.get("targetPercent") is not None:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if data.get("capacityMonitoringApproach") is not None:
        import capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            capo_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.deserialize_aws_json_1_0(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    if data.get("waitELBTargetGroupHealthy") is not None:
        import capo_arc_region_switch.types.wait_elb_target_group_healthy

        out["wait_elb_target_group_healthy"] = (
            capo_arc_region_switch.types.wait_elb_target_group_healthy.deserialize_aws_json_1_0(
                data["waitELBTargetGroupHealthy"]
            )
        )
    return out
