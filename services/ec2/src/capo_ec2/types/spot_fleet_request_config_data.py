"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfigData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allocation_strategy
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.double
    import capo_ec2.types.excess_capacity_termination_policy
    import capo_ec2.types.fleet_type
    import capo_ec2.types.instance_interruption_behavior
    import capo_ec2.types.integer
    import capo_ec2.types.launch_specs_list
    import capo_ec2.types.launch_template_config_list
    import capo_ec2.types.load_balancers_config
    import capo_ec2.types.on_demand_allocation_strategy
    import capo_ec2.types.spot_maintenance_strategies
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.target_capacity_unit_type


class SpotFleetRequestConfigData(TypedDict, closed=True):
    allocation_strategy: NotRequired[
        "capo_ec2.types.allocation_strategy.AllocationStrategy"
    ]
    """<p>The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the Spot Fleet launch configuration. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html">Allocation strategies for Spot Instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <dl> <dt>priceCapacityOptimized (recommended)</dt> <dd> <p>Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. Spot Fleet then requests Spot Instances from the lowest priced of these pools.</p> </dd> <dt>capacityOptimized</dt> <dd> <p>Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use <code>capacityOptimizedPrioritized</code>. Set a priority for each instance type by using the <code>Priority</code> parameter for <code>LaunchTemplateOverrides</code>. You can assign the same priority to different <code>LaunchTemplateOverrides</code>. EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. <code>capacityOptimizedPrioritized</code> is supported only if your Spot Fleet uses a launch template. Note that if the <code>OnDemandAllocationStrategy</code> is set to <code>prioritized</code>, the same priority is applied when fulfilling On-Demand capacity.</p> </dd> <dt>diversified</dt> <dd> <p>Spot Fleet requests instances from all of the Spot Instance pools that you specify.</p> </dd> <dt>lowestPrice (not recommended)</dt> <dd> <important> <p>We don't recommend the <code>lowestPrice</code> allocation strategy because it has the highest risk of interruption for your Spot Instances.</p> </important> <p>Spot Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, Spot Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.</p> </dd> </dl> <p>Default: <code>lowestPrice</code> </p>"""
    on_demand_allocation_strategy: NotRequired[
        "capo_ec2.types.on_demand_allocation_strategy.OnDemandAllocationStrategy"
    ]
    """<p>The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify <code>lowestPrice</code>, Spot Fleet uses price to determine the order, launching the lowest price first. If you specify <code>prioritized</code>, Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to <code>lowestPrice</code>.</p>"""
    spot_maintenance_strategies: NotRequired[
        "capo_ec2.types.spot_maintenance_strategies.SpotMaintenanceStrategies"
    ]
    """<p>The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "capo_ec2.types.excess_capacity_termination_policy.ExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if you decrease the target capacity of the Spot Fleet request below the current size of the Spot Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    fulfilled_capacity: NotRequired["capo_ec2.types.double.Double"]
    """<p>The number of units fulfilled by this request compared to the set target capacity. You cannot set this value.</p>"""
    on_demand_fulfilled_capacity: NotRequired["capo_ec2.types.double.Double"]
    """<p>The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.</p>"""
    iam_fleet_role: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that grants the Spot Fleet the permission to request, launch, terminate, and tag instances on your behalf. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html#spot-fleet-prerequisites">Spot Fleet prerequisites</a> in the <i>Amazon EC2 User Guide</i>. Spot Fleet can terminate Spot Instances on your behalf when you cancel its Spot Fleet request using <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests">CancelSpotFleetRequests</a> or when the Spot Fleet request expires, if you set <code>TerminateInstancesWithExpiration</code>.</p>"""
    launch_specifications: NotRequired[
        "capo_ec2.types.launch_specs_list.LaunchSpecsList"
    ]
    """<p>The launch specifications for the Spot Fleet request. If you specify <code>LaunchSpecifications</code>, you can't specify <code>LaunchTemplateConfigs</code>. If you include On-Demand capacity in your request, you must use <code>LaunchTemplateConfigs</code>.</p> <note> <p>If an AMI specified in a launch specification is deregistered or disabled, no new instances can be launched from the AMI. For fleets of type <code>maintain</code>, the target capacity will not be maintained.</p> </note>"""
    launch_template_configs: NotRequired[
        "capo_ec2.types.launch_template_config_list.LaunchTemplateConfigList"
    ]
    """<p>The launch template and overrides. If you specify <code>LaunchTemplateConfigs</code>, you can't specify <code>LaunchSpecifications</code>. If you include On-Demand capacity in your request, you must use <code>LaunchTemplateConfigs</code>.</p>"""
    spot_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of units to request for the Spot Fleet. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is <code>maintain</code>, you can specify a target capacity of 0 and add capacity later.</p>"""
    on_demand_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is <code>maintain</code>, you can specify a target capacity of 0 and add capacity later.</p>"""
    on_demand_max_total_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum amount per hour for On-Demand Instances that you're willing to pay. You can use the <code>onDemandMaxTotalPrice</code> parameter, the <code>spotMaxTotalPrice</code> parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>onDemandMaxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>onDemandMaxTotalPrice</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""
    spot_max_total_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum amount per hour for Spot Instances that you're willing to pay. You can use the <code>spotMaxTotalPrice</code> parameter, the <code>onDemandMaxTotalPrice</code> parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>spotMaxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>spotMaxTotalPrice</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""
    terminate_instances_with_expiration: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether running Spot Instances are terminated when the Spot Fleet request expires.</p>"""
    type: NotRequired["capo_ec2.types.fleet_type.FleetType"]
    """<p>The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is <code>request</code>, the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. When this value is <code>maintain</code>, the Spot Fleet maintains the target capacity. The Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: <code>maintain</code>. <code>instant</code> is listed but is not used by Spot Fleet.</p>"""
    valid_from: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The start date and time of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). By default, Amazon EC2 starts fulfilling the request immediately.</p>"""
    valid_until: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The end date and time of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). After the end date and time, no new Spot Instance requests are placed or able to fulfill the request. If no value is specified, the Spot Fleet request remains until you cancel it.</p>"""
    replace_unhealthy_instances: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Spot Fleet should replace unhealthy instances.</p>"""
    instance_interruption_behavior: NotRequired[
        "capo_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted. The default is <code>terminate</code>.</p>"""
    load_balancers_config: NotRequired[
        "capo_ec2.types.load_balancers_config.LoadBalancersConfig"
    ]
    """<p>One or more Classic Load Balancers and target groups to attach to the Spot Fleet request. Spot Fleet registers the running Spot Instances with the specified Classic Load Balancers and target groups.</p> <p>With Network Load Balancers, Spot Fleet cannot register instances that have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.</p>"""
    instance_pools_to_use_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot <b>AllocationStrategy</b> is set to <code>lowest-price</code>. Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.</p> <p>Note that Spot Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, Spot Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.</p>"""
    context: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    target_capacity_unit_type: NotRequired[
        "capo_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity. You can specify this parameter only when using attribute-based instance type selection.</p> <p>Default: <code>units</code> (the number of instances)</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the Spot Fleet request on creation. The value for <code>ResourceType</code> must be <code>spot-fleet-request</code>, otherwise the Spot Fleet request fails. To tag instances at launch, specify the tags in the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template">launch template</a> (valid only if you use <code>LaunchTemplateConfigs</code>) or in the <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetTagSpecification.html">SpotFleetTagSpecification</a> </code> (valid only if you use <code>LaunchSpecifications</code>). For information about tagging after launch, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources">Tag your resources</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetRequestConfigData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        import capo_ec2.types.allocation_strategy

        capo_ec2.types.allocation_strategy.serialize_ec2_query(
            value["allocation_strategy"], pairs, f"{key_prefix}AllocationStrategy"
        )
    if "on_demand_allocation_strategy" in value:
        import capo_ec2.types.on_demand_allocation_strategy

        capo_ec2.types.on_demand_allocation_strategy.serialize_ec2_query(
            value["on_demand_allocation_strategy"],
            pairs,
            f"{key_prefix}OnDemandAllocationStrategy",
        )
    if "spot_maintenance_strategies" in value:
        import capo_ec2.types.spot_maintenance_strategies

        capo_ec2.types.spot_maintenance_strategies.serialize_ec2_query(
            value["spot_maintenance_strategies"],
            pairs,
            f"{key_prefix}SpotMaintenanceStrategies",
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "excess_capacity_termination_policy" in value:
        import capo_ec2.types.excess_capacity_termination_policy

        capo_ec2.types.excess_capacity_termination_policy.serialize_ec2_query(
            value["excess_capacity_termination_policy"],
            pairs,
            f"{key_prefix}ExcessCapacityTerminationPolicy",
        )
    if "fulfilled_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}FulfilledCapacity",
                (
                    "NaN"
                    if value["fulfilled_capacity"] != value["fulfilled_capacity"]
                    else "Infinity"
                    if value["fulfilled_capacity"] == float("inf")
                    else "-Infinity"
                    if value["fulfilled_capacity"] == float("-inf")
                    else str(value["fulfilled_capacity"])
                ),
            )
        )
    if "on_demand_fulfilled_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandFulfilledCapacity",
                (
                    "NaN"
                    if value["on_demand_fulfilled_capacity"]
                    != value["on_demand_fulfilled_capacity"]
                    else "Infinity"
                    if value["on_demand_fulfilled_capacity"] == float("inf")
                    else "-Infinity"
                    if value["on_demand_fulfilled_capacity"] == float("-inf")
                    else str(value["on_demand_fulfilled_capacity"])
                ),
            )
        )
    if "iam_fleet_role" in value:
        pairs.append((f"{key_prefix}IamFleetRole", str(value["iam_fleet_role"])))
    if "launch_specifications" in value:
        import capo_ec2.types.launch_specs_list

        capo_ec2.types.launch_specs_list.serialize_ec2_query(
            value["launch_specifications"], pairs, f"{key_prefix}LaunchSpecifications"
        )
    if "launch_template_configs" in value:
        import capo_ec2.types.launch_template_config_list

        capo_ec2.types.launch_template_config_list.serialize_ec2_query(
            value["launch_template_configs"],
            pairs,
            f"{key_prefix}LaunchTemplateConfigs",
        )
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "target_capacity" in value:
        pairs.append((f"{key_prefix}TargetCapacity", str(value["target_capacity"])))
    if "on_demand_target_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandTargetCapacity",
                str(value["on_demand_target_capacity"]),
            )
        )
    if "on_demand_max_total_price" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandMaxTotalPrice",
                str(value["on_demand_max_total_price"]),
            )
        )
    if "spot_max_total_price" in value:
        pairs.append(
            (f"{key_prefix}SpotMaxTotalPrice", str(value["spot_max_total_price"]))
        )
    if "terminate_instances_with_expiration" in value:
        pairs.append(
            (
                f"{key_prefix}TerminateInstancesWithExpiration",
                "true" if value["terminate_instances_with_expiration"] else "false",
            )
        )
    if "type" in value:
        import capo_ec2.types.fleet_type

        capo_ec2.types.fleet_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "valid_from" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_from"], pairs, f"{key_prefix}ValidFrom"
        )
    if "valid_until" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{key_prefix}ValidUntil"
        )
    if "replace_unhealthy_instances" in value:
        pairs.append(
            (
                f"{key_prefix}ReplaceUnhealthyInstances",
                "true" if value["replace_unhealthy_instances"] else "false",
            )
        )
    if "instance_interruption_behavior" in value:
        import capo_ec2.types.instance_interruption_behavior

        capo_ec2.types.instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{key_prefix}InstanceInterruptionBehavior",
        )
    if "load_balancers_config" in value:
        import capo_ec2.types.load_balancers_config

        capo_ec2.types.load_balancers_config.serialize_ec2_query(
            value["load_balancers_config"], pairs, f"{key_prefix}LoadBalancersConfig"
        )
    if "instance_pools_to_use_count" in value:
        pairs.append(
            (
                f"{key_prefix}InstancePoolsToUseCount",
                str(value["instance_pools_to_use_count"]),
            )
        )
    if "context" in value:
        pairs.append((f"{key_prefix}Context", str(value["context"])))
    if "target_capacity_unit_type" in value:
        import capo_ec2.types.target_capacity_unit_type

        capo_ec2.types.target_capacity_unit_type.serialize_ec2_query(
            value["target_capacity_unit_type"],
            pairs,
            f"{key_prefix}TargetCapacityUnitType",
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetRequestConfigData:
    out: SpotFleetRequestConfigData = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("allocationStrategy")
    if child_allocation_strategy is not None:
        import capo_ec2.types.allocation_strategy

        out["allocation_strategy"] = (
            capo_ec2.types.allocation_strategy.deserialize_ec2_query(
                child_allocation_strategy
            )
        )
    child_on_demand_allocation_strategy = el.find("onDemandAllocationStrategy")
    if child_on_demand_allocation_strategy is not None:
        import capo_ec2.types.on_demand_allocation_strategy

        out["on_demand_allocation_strategy"] = (
            capo_ec2.types.on_demand_allocation_strategy.deserialize_ec2_query(
                child_on_demand_allocation_strategy
            )
        )
    child_spot_maintenance_strategies = el.find("spotMaintenanceStrategies")
    if child_spot_maintenance_strategies is not None:
        import capo_ec2.types.spot_maintenance_strategies

        out["spot_maintenance_strategies"] = (
            capo_ec2.types.spot_maintenance_strategies.deserialize_ec2_query(
                child_spot_maintenance_strategies
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_excess_capacity_termination_policy = el.find(
        "excessCapacityTerminationPolicy"
    )
    if child_excess_capacity_termination_policy is not None:
        import capo_ec2.types.excess_capacity_termination_policy

        out["excess_capacity_termination_policy"] = (
            capo_ec2.types.excess_capacity_termination_policy.deserialize_ec2_query(
                child_excess_capacity_termination_policy
            )
        )
    child_fulfilled_capacity = el.find("fulfilledCapacity")
    if child_fulfilled_capacity is not None:
        out["fulfilled_capacity"] = float(child_fulfilled_capacity.text or "")
    child_on_demand_fulfilled_capacity = el.find("onDemandFulfilledCapacity")
    if child_on_demand_fulfilled_capacity is not None:
        out["on_demand_fulfilled_capacity"] = float(
            child_on_demand_fulfilled_capacity.text or ""
        )
    child_iam_fleet_role = el.find("iamFleetRole")
    if child_iam_fleet_role is not None:
        out["iam_fleet_role"] = str(child_iam_fleet_role.text or "")
    child_launch_specifications = el.find("launchSpecifications")
    if child_launch_specifications is not None:
        import capo_ec2.types.launch_specs_list

        out["launch_specifications"] = (
            capo_ec2.types.launch_specs_list.deserialize_ec2_query(
                child_launch_specifications
            )
        )
    child_launch_template_configs = el.find("launchTemplateConfigs")
    if child_launch_template_configs is not None:
        import capo_ec2.types.launch_template_config_list

        out["launch_template_configs"] = (
            capo_ec2.types.launch_template_config_list.deserialize_ec2_query(
                child_launch_template_configs
            )
        )
    child_spot_price = el.find("spotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_target_capacity = el.find("targetCapacity")
    if child_target_capacity is not None:
        out["target_capacity"] = int(child_target_capacity.text or "")
    child_on_demand_target_capacity = el.find("onDemandTargetCapacity")
    if child_on_demand_target_capacity is not None:
        out["on_demand_target_capacity"] = int(
            child_on_demand_target_capacity.text or ""
        )
    child_on_demand_max_total_price = el.find("onDemandMaxTotalPrice")
    if child_on_demand_max_total_price is not None:
        out["on_demand_max_total_price"] = str(
            child_on_demand_max_total_price.text or ""
        )
    child_spot_max_total_price = el.find("spotMaxTotalPrice")
    if child_spot_max_total_price is not None:
        out["spot_max_total_price"] = str(child_spot_max_total_price.text or "")
    child_terminate_instances_with_expiration = el.find(
        "terminateInstancesWithExpiration"
    )
    if child_terminate_instances_with_expiration is not None:
        out["terminate_instances_with_expiration"] = (
            child_terminate_instances_with_expiration.text or ""
        ).lower() == "true"
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.fleet_type

        out["type"] = capo_ec2.types.fleet_type.deserialize_ec2_query(child_type)
    child_valid_from = el.find("validFrom")
    if child_valid_from is not None:
        import capo_ec2.types.date_time

        out["valid_from"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_from
        )
    child_valid_until = el.find("validUntil")
    if child_valid_until is not None:
        import capo_ec2.types.date_time

        out["valid_until"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_replace_unhealthy_instances = el.find("replaceUnhealthyInstances")
    if child_replace_unhealthy_instances is not None:
        out["replace_unhealthy_instances"] = (
            child_replace_unhealthy_instances.text or ""
        ).lower() == "true"
    child_instance_interruption_behavior = el.find("instanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import capo_ec2.types.instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            capo_ec2.types.instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    child_load_balancers_config = el.find("loadBalancersConfig")
    if child_load_balancers_config is not None:
        import capo_ec2.types.load_balancers_config

        out["load_balancers_config"] = (
            capo_ec2.types.load_balancers_config.deserialize_ec2_query(
                child_load_balancers_config
            )
        )
    child_instance_pools_to_use_count = el.find("instancePoolsToUseCount")
    if child_instance_pools_to_use_count is not None:
        out["instance_pools_to_use_count"] = int(
            child_instance_pools_to_use_count.text or ""
        )
    child_context = el.find("context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    child_target_capacity_unit_type = el.find("targetCapacityUnitType")
    if child_target_capacity_unit_type is not None:
        import capo_ec2.types.target_capacity_unit_type

        out["target_capacity_unit_type"] = (
            capo_ec2.types.target_capacity_unit_type.deserialize_ec2_query(
                child_target_capacity_unit_type
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
