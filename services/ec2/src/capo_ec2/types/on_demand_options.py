"""Generated from Smithy shape ``com.amazonaws.ec2#OnDemandOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_options
    import capo_ec2.types.fleet_on_demand_allocation_strategy
    import capo_ec2.types.integer
    import capo_ec2.types.string


class OnDemandOptions(TypedDict, closed=True):
    allocation_strategy: NotRequired[
        "capo_ec2.types.fleet_on_demand_allocation_strategy.FleetOnDemandAllocationStrategy"
    ]
    """<p>The strategy that determines the order of the launch template overrides to use in fulfilling On-Demand capacity.</p> <p> <code>lowest-price</code> - EC2 Fleet uses price to determine the order, launching the lowest price first.</p> <p> <code>prioritized</code> - EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first.</p> <p>Default: <code>lowest-price</code> </p>"""
    capacity_reservation_options: NotRequired[
        "capo_ec2.types.capacity_reservation_options.CapacityReservationOptions"
    ]
    """<p>The strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    single_instance_type: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    single_availability_zone: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    min_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum target capacity for On-Demand Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.</p> <p>Constraints: Maximum value of <code>1000</code>. Supported only for fleets of type <code>instant</code>.</p> <p>At least one of the following must be specified: <code>SingleAvailabilityZone</code> | <code>SingleInstanceType</code> </p>"""
    max_total_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum amount per hour for On-Demand Instances that you're willing to pay.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>maxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>maxTotalPrice</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OnDemandOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        import capo_ec2.types.fleet_on_demand_allocation_strategy

        capo_ec2.types.fleet_on_demand_allocation_strategy.serialize_ec2_query(
            value["allocation_strategy"], pairs, f"{key_prefix}AllocationStrategy"
        )
    if "capacity_reservation_options" in value:
        import capo_ec2.types.capacity_reservation_options

        capo_ec2.types.capacity_reservation_options.serialize_ec2_query(
            value["capacity_reservation_options"],
            pairs,
            f"{key_prefix}CapacityReservationOptions",
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


def deserialize_ec2_query(el: Element) -> OnDemandOptions:
    out: OnDemandOptions = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("allocationStrategy")
    if child_allocation_strategy is not None:
        import capo_ec2.types.fleet_on_demand_allocation_strategy

        out["allocation_strategy"] = (
            capo_ec2.types.fleet_on_demand_allocation_strategy.deserialize_ec2_query(
                child_allocation_strategy
            )
        )
    child_capacity_reservation_options = el.find("capacityReservationOptions")
    if child_capacity_reservation_options is not None:
        import capo_ec2.types.capacity_reservation_options

        out["capacity_reservation_options"] = (
            capo_ec2.types.capacity_reservation_options.deserialize_ec2_query(
                child_capacity_reservation_options
            )
        )
    child_single_instance_type = el.find("singleInstanceType")
    if child_single_instance_type is not None:
        out["single_instance_type"] = (
            child_single_instance_type.text or ""
        ).lower() == "true"
    child_single_availability_zone = el.find("singleAvailabilityZone")
    if child_single_availability_zone is not None:
        out["single_availability_zone"] = (
            child_single_availability_zone.text or ""
        ).lower() == "true"
    child_min_target_capacity = el.find("minTargetCapacity")
    if child_min_target_capacity is not None:
        out["min_target_capacity"] = int(child_min_target_capacity.text or "")
    child_max_total_price = el.find("maxTotalPrice")
    if child_max_total_price is not None:
        out["max_total_price"] = str(child_max_total_price.text or "")
    return out
