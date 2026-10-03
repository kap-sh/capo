"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_group_desired_capacity
    import capo_auto_scaling.types.auto_scaling_group_max_size
    import capo_auto_scaling.types.auto_scaling_group_min_size
    import capo_auto_scaling.types.auto_scaling_group_predicted_capacity
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
    import capo_auto_scaling.types.enabled_metrics
    import capo_auto_scaling.types.health_check_grace_period
    import capo_auto_scaling.types.instance_lifecycle_policy
    import capo_auto_scaling.types.instance_maintenance_policy
    import capo_auto_scaling.types.instance_protected
    import capo_auto_scaling.types.instances
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.load_balancer_names
    import capo_auto_scaling.types.max_instance_lifetime
    import capo_auto_scaling.types.mixed_instances_policy
    import capo_auto_scaling.types.operator
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.suspended_processes
    import capo_auto_scaling.types.tag_description_list
    import capo_auto_scaling.types.target_group_ar_ns
    import capo_auto_scaling.types.termination_policies
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.traffic_sources
    import capo_auto_scaling.types.warm_pool_configuration
    import capo_auto_scaling.types.warm_pool_size
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len5000


class AutoScalingGroup(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    auto_scaling_group_arn: NotRequired[
        "capo_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the Auto Scaling group.</p>"""
    launch_configuration_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the associated launch configuration for the Auto Scaling group.</p>"""
    launch_template: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template for the Auto Scaling group.</p>"""
    mixed_instances_policy: NotRequired[
        "capo_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
    ]
    """<p>The mixed instances policy for the group.</p>"""
    min_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
    ]
    """<p>The minimum size of the Auto Scaling group.</p>"""
    max_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
    ]
    """<p>The maximum size of the Auto Scaling group.</p>"""
    desired_capacity: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
    ]
    """<p>The desired size of the Auto Scaling group.</p>"""
    predicted_capacity: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_predicted_capacity.AutoScalingGroupPredictedCapacity"
    ]
    """<p>The predicted capacity of the group when it has a predictive scaling policy.</p>"""
    default_cooldown: NotRequired["capo_auto_scaling.types.cooldown.Cooldown"]
    """<p>The duration of the default cooldown period, in seconds, for the Auto Scaling group.</p>"""
    availability_zones: NotRequired[
        "capo_auto_scaling.types.availability_zones.AvailabilityZones"
    ]
    """<p>One or more Availability Zones for the Auto Scaling group.</p>"""
    availability_zone_ids: NotRequired[
        "capo_auto_scaling.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p> The Availability Zone IDs where the Auto Scaling group can launch instances. </p>"""
    load_balancer_names: NotRequired[
        "capo_auto_scaling.types.load_balancer_names.LoadBalancerNames"
    ]
    """<p>One or more load balancers associated with the group.</p>"""
    target_group_ar_ns: NotRequired[
        "capo_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
    ]
    """<p>The Amazon Resource Names (ARN) of the target groups for your load balancer.</p>"""
    health_check_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>One or more comma-separated health check types for the Auto Scaling group.</p>"""
    health_check_grace_period: NotRequired[
        "capo_auto_scaling.types.health_check_grace_period.HealthCheckGracePeriod"
    ]
    """<p>The duration of the health check grace period, in seconds, for the Auto Scaling group.</p>"""
    instances: NotRequired["capo_auto_scaling.types.instances.Instances"]
    """<p>The EC2 instances associated with the Auto Scaling group.</p>"""
    created_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The date and time the Auto Scaling group was created.</p>"""
    suspended_processes: NotRequired[
        "capo_auto_scaling.types.suspended_processes.SuspendedProcesses"
    ]
    """<p>The suspended processes associated with the Auto Scaling group.</p>"""
    placement_group: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the placement group into which to launch EC2 instances for the Auto Scaling group.</p>"""
    vpc_zone_identifier: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len5000.XmlStringMaxLen5000"
    ]
    """<p>One or more comma-separated subnet IDs for the Auto Scaling group.</p>"""
    enabled_metrics: NotRequired[
        "capo_auto_scaling.types.enabled_metrics.EnabledMetrics"
    ]
    """<p>The metrics enabled for the Auto Scaling group.</p>"""
    status: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The current state of the Auto Scaling group when the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html">DeleteAutoScalingGroup</a> operation is in progress.</p>"""
    tags: NotRequired["capo_auto_scaling.types.tag_description_list.TagDescriptionList"]
    """<p>The tags for the Auto Scaling group.</p>"""
    termination_policies: NotRequired[
        "capo_auto_scaling.types.termination_policies.TerminationPolicies"
    ]
    """<p>The termination policies for the Auto Scaling group.</p>"""
    new_instances_protected_from_scale_in: NotRequired[
        "capo_auto_scaling.types.instance_protected.InstanceProtected"
    ]
    """<p>Indicates whether newly launched EC2 instances are protected from termination when scaling in for the Auto Scaling group.</p> <p> For more information about preventing instances from terminating on scale in, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html">Use instance scale-in protection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""
    service_linked_role_arn: NotRequired[
        "capo_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf.</p>"""
    max_instance_lifetime: NotRequired[
        "capo_auto_scaling.types.max_instance_lifetime.MaxInstanceLifetime"
    ]
    """<p>The maximum amount of time, in seconds, that an EC2 instance can be in service for the Auto Scaling group.</p>"""
    capacity_rebalance: NotRequired[
        "capo_auto_scaling.types.capacity_rebalance_enabled.CapacityRebalanceEnabled"
    ]
    """<p>Indicates whether Capacity Rebalancing is enabled.</p>"""
    warm_pool_configuration: NotRequired[
        "capo_auto_scaling.types.warm_pool_configuration.WarmPoolConfiguration"
    ]
    """<p>The warm pool for the group.</p>"""
    warm_pool_size: NotRequired["capo_auto_scaling.types.warm_pool_size.WarmPoolSize"]
    """<p>The current size of the warm pool.</p>"""
    context: NotRequired["capo_auto_scaling.types.context.Context"]
    """<p>Reserved.</p>"""
    desired_capacity_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports <code>DesiredCapacityType</code> for attribute-based instance type selection only.</p>"""
    default_instance_warmup: NotRequired[
        "capo_auto_scaling.types.default_instance_warmup.DefaultInstanceWarmup"
    ]
    """<p>The duration of the default EC2 instance warmup time, in seconds, for the Auto Scaling group.</p>"""
    traffic_sources: NotRequired[
        "capo_auto_scaling.types.traffic_sources.TrafficSources"
    ]
    """<p>The traffic sources associated with this Auto Scaling group.</p>"""
    instance_maintenance_policy: NotRequired[
        "capo_auto_scaling.types.instance_maintenance_policy.InstanceMaintenancePolicy"
    ]
    """<p>An instance maintenance policy.</p>"""
    deletion_protection: NotRequired[
        "capo_auto_scaling.types.deletion_protection.DeletionProtection"
    ]
    """<p>The deletion protection setting for the Auto Scaling group.</p>"""
    availability_zone_distribution: NotRequired[
        "capo_auto_scaling.types.availability_zone_distribution.AvailabilityZoneDistribution"
    ]
    """<p>The EC2 instance capacity distribution across Availability Zones for the Auto Scaling group.</p>"""
    availability_zone_impairment_policy: NotRequired[
        "capo_auto_scaling.types.availability_zone_impairment_policy.AvailabilityZoneImpairmentPolicy"
    ]
    """<p>The Availability Zone impairment policy for the Auto Scaling group.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>The capacity reservation specification for the Auto Scaling group.</p>"""
    instance_lifecycle_policy: NotRequired[
        "capo_auto_scaling.types.instance_lifecycle_policy.InstanceLifecyclePolicy"
    ]
    """<p>The instance lifecycle policy for the Auto Scaling group.</p>"""
    operator: NotRequired["capo_auto_scaling.types.operator.Operator"]
    """<p>The entity that manages the Auto Scaling group, if applicable. When set, only the designated operator can make changes to the group configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "auto_scaling_group_arn" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupARN", str(value["auto_scaling_group_arn"]))
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
    if "predicted_capacity" in value:
        pairs.append(
            (f"{key_prefix}PredictedCapacity", str(value["predicted_capacity"]))
        )
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
    if "load_balancer_names" in value:
        import capo_auto_scaling.types.load_balancer_names

        capo_auto_scaling.types.load_balancer_names.serialize_query(
            value["load_balancer_names"], pairs, f"{key_prefix}LoadBalancerNames"
        )
    if "target_group_ar_ns" in value:
        import capo_auto_scaling.types.target_group_ar_ns

        capo_auto_scaling.types.target_group_ar_ns.serialize_query(
            value["target_group_ar_ns"], pairs, f"{key_prefix}TargetGroupARNs"
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
    if "instances" in value:
        import capo_auto_scaling.types.instances

        capo_auto_scaling.types.instances.serialize_query(
            value["instances"], pairs, f"{key_prefix}Instances"
        )
    if "created_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["created_time"], pairs, f"{key_prefix}CreatedTime"
        )
    if "suspended_processes" in value:
        import capo_auto_scaling.types.suspended_processes

        capo_auto_scaling.types.suspended_processes.serialize_query(
            value["suspended_processes"], pairs, f"{key_prefix}SuspendedProcesses"
        )
    if "placement_group" in value:
        pairs.append((f"{key_prefix}PlacementGroup", str(value["placement_group"])))
    if "vpc_zone_identifier" in value:
        pairs.append(
            (f"{key_prefix}VPCZoneIdentifier", str(value["vpc_zone_identifier"]))
        )
    if "enabled_metrics" in value:
        import capo_auto_scaling.types.enabled_metrics

        capo_auto_scaling.types.enabled_metrics.serialize_query(
            value["enabled_metrics"], pairs, f"{key_prefix}EnabledMetrics"
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "tags" in value:
        import capo_auto_scaling.types.tag_description_list

        capo_auto_scaling.types.tag_description_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
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
    if "warm_pool_configuration" in value:
        import capo_auto_scaling.types.warm_pool_configuration

        capo_auto_scaling.types.warm_pool_configuration.serialize_query(
            value["warm_pool_configuration"],
            pairs,
            f"{key_prefix}WarmPoolConfiguration",
        )
    if "warm_pool_size" in value:
        pairs.append((f"{key_prefix}WarmPoolSize", str(value["warm_pool_size"])))
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
    if "traffic_sources" in value:
        import capo_auto_scaling.types.traffic_sources

        capo_auto_scaling.types.traffic_sources.serialize_query(
            value["traffic_sources"], pairs, f"{key_prefix}TrafficSources"
        )
    if "instance_maintenance_policy" in value:
        import capo_auto_scaling.types.instance_maintenance_policy

        capo_auto_scaling.types.instance_maintenance_policy.serialize_query(
            value["instance_maintenance_policy"],
            pairs,
            f"{key_prefix}InstanceMaintenancePolicy",
        )
    if "deletion_protection" in value:
        import capo_auto_scaling.types.deletion_protection

        capo_auto_scaling.types.deletion_protection.serialize_query(
            value["deletion_protection"], pairs, f"{key_prefix}DeletionProtection"
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
    if "operator" in value:
        import capo_auto_scaling.types.operator

        capo_auto_scaling.types.operator.serialize_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_query(el: Element) -> AutoScalingGroup:
    out: AutoScalingGroup = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_auto_scaling_group_arn = el.find("AutoScalingGroupARN")
    if child_auto_scaling_group_arn is not None:
        out["auto_scaling_group_arn"] = str(child_auto_scaling_group_arn.text or "")
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
    child_predicted_capacity = el.find("PredictedCapacity")
    if child_predicted_capacity is not None:
        out["predicted_capacity"] = int(child_predicted_capacity.text or "")
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
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import capo_auto_scaling.types.load_balancer_names

        out["load_balancer_names"] = (
            capo_auto_scaling.types.load_balancer_names.deserialize_query(
                child_load_balancer_names
            )
        )
    child_target_group_ar_ns = el.find("TargetGroupARNs")
    if child_target_group_ar_ns is not None:
        import capo_auto_scaling.types.target_group_ar_ns

        out["target_group_ar_ns"] = (
            capo_auto_scaling.types.target_group_ar_ns.deserialize_query(
                child_target_group_ar_ns
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
    child_instances = el.find("Instances")
    if child_instances is not None:
        import capo_auto_scaling.types.instances

        out["instances"] = capo_auto_scaling.types.instances.deserialize_query(
            child_instances
        )
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["created_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_created_time
        )
    child_suspended_processes = el.find("SuspendedProcesses")
    if child_suspended_processes is not None:
        import capo_auto_scaling.types.suspended_processes

        out["suspended_processes"] = (
            capo_auto_scaling.types.suspended_processes.deserialize_query(
                child_suspended_processes
            )
        )
    child_placement_group = el.find("PlacementGroup")
    if child_placement_group is not None:
        out["placement_group"] = str(child_placement_group.text or "")
    child_vpc_zone_identifier = el.find("VPCZoneIdentifier")
    if child_vpc_zone_identifier is not None:
        out["vpc_zone_identifier"] = str(child_vpc_zone_identifier.text or "")
    child_enabled_metrics = el.find("EnabledMetrics")
    if child_enabled_metrics is not None:
        import capo_auto_scaling.types.enabled_metrics

        out["enabled_metrics"] = (
            capo_auto_scaling.types.enabled_metrics.deserialize_query(
                child_enabled_metrics
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_auto_scaling.types.tag_description_list

        out["tags"] = capo_auto_scaling.types.tag_description_list.deserialize_query(
            child_tags
        )
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
    child_warm_pool_configuration = el.find("WarmPoolConfiguration")
    if child_warm_pool_configuration is not None:
        import capo_auto_scaling.types.warm_pool_configuration

        out["warm_pool_configuration"] = (
            capo_auto_scaling.types.warm_pool_configuration.deserialize_query(
                child_warm_pool_configuration
            )
        )
    child_warm_pool_size = el.find("WarmPoolSize")
    if child_warm_pool_size is not None:
        out["warm_pool_size"] = int(child_warm_pool_size.text or "")
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    child_desired_capacity_type = el.find("DesiredCapacityType")
    if child_desired_capacity_type is not None:
        out["desired_capacity_type"] = str(child_desired_capacity_type.text or "")
    child_default_instance_warmup = el.find("DefaultInstanceWarmup")
    if child_default_instance_warmup is not None:
        out["default_instance_warmup"] = int(child_default_instance_warmup.text or "")
    child_traffic_sources = el.find("TrafficSources")
    if child_traffic_sources is not None:
        import capo_auto_scaling.types.traffic_sources

        out["traffic_sources"] = (
            capo_auto_scaling.types.traffic_sources.deserialize_query(
                child_traffic_sources
            )
        )
    child_instance_maintenance_policy = el.find("InstanceMaintenancePolicy")
    if child_instance_maintenance_policy is not None:
        import capo_auto_scaling.types.instance_maintenance_policy

        out["instance_maintenance_policy"] = (
            capo_auto_scaling.types.instance_maintenance_policy.deserialize_query(
                child_instance_maintenance_policy
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
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_auto_scaling.types.operator

        out["operator"] = capo_auto_scaling.types.operator.deserialize_query(
            child_operator
        )
    return out
