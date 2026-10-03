"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsAutoScalingAutoScalingGroupDetails(TypedDict, closed=True):
    launch_configuration_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch configuration.</p>"""
    load_balancer_names: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of load balancers associated with the group.</p>"""
    health_check_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The service to use for the health checks. Valid values are <code>EC2</code> or <code>ELB</code>.</p>"""
    health_check_grace_period: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before it checks the health status of an EC2 instance that has come into service.</p>"""
    created_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the auto scaling group was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    mixed_instances_policy: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails"
    ]
    """<p>The mixed instances policy for the automatic scaling group.</p>"""
    availability_zones: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.AwsAutoScalingAutoScalingGroupAvailabilityZonesList"
    ]
    """<p>The list of Availability Zones for the automatic scaling group.</p>"""
    launch_template: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification"
    ]
    """<p>The launch template to use.</p>"""
    capacity_rebalance: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether capacity rebalancing is enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAutoScalingAutoScalingGroupDetails) -> dict:
    out: dict = {}
    if "launch_configuration_name" in value:
        out["LaunchConfigurationName"] = value["launch_configuration_name"]
    if "load_balancer_names" in value:
        import capo_securityhub.types.string_list

        out["LoadBalancerNames"] = capo_securityhub.types.string_list.serialize_json(
            value["load_balancer_names"]
        )
    if "health_check_type" in value:
        out["HealthCheckType"] = value["health_check_type"]
    if "health_check_grace_period" in value:
        out["HealthCheckGracePeriod"] = value["health_check_grace_period"]
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "mixed_instances_policy" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details

        out["MixedInstancesPolicy"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.serialize_json(
                value["mixed_instances_policy"]
            )
        )
    if "availability_zones" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list

        out["AvailabilityZones"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.serialize_json(
                value["availability_zones"]
            )
        )
    if "launch_template" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification

        out["LaunchTemplate"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "capacity_rebalance" in value:
        out["CapacityRebalance"] = value["capacity_rebalance"]
    return out


def deserialize_json(data: dict) -> AwsAutoScalingAutoScalingGroupDetails:
    out: AwsAutoScalingAutoScalingGroupDetails = {}  # type: ignore[typeddict-item]
    if data.get("LaunchConfigurationName") is not None:
        out["launch_configuration_name"] = data["LaunchConfigurationName"]
    if data.get("LoadBalancerNames") is not None:
        import capo_securityhub.types.string_list

        out["load_balancer_names"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["LoadBalancerNames"]
            )
        )
    if data.get("HealthCheckType") is not None:
        out["health_check_type"] = data["HealthCheckType"]
    if data.get("HealthCheckGracePeriod") is not None:
        out["health_check_grace_period"] = data["HealthCheckGracePeriod"]
    if data.get("CreatedTime") is not None:
        out["created_time"] = data["CreatedTime"]
    if data.get("MixedInstancesPolicy") is not None:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details

        out["mixed_instances_policy"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.deserialize_json(
                data["MixedInstancesPolicy"]
            )
        )
    if data.get("AvailabilityZones") is not None:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list

        out["availability_zones"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if data.get("LaunchTemplate") is not None:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification

        out["launch_template"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.deserialize_json(
                data["LaunchTemplate"]
            )
        )
    if data.get("CapacityRebalance") is not None:
        out["capacity_rebalance"] = data["CapacityRebalance"]
    return out
