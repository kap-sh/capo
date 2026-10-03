"""Generated from Smithy shape ``com.amazonaws.autoscaling#UpdateAutoScalingGroupType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_group_desired_capacity
    import capo_auto_scaling.types.auto_scaling_group_max_size
    import capo_auto_scaling.types.auto_scaling_group_min_size
    import capo_auto_scaling.types.availability_zone_distribution
    import capo_auto_scaling.types.availability_zone_ids
    import capo_auto_scaling.types.availability_zone_impairment_policy
    import capo_auto_scaling.types.availability_zones
    import capo_auto_scaling.types.capacity_rebalance_enabled
    import capo_auto_scaling.types.capacity_reservation_specification
    import capo_auto_scaling.types.context
    import capo_auto_scaling.types.cooldown
    import capo_auto_scaling.types.default_instance_warmup
    import capo_auto_scaling.types.deletion_protection
    import capo_auto_scaling.types.health_check_grace_period
    import capo_auto_scaling.types.instance_lifecycle_policy
    import capo_auto_scaling.types.instance_maintenance_policy
    import capo_auto_scaling.types.instance_protected
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.max_instance_lifetime
    import capo_auto_scaling.types.mixed_instances_policy
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.skip_zonal_shift_validation
    import capo_auto_scaling.types.termination_policies
    import capo_auto_scaling.types.update_placement_group_param
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len5000


class UpdateAutoScalingGroupType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    launch_configuration_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the launch configuration. If you specify <code>LaunchConfigurationName</code> in your update request, you can't specify <code>LaunchTemplate</code> or <code>MixedInstancesPolicy</code>.</p>"""
    launch_template: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template and version to use to specify the updates. If you specify <code>LaunchTemplate</code> in your update request, you can't specify <code>LaunchConfigurationName</code> or <code>MixedInstancesPolicy</code>.</p>"""
    mixed_instances_policy: NotRequired[
        "capo_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
    ]
    """<p>The mixed instances policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html">Auto Scaling groups with multiple instance types and purchase options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>You can remove the Distribution Segments configuration by specifying <code>OnDemandBaseCapacity</code> or <code>OnDemandPercentageAboveBaseCapacity</code>. You can also remove it explicitly by specifying an empty list for <code>DistributionSegments</code>.</p>"""
    min_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
    ]
    """<p>The minimum size of the Auto Scaling group.</p>"""
    max_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
    ]
    """<p>The maximum size of the Auto Scaling group.</p> <note> <p>With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above <code>MaxSize</code> to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above <code>MaxSize</code> by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).</p> </note>"""
    desired_capacity: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
    ]
    """<p>The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.</p>"""
    default_cooldown: NotRequired["capo_auto_scaling.types.cooldown.Cooldown"]
    """<p> <i>Only needed if you use simple scaling policies.</i> </p> <p>The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    availability_zones: NotRequired[
        "capo_auto_scaling.types.availability_zones.AvailabilityZones"
    ]
    """<p>One or more Availability Zones for the group.</p>"""
    availability_zone_ids: NotRequired[
        "capo_auto_scaling.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p> A list of Availability Zone IDs for the Auto Scaling group. You cannot specify both AvailabilityZones and AvailabilityZoneIds in the same request. </p>"""
    health_check_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>A comma-separated value string of one or more health check types.</p> <p>The valid values are <code>EC2</code>, <code>EBS</code>, <code>ELB</code>, and <code>VPC_LATTICE</code>. <code>EC2</code> is the default health check and cannot be disabled. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html">Health checks for instances in an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Only specify <code>EC2</code> if you must clear a value that was previously set.</p>"""
    health_check_grace_period: NotRequired[
        "capo_auto_scaling.types.health_check_grace_period.HealthCheckGracePeriod"
    ]
    """<p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the <code>InService</code> state. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html">Set the health check grace period for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    placement_group: NotRequired[
        "capo_auto_scaling.types.update_placement_group_param.UpdatePlacementGroupParam"
    ]
    """<p>The name of an existing placement group into which to launch your instances. To remove the placement group setting, pass an empty string for <code>placement-group</code>. For more information about placement groups, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">Placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>A <i>cluster</i> placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group. </p> </note>"""
    vpc_zone_identifier: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len5000.XmlStringMaxLen5000"
    ]
    """<p>A comma-separated list of subnet IDs for a virtual private cloud (VPC). If you specify <code>VPCZoneIdentifier</code> with <code>AvailabilityZones</code>, the subnets that you specify must reside in those Availability Zones.</p>"""
    termination_policies: NotRequired[
        "capo_auto_scaling.types.termination_policies.TerminationPolicies"
    ]
    """<p>A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html">Configure termination policies for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Valid values: <code>Default</code> | <code>AllocationStrategy</code> | <code>ClosestToNextInstanceHour</code> | <code>NewestInstance</code> | <code>OldestInstance</code> | <code>OldestLaunchConfiguration</code> | <code>OldestLaunchTemplate</code> | <code>arn:aws:lambda:region:account-id:function:my-function:my-alias</code> </p>"""
    new_instances_protected_from_scale_in: NotRequired[
        "capo_auto_scaling.types.instance_protected.InstanceProtected"
    ]
    """<p>Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html">Use instance scale-in protection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    service_linked_role_arn: NotRequired[
        "capo_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html">Service-linked roles</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    max_instance_lifetime: NotRequired[
        "capo_auto_scaling.types.max_instance_lifetime.MaxInstanceLifetime"
    ]
    """<p>The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). To clear a previously set value, specify a new value of 0. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html">Replacing Auto Scaling instances based on maximum instance lifetime</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    capacity_rebalance: NotRequired[
        "capo_auto_scaling.types.capacity_rebalance_enabled.CapacityRebalanceEnabled"
    ]
    """<p>Enables or disables Capacity Rebalancing. If Capacity Rebalancing is disabled, proactive replacement of at-risk Spot Instances does not occur. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html">Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <note> <p>To suspend rebalancing across Availability Zones, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendedProcess.html">SuspendProcesses</a> API.</p> </note>"""
    context: NotRequired["capo_auto_scaling.types.context.Context"]
    """<p>Reserved.</p>"""
    desired_capacity_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports <code>DesiredCapacityType</code> for attribute-based instance type selection only. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html">Create a mixed instances group using attribute-based instance type selection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>By default, Amazon EC2 Auto Scaling specifies <code>units</code>, which translates into number of instances.</p> <p>Valid values: <code>units</code> | <code>vcpu</code> | <code>memory-mib</code> </p>"""
    default_instance_warmup: NotRequired[
        "capo_auto_scaling.types.default_instance_warmup.DefaultInstanceWarmup"
    ]
    """<p>The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the <code>InService</code> state. </p> <p>During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html">Set the default instance warmup for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <important> <p>To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, <i>even if it is set to 0 seconds</i>. To remove a value that you previously set, include the property but specify <code>-1</code> for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of <code>0</code> or other nominal value.</p> </important>"""
    instance_maintenance_policy: NotRequired[
        "capo_auto_scaling.types.instance_maintenance_policy.InstanceMaintenancePolicy"
    ]
    """<p>An instance maintenance policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html">Set instance maintenance policy</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    availability_zone_distribution: NotRequired[
        "capo_auto_scaling.types.availability_zone_distribution.AvailabilityZoneDistribution"
    ]
    """<p> The instance capacity distribution across Availability Zones. </p>"""
    availability_zone_impairment_policy: NotRequired[
        "capo_auto_scaling.types.availability_zone_impairment_policy.AvailabilityZoneImpairmentPolicy"
    ]
    """<p> The policy for Availability Zone impairment. </p>"""
    skip_zonal_shift_validation: NotRequired[
        "capo_auto_scaling.types.skip_zonal_shift_validation.SkipZonalShiftValidation"
    ]
    """<p> If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""
    capacity_reservation_specification: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p> The capacity reservation specification for the Auto Scaling group. </p>"""
    instance_lifecycle_policy: NotRequired[
        "capo_auto_scaling.types.instance_lifecycle_policy.InstanceLifecyclePolicy"
    ]
    """<p> The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a <code>Retained</code> state instead of automatic termination. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html"> Control instance retention with instance lifecycle policies</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""
    deletion_protection: NotRequired[
        "capo_auto_scaling.types.deletion_protection.DeletionProtection"
    ]
    """<p> The deletion protection setting for the Auto Scaling group. This setting helps safeguard your Auto Scaling group and its instances by controlling whether the <code>DeleteAutoScalingGroup</code> operation is allowed. When deletion protection is enabled, users cannot delete the Auto Scaling group according to the specified protection level until the setting is changed back to a less restrictive level. </p> <p> The valid values are <code>none</code>, <code>prevent-force-deletion</code>, and <code>prevent-all-deletion</code>. </p> <p> Default: <code>none</code> </p> <p> For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html"> Configure deletion protection for your Amazon EC2 Auto Scaling resources</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAutoScalingGroupType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "launch_configuration_name" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchConfigurationName",
                str(value["launch_configuration_name"]),
            )
        )
    if "launch_template" in value:
        import capo_auto_scaling.types.launch_template_specification

        capo_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template"], pairs, f"{key_prefix}LaunchTemplate"
        )
    if "mixed_instances_policy" in value:
        import capo_auto_scaling.types.mixed_instances_policy

        capo_auto_scaling.types.mixed_instances_policy.serialize_query(
            value["mixed_instances_policy"], pairs, f"{key_prefix}MixedInstancesPolicy"
        )
    if "min_size" in value:
        pairs.append((f"{key_prefix}MinSize", str(value["min_size"])))
    if "max_size" in value:
        pairs.append((f"{key_prefix}MaxSize", str(value["max_size"])))
    if "desired_capacity" in value:
        pairs.append((f"{key_prefix}DesiredCapacity", str(value["desired_capacity"])))
    if "default_cooldown" in value:
        pairs.append((f"{key_prefix}DefaultCooldown", str(value["default_cooldown"])))
    if "availability_zones" in value:
        import capo_auto_scaling.types.availability_zones

        capo_auto_scaling.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "availability_zone_ids" in value:
        import capo_auto_scaling.types.availability_zone_ids

        capo_auto_scaling.types.availability_zone_ids.serialize_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneIds"
        )
    if "health_check_type" in value:
        pairs.append((f"{key_prefix}HealthCheckType", str(value["health_check_type"])))
    if "health_check_grace_period" in value:
        pairs.append(
            (
                f"{key_prefix}HealthCheckGracePeriod",
                str(value["health_check_grace_period"]),
            )
        )
    if "placement_group" in value:
        pairs.append((f"{key_prefix}PlacementGroup", str(value["placement_group"])))
    if "vpc_zone_identifier" in value:
        pairs.append(
            (f"{key_prefix}VPCZoneIdentifier", str(value["vpc_zone_identifier"]))
        )
    if "termination_policies" in value:
        import capo_auto_scaling.types.termination_policies

        capo_auto_scaling.types.termination_policies.serialize_query(
            value["termination_policies"], pairs, f"{key_prefix}TerminationPolicies"
        )
    if "new_instances_protected_from_scale_in" in value:
        pairs.append(
            (
                f"{key_prefix}NewInstancesProtectedFromScaleIn",
                "true" if value["new_instances_protected_from_scale_in"] else "false",
            )
        )
    if "service_linked_role_arn" in value:
        pairs.append(
            (f"{key_prefix}ServiceLinkedRoleARN", str(value["service_linked_role_arn"]))
        )
    if "max_instance_lifetime" in value:
        pairs.append(
            (f"{key_prefix}MaxInstanceLifetime", str(value["max_instance_lifetime"]))
        )
    if "capacity_rebalance" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityRebalance",
                "true" if value["capacity_rebalance"] else "false",
            )
        )
    if "context" in value:
        pairs.append((f"{key_prefix}Context", str(value["context"])))
    if "desired_capacity_type" in value:
        pairs.append(
            (f"{key_prefix}DesiredCapacityType", str(value["desired_capacity_type"]))
        )
    if "default_instance_warmup" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultInstanceWarmup",
                str(value["default_instance_warmup"]),
            )
        )
    if "instance_maintenance_policy" in value:
        import capo_auto_scaling.types.instance_maintenance_policy

        capo_auto_scaling.types.instance_maintenance_policy.serialize_query(
            value["instance_maintenance_policy"],
            pairs,
            f"{key_prefix}InstanceMaintenancePolicy",
        )
    if "availability_zone_distribution" in value:
        import capo_auto_scaling.types.availability_zone_distribution

        capo_auto_scaling.types.availability_zone_distribution.serialize_query(
            value["availability_zone_distribution"],
            pairs,
            f"{key_prefix}AvailabilityZoneDistribution",
        )
    if "availability_zone_impairment_policy" in value:
        import capo_auto_scaling.types.availability_zone_impairment_policy

        capo_auto_scaling.types.availability_zone_impairment_policy.serialize_query(
            value["availability_zone_impairment_policy"],
            pairs,
            f"{key_prefix}AvailabilityZoneImpairmentPolicy",
        )
    if "skip_zonal_shift_validation" in value:
        pairs.append(
            (
                f"{key_prefix}SkipZonalShiftValidation",
                "true" if value["skip_zonal_shift_validation"] else "false",
            )
        )
    if "capacity_reservation_specification" in value:
        import capo_auto_scaling.types.capacity_reservation_specification

        capo_auto_scaling.types.capacity_reservation_specification.serialize_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{key_prefix}CapacityReservationSpecification",
        )
    if "instance_lifecycle_policy" in value:
        import capo_auto_scaling.types.instance_lifecycle_policy

        capo_auto_scaling.types.instance_lifecycle_policy.serialize_query(
            value["instance_lifecycle_policy"],
            pairs,
            f"{key_prefix}InstanceLifecyclePolicy",
        )
    if "deletion_protection" in value:
        import capo_auto_scaling.types.deletion_protection

        capo_auto_scaling.types.deletion_protection.serialize_query(
            value["deletion_protection"], pairs, f"{key_prefix}DeletionProtection"
        )


def deserialize_query(el: Element) -> UpdateAutoScalingGroupType:
    out: UpdateAutoScalingGroupType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_launch_configuration_name = el.find("LaunchConfigurationName")
    if child_launch_configuration_name is not None:
        out["launch_configuration_name"] = str(
            child_launch_configuration_name.text or ""
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_auto_scaling.types.launch_template_specification

        out["launch_template"] = (
            capo_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template
            )
        )
    child_mixed_instances_policy = el.find("MixedInstancesPolicy")
    if child_mixed_instances_policy is not None:
        import capo_auto_scaling.types.mixed_instances_policy

        out["mixed_instances_policy"] = (
            capo_auto_scaling.types.mixed_instances_policy.deserialize_query(
                child_mixed_instances_policy
            )
        )
    child_min_size = el.find("MinSize")
    if child_min_size is not None:
        out["min_size"] = int(child_min_size.text or "")
    child_max_size = el.find("MaxSize")
    if child_max_size is not None:
        out["max_size"] = int(child_max_size.text or "")
    child_desired_capacity = el.find("DesiredCapacity")
    if child_desired_capacity is not None:
        out["desired_capacity"] = int(child_desired_capacity.text or "")
    child_default_cooldown = el.find("DefaultCooldown")
    if child_default_cooldown is not None:
        out["default_cooldown"] = int(child_default_cooldown.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_auto_scaling.types.availability_zones

        out["availability_zones"] = (
            capo_auto_scaling.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_availability_zone_ids = el.find("AvailabilityZoneIds")
    if child_availability_zone_ids is not None:
        import capo_auto_scaling.types.availability_zone_ids

        out["availability_zone_ids"] = (
            capo_auto_scaling.types.availability_zone_ids.deserialize_query(
                child_availability_zone_ids
            )
        )
    child_health_check_type = el.find("HealthCheckType")
    if child_health_check_type is not None:
        out["health_check_type"] = str(child_health_check_type.text or "")
    child_health_check_grace_period = el.find("HealthCheckGracePeriod")
    if child_health_check_grace_period is not None:
        out["health_check_grace_period"] = int(
            child_health_check_grace_period.text or ""
        )
    child_placement_group = el.find("PlacementGroup")
    if child_placement_group is not None:
        out["placement_group"] = str(child_placement_group.text or "")
    child_vpc_zone_identifier = el.find("VPCZoneIdentifier")
    if child_vpc_zone_identifier is not None:
        out["vpc_zone_identifier"] = str(child_vpc_zone_identifier.text or "")
    child_termination_policies = el.find("TerminationPolicies")
    if child_termination_policies is not None:
        import capo_auto_scaling.types.termination_policies

        out["termination_policies"] = (
            capo_auto_scaling.types.termination_policies.deserialize_query(
                child_termination_policies
            )
        )
    child_new_instances_protected_from_scale_in = el.find(
        "NewInstancesProtectedFromScaleIn"
    )
    if child_new_instances_protected_from_scale_in is not None:
        out["new_instances_protected_from_scale_in"] = (
            child_new_instances_protected_from_scale_in.text or ""
        ).lower() == "true"
    child_service_linked_role_arn = el.find("ServiceLinkedRoleARN")
    if child_service_linked_role_arn is not None:
        out["service_linked_role_arn"] = str(child_service_linked_role_arn.text or "")
    child_max_instance_lifetime = el.find("MaxInstanceLifetime")
    if child_max_instance_lifetime is not None:
        out["max_instance_lifetime"] = int(child_max_instance_lifetime.text or "")
    child_capacity_rebalance = el.find("CapacityRebalance")
    if child_capacity_rebalance is not None:
        out["capacity_rebalance"] = (
            child_capacity_rebalance.text or ""
        ).lower() == "true"
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    child_desired_capacity_type = el.find("DesiredCapacityType")
    if child_desired_capacity_type is not None:
        out["desired_capacity_type"] = str(child_desired_capacity_type.text or "")
    child_default_instance_warmup = el.find("DefaultInstanceWarmup")
    if child_default_instance_warmup is not None:
        out["default_instance_warmup"] = int(child_default_instance_warmup.text or "")
    child_instance_maintenance_policy = el.find("InstanceMaintenancePolicy")
    if child_instance_maintenance_policy is not None:
        import capo_auto_scaling.types.instance_maintenance_policy

        out["instance_maintenance_policy"] = (
            capo_auto_scaling.types.instance_maintenance_policy.deserialize_query(
                child_instance_maintenance_policy
            )
        )
    child_availability_zone_distribution = el.find("AvailabilityZoneDistribution")
    if child_availability_zone_distribution is not None:
        import capo_auto_scaling.types.availability_zone_distribution

        out["availability_zone_distribution"] = (
            capo_auto_scaling.types.availability_zone_distribution.deserialize_query(
                child_availability_zone_distribution
            )
        )
    child_availability_zone_impairment_policy = el.find(
        "AvailabilityZoneImpairmentPolicy"
    )
    if child_availability_zone_impairment_policy is not None:
        import capo_auto_scaling.types.availability_zone_impairment_policy

        out["availability_zone_impairment_policy"] = (
            capo_auto_scaling.types.availability_zone_impairment_policy.deserialize_query(
                child_availability_zone_impairment_policy
            )
        )
    child_skip_zonal_shift_validation = el.find("SkipZonalShiftValidation")
    if child_skip_zonal_shift_validation is not None:
        out["skip_zonal_shift_validation"] = (
            child_skip_zonal_shift_validation.text or ""
        ).lower() == "true"
    child_capacity_reservation_specification = el.find(
        "CapacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import capo_auto_scaling.types.capacity_reservation_specification

        out["capacity_reservation_specification"] = (
            capo_auto_scaling.types.capacity_reservation_specification.deserialize_query(
                child_capacity_reservation_specification
            )
        )
    child_instance_lifecycle_policy = el.find("InstanceLifecyclePolicy")
    if child_instance_lifecycle_policy is not None:
        import capo_auto_scaling.types.instance_lifecycle_policy

        out["instance_lifecycle_policy"] = (
            capo_auto_scaling.types.instance_lifecycle_policy.deserialize_query(
                child_instance_lifecycle_policy
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        import capo_auto_scaling.types.deletion_protection

        out["deletion_protection"] = (
            capo_auto_scaling.types.deletion_protection.deserialize_query(
                child_deletion_protection
            )
        )
    return out
