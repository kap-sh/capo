"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.always_on_capacity
    import capo_gameliftstreams.types.capacity_value
    import capo_gameliftstreams.types.ipv4_cidr_block
    import capo_gameliftstreams.types.location_name
    import capo_gameliftstreams.types.maximum_capacity
    import capo_gameliftstreams.types.on_demand_capacity
    import capo_gameliftstreams.types.stream_group_location_status
    import capo_gameliftstreams.types.target_idle_capacity
    import capo_gameliftstreams.types.vpc_transit_configuration_response


class LocationState(TypedDict, closed=True):
    location_name: NotRequired["capo_gameliftstreams.types.location_name.LocationName"]
    """<p> A location's name. For example, <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    status: NotRequired[
        "capo_gameliftstreams.types.stream_group_location_status.StreamGroupLocationStatus"
    ]
    """<p>This value is set of locations, including their name, current status, and capacities. </p> <p>A location can be in one of the following states:</p> <ul> <li> <p> <code>ACTIVATING</code>: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.</p> </li> <li> <p> <code>ACTIVE</code>: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.</p> </li> <li> <p> <code>ERROR</code>: Amazon GameLift Streams failed to set up this location. The <code>StatusReason</code> field describes the error. You can remove this location and try to add it again.</p> </li> <li> <p> <code>REMOVING</code>: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.</p> </li> </ul>"""
    always_on_capacity: NotRequired[
        "capo_gameliftstreams.types.always_on_capacity.AlwaysOnCapacity"
    ]
    """<p>This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.</p>"""
    on_demand_capacity: NotRequired[
        "capo_gameliftstreams.types.on_demand_capacity.OnDemandCapacity"
    ]
    """<p>The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes). Default is 0 when creating a stream group or adding a location.</p>"""
    target_idle_capacity: NotRequired[
        "capo_gameliftstreams.types.target_idle_capacity.TargetIdleCapacity"
    ]
    """<p>This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.</p>"""
    maximum_capacity: NotRequired[
        "capo_gameliftstreams.types.maximum_capacity.MaximumCapacity"
    ]
    """<p>This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.</p>"""
    requested_capacity: NotRequired[
        "capo_gameliftstreams.types.capacity_value.CapacityValue"
    ]
    """<p>This value is the always-on capacity that you most recently requested for a stream group. You request capacity separately for each location in a stream group. In response to an increase in requested capacity, Amazon GameLift Streams attempts to provision compute resources to make the stream group's allocated capacity meet requested capacity. When always-on capacity is decreased, it can take a few minutes to deprovision allocated capacity to match the requested capacity.</p>"""
    allocated_capacity: NotRequired[
        "capo_gameliftstreams.types.capacity_value.CapacityValue"
    ]
    """<p>This value is the stream capacity that Amazon GameLift Streams has provisioned in a stream group that can respond immediately to stream requests. It includes resources that are currently streaming and resources that are idle and ready to respond to stream requests. When target-idle capacity is configured, the idle resources include the capacity buffer maintained beyond ongoing sessions. You pay for this capacity whether it's in use or not. After making changes to capacity, it can take a few minutes for the allocated capacity count to reflect the change while compute resources are allocated or deallocated. Similarly, when allocated on-demand capacity is no longer needed, it can take a few minutes for Amazon GameLift Streams to spin down the allocated capacity.</p>"""
    idle_capacity: NotRequired[
        "capo_gameliftstreams.types.capacity_value.CapacityValue"
    ]
    """<p>This value is the amount of allocated capacity that is not currently streaming. It represents the stream group's ability to respond immediately to new stream requests with near-instant startup time.</p>"""
    internal_vpc_ipv4_cidr_block: NotRequired[
        "capo_gameliftstreams.types.ipv4_cidr_block.Ipv4CidrBlock"
    ]
    """<p>The CIDR block of the service VPC for this location. Add this CIDR block to your VPC route table to enable traffic routing through the Transit Gateway.</p>"""
    vpc_transit_configuration: NotRequired[
        "capo_gameliftstreams.types.vpc_transit_configuration_response.VpcTransitConfigurationResponse"
    ]
    """<p>The VPC transit configuration for this location, including the Transit Gateway details needed to complete the VPC attachment setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationState) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    if "status" in value:
        import capo_gameliftstreams.types.stream_group_location_status

        out["Status"] = (
            capo_gameliftstreams.types.stream_group_location_status.serialize_json(
                value["status"]
            )
        )
    if "always_on_capacity" in value:
        out["AlwaysOnCapacity"] = value["always_on_capacity"]
    if "on_demand_capacity" in value:
        out["OnDemandCapacity"] = value["on_demand_capacity"]
    if "target_idle_capacity" in value:
        out["TargetIdleCapacity"] = value["target_idle_capacity"]
    if "maximum_capacity" in value:
        out["MaximumCapacity"] = value["maximum_capacity"]
    if "requested_capacity" in value:
        out["RequestedCapacity"] = value["requested_capacity"]
    if "allocated_capacity" in value:
        out["AllocatedCapacity"] = value["allocated_capacity"]
    if "idle_capacity" in value:
        out["IdleCapacity"] = value["idle_capacity"]
    if "internal_vpc_ipv4_cidr_block" in value:
        out["InternalVpcIpv4CidrBlock"] = value["internal_vpc_ipv4_cidr_block"]
    if "vpc_transit_configuration" in value:
        import capo_gameliftstreams.types.vpc_transit_configuration_response

        out["VpcTransitConfiguration"] = (
            capo_gameliftstreams.types.vpc_transit_configuration_response.serialize_json(
                value["vpc_transit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LocationState:
    out: LocationState = {}  # type: ignore[typeddict-item]
    if data.get("LocationName") is not None:
        out["location_name"] = data["LocationName"]
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.stream_group_location_status

        out["status"] = (
            capo_gameliftstreams.types.stream_group_location_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("AlwaysOnCapacity") is not None:
        out["always_on_capacity"] = data["AlwaysOnCapacity"]
    if data.get("OnDemandCapacity") is not None:
        out["on_demand_capacity"] = data["OnDemandCapacity"]
    if data.get("TargetIdleCapacity") is not None:
        out["target_idle_capacity"] = data["TargetIdleCapacity"]
    if data.get("MaximumCapacity") is not None:
        out["maximum_capacity"] = data["MaximumCapacity"]
    if data.get("RequestedCapacity") is not None:
        out["requested_capacity"] = data["RequestedCapacity"]
    if data.get("AllocatedCapacity") is not None:
        out["allocated_capacity"] = data["AllocatedCapacity"]
    if data.get("IdleCapacity") is not None:
        out["idle_capacity"] = data["IdleCapacity"]
    if data.get("InternalVpcIpv4CidrBlock") is not None:
        out["internal_vpc_ipv4_cidr_block"] = data["InternalVpcIpv4CidrBlock"]
    if data.get("VpcTransitConfiguration") is not None:
        import capo_gameliftstreams.types.vpc_transit_configuration_response

        out["vpc_transit_configuration"] = (
            capo_gameliftstreams.types.vpc_transit_configuration_response.deserialize_json(
                data["VpcTransitConfiguration"]
            )
        )
    return out
