"""Generated from Smithy shape ``com.amazonaws.ec2#SpotOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.fleet_spot_maintenance_strategies_request
    import capo_ec2.types.integer
    import capo_ec2.types.spot_allocation_strategy
    import capo_ec2.types.spot_instance_interruption_behavior
    import capo_ec2.types.string


class SpotOptionsRequest(TypedDict, closed=True):
    allocation_strategy: NotRequired[
        "capo_ec2.types.spot_allocation_strategy.SpotAllocationStrategy"
    ]
    """<p>The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the EC2 Fleet launch configuration. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html">Allocation strategies for Spot Instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <dl> <dt>price-capacity-optimized (recommended)</dt> <dd> <p>EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. EC2 Fleet then requests Spot Instances from the lowest priced of these pools.</p> </dd> <dt>capacity-optimized</dt> <dd> <p>EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use <code>capacity-optimized-prioritized</code>. Set a priority for each instance type by using the <code>Priority</code> parameter for <code>LaunchTemplateOverrides</code>. You can assign the same priority to different <code>LaunchTemplateOverrides</code>. EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. <code>capacity-optimized-prioritized</code> is supported only if your EC2 Fleet uses a launch template. Note that if the On-Demand <code>AllocationStrategy</code> is set to <code>prioritized</code>, the same priority is applied when fulfilling On-Demand capacity.</p> </dd> <dt>diversified</dt> <dd> <p>EC2 Fleet requests instances from all of the Spot Instance pools that you specify.</p> </dd> <dt>lowest-price (not recommended)</dt> <dd> <important> <p>We don't recommend the <code>lowest-price</code> allocation strategy because it has the highest risk of interruption for your Spot Instances.</p> </important> <p>EC2 Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, EC2 Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.</p> </dd> </dl> <p>Default: <code>lowest-price</code> </p>"""
    maintenance_strategies: NotRequired[
        "capo_ec2.types.fleet_spot_maintenance_strategies_request.FleetSpotMaintenanceStrategiesRequest"
    ]
    """<p>The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.</p>"""
    instance_interruption_behavior: NotRequired[
        "capo_ec2.types.spot_instance_interruption_behavior.SpotInstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p> <p>Default: <code>terminate</code> </p>"""
    instance_pools_to_use_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of Spot pools across which to allocate your target Spot capacity. Supported only when Spot <code>AllocationStrategy</code> is set to <code>lowest-price</code>. EC2 Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.</p> <p>Note that EC2 Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, EC2 Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.</p>"""
    single_instance_type: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet uses a single instance type to launch all Spot Instances in the fleet.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    single_availability_zone: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet launches all Spot Instances into a single Availability Zone.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    min_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum target capacity for Spot Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.</p> <p>Constraints: Maximum value of <code>1000</code>. Supported only for fleets of type <code>instant</code>.</p> <p>At least one of the following must be specified: <code>SingleAvailabilityZone</code> | <code>SingleInstanceType</code> </p>"""
    max_total_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum amount per hour for Spot Instances that you're willing to pay. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.</p> </important> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>MaxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>MaxTotalPrice</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        import capo_ec2.types.spot_allocation_strategy

        capo_ec2.types.spot_allocation_strategy.serialize_ec2_query(
            value["allocation_strategy"], pairs, f"{key_prefix}AllocationStrategy"
        )
    if "maintenance_strategies" in value:
        import capo_ec2.types.fleet_spot_maintenance_strategies_request

        capo_ec2.types.fleet_spot_maintenance_strategies_request.serialize_ec2_query(
            value["maintenance_strategies"], pairs, f"{key_prefix}MaintenanceStrategies"
        )
    if "instance_interruption_behavior" in value:
        import capo_ec2.types.spot_instance_interruption_behavior

        capo_ec2.types.spot_instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{key_prefix}InstanceInterruptionBehavior",
        )
    if "instance_pools_to_use_count" in value:
        pairs.append(
            (
                f"{key_prefix}InstancePoolsToUseCount",
                str(value["instance_pools_to_use_count"]),
            )
        )
    if "single_instance_type" in value:
        pairs.append(
            (
                f"{key_prefix}SingleInstanceType",
                "true" if value["single_instance_type"] else "false",
            )
        )
    if "single_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SingleAvailabilityZone",
                "true" if value["single_availability_zone"] else "false",
            )
        )
    if "min_target_capacity" in value:
        pairs.append(
            (f"{key_prefix}MinTargetCapacity", str(value["min_target_capacity"]))
        )
    if "max_total_price" in value:
        pairs.append((f"{key_prefix}MaxTotalPrice", str(value["max_total_price"])))


def deserialize_ec2_query(el: Element) -> SpotOptionsRequest:
    out: SpotOptionsRequest = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("AllocationStrategy")
    if child_allocation_strategy is not None:
        import capo_ec2.types.spot_allocation_strategy

        out["allocation_strategy"] = (
            capo_ec2.types.spot_allocation_strategy.deserialize_ec2_query(
                child_allocation_strategy
            )
        )
    child_maintenance_strategies = el.find("MaintenanceStrategies")
    if child_maintenance_strategies is not None:
        import capo_ec2.types.fleet_spot_maintenance_strategies_request

        out["maintenance_strategies"] = (
            capo_ec2.types.fleet_spot_maintenance_strategies_request.deserialize_ec2_query(
                child_maintenance_strategies
            )
        )
    child_instance_interruption_behavior = el.find("InstanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import capo_ec2.types.spot_instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            capo_ec2.types.spot_instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    child_instance_pools_to_use_count = el.find("InstancePoolsToUseCount")
    if child_instance_pools_to_use_count is not None:
        out["instance_pools_to_use_count"] = int(
            child_instance_pools_to_use_count.text or ""
        )
    child_single_instance_type = el.find("SingleInstanceType")
    if child_single_instance_type is not None:
        out["single_instance_type"] = (
            child_single_instance_type.text or ""
        ).lower() == "true"
    child_single_availability_zone = el.find("SingleAvailabilityZone")
    if child_single_availability_zone is not None:
        out["single_availability_zone"] = (
            child_single_availability_zone.text or ""
        ).lower() == "true"
    child_min_target_capacity = el.find("MinTargetCapacity")
    if child_min_target_capacity is not None:
        out["min_target_capacity"] = int(child_min_target_capacity.text or "")
    child_max_total_price = el.find("MaxTotalPrice")
    if child_max_total_price is not None:
        out["max_total_price"] = str(child_max_total_price.text or "")
    return out
