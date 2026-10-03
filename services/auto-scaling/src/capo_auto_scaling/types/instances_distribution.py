"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstancesDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.distribution_segments
    import capo_auto_scaling.types.mixed_instance_spot_price
    import capo_auto_scaling.types.on_demand_base_capacity
    import capo_auto_scaling.types.on_demand_percentage_above_base_capacity
    import capo_auto_scaling.types.spot_instance_pools
    import capo_auto_scaling.types.xml_string


class InstancesDistribution(TypedDict, closed=True):
    on_demand_allocation_strategy: NotRequired[
        "capo_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The allocation strategy to apply to your On-Demand Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.</p> <p>The following lists the valid values:</p> <dl> <dt>lowest-price</dt> <dd> <p>Uses price to determine which instance types are the highest priority, launching the lowest priced instance types within an Availability Zone first. This is the default value for Auto Scaling groups that specify <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html">InstanceRequirements</a>. </p> </dd> <dt>prioritized</dt> <dd> <p>You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling launches your highest priority instance types first. If all your On-Demand capacity cannot be fulfilled using your highest priority instance type, then Amazon EC2 Auto Scaling launches the remaining capacity using the second priority instance type, and so on. This is the default value for Auto Scaling groups that don't specify <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html">InstanceRequirements</a> and cannot be used for groups that do.</p> </dd> </dl>"""
    on_demand_base_capacity: NotRequired[
        "capo_auto_scaling.types.on_demand_base_capacity.OnDemandBaseCapacity"
    ]
    """<p>The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is launched first as your group scales.</p> <p>This number has the same unit of measurement as the group's desired capacity. If you change the default unit of measurement (number of instances) by specifying weighted capacity values in your launch template overrides list, or by changing the default desired capacity type setting of the group, you must specify this number using the same unit of measurement.</p> <p>Default: 0</p>"""
    on_demand_percentage_above_base_capacity: NotRequired[
        "capo_auto_scaling.types.on_demand_percentage_above_base_capacity.OnDemandPercentageAboveBaseCapacity"
    ]
    """<p>Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond <code>OnDemandBaseCapacity</code>. Expressed as a number (for example, 20 specifies 20% On-Demand Instances, 80% Spot Instances). If set to 100, only On-Demand Instances are used.</p> <p>Default: 100</p>"""
    spot_allocation_strategy: NotRequired[
        "capo_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The allocation strategy to apply to your Spot Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.</p> <p>The following lists the valid values:</p> <dl> <dt>capacity-optimized</dt> <dd> <p>Requests Spot Instances using pools that are optimally chosen based on the available Spot capacity. This strategy has the lowest risk of interruption. To give certain instance types a higher chance of launching first, use <code>capacity-optimized-prioritized</code>.</p> </dd> <dt>capacity-optimized-prioritized</dt> <dd> <p>You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling honors the instance type priorities on a best effort basis but optimizes for capacity first. Note that if the On-Demand allocation strategy is set to <code>prioritized</code>, the same priority is applied when fulfilling On-Demand capacity. This is not a valid value for Auto Scaling groups that specify <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html">InstanceRequirements</a>.</p> </dd> <dt>lowest-price</dt> <dd> <p>Requests Spot Instances using the lowest priced pools within an Availability Zone, across the number of Spot pools that you specify for the <code>SpotInstancePools</code> property. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. This is the default value, but it might lead to high interruption rates because this strategy only considers instance price and not available capacity.</p> </dd> <dt>price-capacity-optimized (recommended)</dt> <dd> <p>The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price.</p> </dd> </dl>"""
    spot_instance_pools: NotRequired[
        "capo_auto_scaling.types.spot_instance_pools.SpotInstancePools"
    ]
    """<p>The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the overrides. Valid only when the <code>SpotAllocationStrategy</code> is <code>lowest-price</code>. Value must be in the range of 1–20.</p> <p>Default: 2</p>"""
    spot_max_price: NotRequired[
        "capo_auto_scaling.types.mixed_instance_spot_price.MixedInstanceSpotPrice"
    ]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. If your maximum price is lower than the Spot price for the instance types that you selected, your Spot Instances are not launched. We do not recommend specifying a maximum price because it can lead to increased interruptions. When Spot Instances launch, you pay the current Spot price. To remove a maximum price that you previously set, include the property but specify an empty string ("") for the value.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify one.</p> </important> <p>Valid Range: Minimum value of 0.001</p>"""
    distribution_segments: NotRequired[
        "capo_auto_scaling.types.distribution_segments.DistributionSegments"
    ]
    """<p>The Distribution Segments configuration. Each segment contains an ordered list of capacity types to prioritize.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html">Use Distribution Segments to target multiple capacity types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstancesDistribution, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "on_demand_allocation_strategy" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandAllocationStrategy",
                str(value["on_demand_allocation_strategy"]),
            )
        )
    if "on_demand_base_capacity" in value:
        pairs.append(
            (f"{key_prefix}OnDemandBaseCapacity", str(value["on_demand_base_capacity"]))
        )
    if "on_demand_percentage_above_base_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandPercentageAboveBaseCapacity",
                str(value["on_demand_percentage_above_base_capacity"]),
            )
        )
    if "spot_allocation_strategy" in value:
        pairs.append(
            (
                f"{key_prefix}SpotAllocationStrategy",
                str(value["spot_allocation_strategy"]),
            )
        )
    if "spot_instance_pools" in value:
        pairs.append(
            (f"{key_prefix}SpotInstancePools", str(value["spot_instance_pools"]))
        )
    if "spot_max_price" in value:
        pairs.append((f"{key_prefix}SpotMaxPrice", str(value["spot_max_price"])))
    if "distribution_segments" in value:
        import capo_auto_scaling.types.distribution_segments

        capo_auto_scaling.types.distribution_segments.serialize_query(
            value["distribution_segments"], pairs, f"{key_prefix}DistributionSegments"
        )


def deserialize_query(el: Element) -> InstancesDistribution:
    out: InstancesDistribution = {}  # type: ignore[typeddict-item]
    child_on_demand_allocation_strategy = el.find("OnDemandAllocationStrategy")
    if child_on_demand_allocation_strategy is not None:
        out["on_demand_allocation_strategy"] = str(
            child_on_demand_allocation_strategy.text or ""
        )
    child_on_demand_base_capacity = el.find("OnDemandBaseCapacity")
    if child_on_demand_base_capacity is not None:
        out["on_demand_base_capacity"] = int(child_on_demand_base_capacity.text or "")
    child_on_demand_percentage_above_base_capacity = el.find(
        "OnDemandPercentageAboveBaseCapacity"
    )
    if child_on_demand_percentage_above_base_capacity is not None:
        out["on_demand_percentage_above_base_capacity"] = int(
            child_on_demand_percentage_above_base_capacity.text or ""
        )
    child_spot_allocation_strategy = el.find("SpotAllocationStrategy")
    if child_spot_allocation_strategy is not None:
        out["spot_allocation_strategy"] = str(child_spot_allocation_strategy.text or "")
    child_spot_instance_pools = el.find("SpotInstancePools")
    if child_spot_instance_pools is not None:
        out["spot_instance_pools"] = int(child_spot_instance_pools.text or "")
    child_spot_max_price = el.find("SpotMaxPrice")
    if child_spot_max_price is not None:
        out["spot_max_price"] = str(child_spot_max_price.text or "")
    child_distribution_segments = el.find("DistributionSegments")
    if child_distribution_segments is not None:
        import capo_auto_scaling.types.distribution_segments

        out["distribution_segments"] = (
            capo_auto_scaling.types.distribution_segments.deserialize_query(
                child_distribution_segments
            )
        )
    return out
