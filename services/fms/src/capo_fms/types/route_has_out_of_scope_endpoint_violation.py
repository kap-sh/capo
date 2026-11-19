"""Generated from Smithy shape ``com.amazonaws.fms#RouteHasOutOfScopeEndpointViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id
    import capo_fms.types.routes


class RouteHasOutOfScopeEndpointViolation(TypedDict, closed=True):
    subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the subnet associated with the route that violates the policy scope.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The VPC ID of the route that violates the policy scope.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the route table.</p>"""
    violating_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The list of routes that violate the route table.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The subnet's Availability Zone.</p>"""
    subnet_availability_zone_id: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The ID of the subnet's Availability Zone.</p>"""
    current_firewall_subnet_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>The route table associated with the current firewall subnet.</p>"""
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the firewall subnet.</p>"""
    firewall_subnet_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The list of firewall subnet routes.</p>"""
    internet_gateway_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the Internet Gateway.</p>"""
    current_internet_gateway_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>The current route table associated with the Internet Gateway.</p>"""
    internet_gateway_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The routes in the route table associated with the Internet Gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteHasOutOfScopeEndpointViolation) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "firewall_subnet_routes" in value:
        import capo_fms.types.routes

        out["FirewallSubnetRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["firewall_subnet_routes"]
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "internet_gateway_routes" in value:
        import capo_fms.types.routes

        out["InternetGatewayRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["internet_gateway_routes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RouteHasOutOfScopeEndpointViolation:
    out: RouteHasOutOfScopeEndpointViolation = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if data.get("CurrentFirewallSubnetRouteTable") is not None:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("FirewallSubnetRoutes") is not None:
        import capo_fms.types.routes

        out["firewall_subnet_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["FirewallSubnetRoutes"]
        )
    if data.get("InternetGatewayId") is not None:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if data.get("CurrentInternetGatewayRouteTable") is not None:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if data.get("InternetGatewayRoutes") is not None:
        import capo_fms.types.routes

        out["internet_gateway_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["InternetGatewayRoutes"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteHasOutOfScopeEndpointViolation) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["violating_routes"]
        )
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "firewall_subnet_routes" in value:
        import capo_fms.types.routes

        out["FirewallSubnetRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["firewall_subnet_routes"]
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "internet_gateway_routes" in value:
        import capo_fms.types.routes

        out["InternetGatewayRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["internet_gateway_routes"]
        )
    return out


def deserialize_cbor(data: dict) -> RouteHasOutOfScopeEndpointViolation:
    out: RouteHasOutOfScopeEndpointViolation = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["ViolatingRoutes"]
        )
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if data.get("CurrentFirewallSubnetRouteTable") is not None:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("FirewallSubnetRoutes") is not None:
        import capo_fms.types.routes

        out["firewall_subnet_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["FirewallSubnetRoutes"]
        )
    if data.get("InternetGatewayId") is not None:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if data.get("CurrentInternetGatewayRouteTable") is not None:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if data.get("InternetGatewayRoutes") is not None:
        import capo_fms.types.routes

        out["internet_gateway_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["InternetGatewayRoutes"]
        )
    return out
