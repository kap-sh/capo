"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.always_on_capacity
    import capo_gameliftstreams.types.location_name
    import capo_gameliftstreams.types.maximum_capacity
    import capo_gameliftstreams.types.on_demand_capacity
    import capo_gameliftstreams.types.target_idle_capacity
    import capo_gameliftstreams.types.vpc_transit_configuration


class LocationConfiguration(TypedDict, closed=True):
    location_name: "capo_gameliftstreams.types.location_name.LocationName"
    """<p> A location's name. For example, <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    always_on_capacity: NotRequired[
        "capo_gameliftstreams.types.always_on_capacity.AlwaysOnCapacity"
    ]
    """<p>This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.</p>"""
    on_demand_capacity: NotRequired[
        "capo_gameliftstreams.types.on_demand_capacity.OnDemandCapacity"
    ]
    """<p>This field is deprecated. Use <code>MaximumCapacity</code> instead. This parameter cannot be used with <code>MaximumCapacity</code> or <code>TargetIdleCapacity</code> in the same location configuration.</p> <p>The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes). Default is 0 when creating a stream group or adding a location.</p>"""
    target_idle_capacity: NotRequired[
        "capo_gameliftstreams.types.target_idle_capacity.TargetIdleCapacity"
    ]
    """<p>This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.</p>"""
    maximum_capacity: NotRequired[
        "capo_gameliftstreams.types.maximum_capacity.MaximumCapacity"
    ]
    """<p>This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.</p>"""
    vpc_transit_configuration: NotRequired[
        "capo_gameliftstreams.types.vpc_transit_configuration.VpcTransitConfiguration"
    ]
    """<p>Configuration for connecting the stream group to resources in your Amazon VPC using AWS Transit Gateway. This setting is optional. If specified, Amazon GameLift Streams creates a Transit Gateway to enable private network connectivity between the service VPC and your VPC. The VPC ID cannot be changed after the stream group is created, but you can update the CIDR blocks by calling <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html">UpdateStreamGroup</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationConfiguration) -> dict:
    out: dict = {}
    out["LocationName"] = value["location_name"]
    if "always_on_capacity" in value:
        out["AlwaysOnCapacity"] = value["always_on_capacity"]
    if "on_demand_capacity" in value:
        out["OnDemandCapacity"] = value["on_demand_capacity"]
    if "target_idle_capacity" in value:
        out["TargetIdleCapacity"] = value["target_idle_capacity"]
    if "maximum_capacity" in value:
        out["MaximumCapacity"] = value["maximum_capacity"]
    if "vpc_transit_configuration" in value:
        import capo_gameliftstreams.types.vpc_transit_configuration

        out["VpcTransitConfiguration"] = (
            capo_gameliftstreams.types.vpc_transit_configuration.serialize_json(
                value["vpc_transit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LocationConfiguration:
    out: LocationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LocationName") is not None:
        out["location_name"] = data["LocationName"]
    else:
        raise DeserializationError("LocationConfiguration.location_name required")
    if data.get("AlwaysOnCapacity") is not None:
        out["always_on_capacity"] = data["AlwaysOnCapacity"]
    if data.get("OnDemandCapacity") is not None:
        out["on_demand_capacity"] = data["OnDemandCapacity"]
    if data.get("TargetIdleCapacity") is not None:
        out["target_idle_capacity"] = data["TargetIdleCapacity"]
    if data.get("MaximumCapacity") is not None:
        out["maximum_capacity"] = data["MaximumCapacity"]
    if data.get("VpcTransitConfiguration") is not None:
        import capo_gameliftstreams.types.vpc_transit_configuration

        out["vpc_transit_configuration"] = (
            capo_gameliftstreams.types.vpc_transit_configuration.deserialize_json(
                data["VpcTransitConfiguration"]
            )
        )
    return out
