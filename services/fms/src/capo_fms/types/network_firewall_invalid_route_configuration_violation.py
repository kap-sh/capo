"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallInvalidRouteConfigurationViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.expected_routes
    import capo_fms.types.resource_id
    import capo_fms.types.resource_id_list
    import capo_fms.types.route
    import capo_fms.types.routes


class NetworkFirewallInvalidRouteConfigurationViolation(TypedDict, closed=True):
    affected_subnets: NotRequired["capo_fms.types.resource_id_list.ResourceIdList"]
    """<p>The subnets that are affected.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The route table ID.</p>"""
    is_route_table_used_in_different_az: "capo_fms.types.boolean.Boolean"
    """<p>Information about whether the route table is used in another Availability Zone.</p>"""
    violating_route: NotRequired["capo_fms.types.route.Route"]
    """<p>The route that's in violation.</p>"""
    current_firewall_subnet_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>The subnet route table for the current firewall.</p>"""
    expected_firewall_endpoint: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The firewall endpoint that's expected.</p>"""
    actual_firewall_endpoint: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The actual firewall endpoint.</p>"""
    expected_firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The expected subnet ID for the firewall.</p>"""
    actual_firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The actual subnet ID for the firewall.</p>"""
    expected_firewall_subnet_routes: NotRequired[
        "capo_fms.types.expected_routes.ExpectedRoutes"
    ]
    """<p>The firewall subnet routes that are expected.</p>"""
    actual_firewall_subnet_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The actual firewall subnet routes that are expected.</p>"""
    internet_gateway_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The internet gateway ID.</p>"""
    current_internet_gateway_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>The route table for the current internet gateway.</p>"""
    expected_internet_gateway_routes: NotRequired[
        "capo_fms.types.expected_routes.ExpectedRoutes"
    ]
    """<p>The expected routes for the internet gateway.</p>"""
    actual_internet_gateway_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The actual internet gateway routes.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallInvalidRouteConfigurationViolation,
) -> dict:
    out: dict = {}
    if "affected_subnets" in value:
        import capo_fms.types.resource_id_list

        out["AffectedSubnets"] = capo_fms.types.resource_id_list.serialize_aws_json_1_1(
            value["affected_subnets"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    out["IsRouteTableUsedInDifferentAZ"] = value.get(
        "is_route_table_used_in_different_az", False
    )
    if "violating_route" in value:
        import capo_fms.types.route

        out["ViolatingRoute"] = capo_fms.types.route.serialize_aws_json_1_1(
            value["violating_route"]
        )
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "expected_firewall_endpoint" in value:
        out["ExpectedFirewallEndpoint"] = value["expected_firewall_endpoint"]
    if "actual_firewall_endpoint" in value:
        out["ActualFirewallEndpoint"] = value["actual_firewall_endpoint"]
    if "expected_firewall_subnet_id" in value:
        out["ExpectedFirewallSubnetId"] = value["expected_firewall_subnet_id"]
    if "actual_firewall_subnet_id" in value:
        out["ActualFirewallSubnetId"] = value["actual_firewall_subnet_id"]
    if "expected_firewall_subnet_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedFirewallSubnetRoutes"] = (
            capo_fms.types.expected_routes.serialize_aws_json_1_1(
                value["expected_firewall_subnet_routes"]
            )
        )
    if "actual_firewall_subnet_routes" in value:
        import capo_fms.types.routes

        out["ActualFirewallSubnetRoutes"] = (
            capo_fms.types.routes.serialize_aws_json_1_1(
                value["actual_firewall_subnet_routes"]
            )
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "expected_internet_gateway_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedInternetGatewayRoutes"] = (
            capo_fms.types.expected_routes.serialize_aws_json_1_1(
                value["expected_internet_gateway_routes"]
            )
        )
    if "actual_internet_gateway_routes" in value:
        import capo_fms.types.routes

        out["ActualInternetGatewayRoutes"] = (
            capo_fms.types.routes.serialize_aws_json_1_1(
                value["actual_internet_gateway_routes"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallInvalidRouteConfigurationViolation:
    out: NetworkFirewallInvalidRouteConfigurationViolation = {}  # type: ignore[typeddict-item]
    if data.get("AffectedSubnets") is not None:
        import capo_fms.types.resource_id_list

        out["affected_subnets"] = (
            capo_fms.types.resource_id_list.deserialize_aws_json_1_1(
                data["AffectedSubnets"]
            )
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("IsRouteTableUsedInDifferentAZ") is not None:
        out["is_route_table_used_in_different_az"] = data[
            "IsRouteTableUsedInDifferentAZ"
        ]
    else:
        out["is_route_table_used_in_different_az"] = False
    if data.get("ViolatingRoute") is not None:
        import capo_fms.types.route

        out["violating_route"] = capo_fms.types.route.deserialize_aws_json_1_1(
            data["ViolatingRoute"]
        )
    if data.get("CurrentFirewallSubnetRouteTable") is not None:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if data.get("ExpectedFirewallEndpoint") is not None:
        out["expected_firewall_endpoint"] = data["ExpectedFirewallEndpoint"]
    if data.get("ActualFirewallEndpoint") is not None:
        out["actual_firewall_endpoint"] = data["ActualFirewallEndpoint"]
    if data.get("ExpectedFirewallSubnetId") is not None:
        out["expected_firewall_subnet_id"] = data["ExpectedFirewallSubnetId"]
    if data.get("ActualFirewallSubnetId") is not None:
        out["actual_firewall_subnet_id"] = data["ActualFirewallSubnetId"]
    if data.get("ExpectedFirewallSubnetRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_firewall_subnet_routes"] = (
            capo_fms.types.expected_routes.deserialize_aws_json_1_1(
                data["ExpectedFirewallSubnetRoutes"]
            )
        )
    if data.get("ActualFirewallSubnetRoutes") is not None:
        import capo_fms.types.routes

        out["actual_firewall_subnet_routes"] = (
            capo_fms.types.routes.deserialize_aws_json_1_1(
                data["ActualFirewallSubnetRoutes"]
            )
        )
    if data.get("InternetGatewayId") is not None:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if data.get("CurrentInternetGatewayRouteTable") is not None:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if data.get("ExpectedInternetGatewayRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_internet_gateway_routes"] = (
            capo_fms.types.expected_routes.deserialize_aws_json_1_1(
                data["ExpectedInternetGatewayRoutes"]
            )
        )
    if data.get("ActualInternetGatewayRoutes") is not None:
        import capo_fms.types.routes

        out["actual_internet_gateway_routes"] = (
            capo_fms.types.routes.deserialize_aws_json_1_1(
                data["ActualInternetGatewayRoutes"]
            )
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallInvalidRouteConfigurationViolation) -> dict:
    out: dict = {}
    if "affected_subnets" in value:
        import capo_fms.types.resource_id_list

        out["AffectedSubnets"] = capo_fms.types.resource_id_list.serialize_cbor(
            value["affected_subnets"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    out["IsRouteTableUsedInDifferentAZ"] = value.get(
        "is_route_table_used_in_different_az", False
    )
    if "violating_route" in value:
        import capo_fms.types.route

        out["ViolatingRoute"] = capo_fms.types.route.serialize_cbor(
            value["violating_route"]
        )
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "expected_firewall_endpoint" in value:
        out["ExpectedFirewallEndpoint"] = value["expected_firewall_endpoint"]
    if "actual_firewall_endpoint" in value:
        out["ActualFirewallEndpoint"] = value["actual_firewall_endpoint"]
    if "expected_firewall_subnet_id" in value:
        out["ExpectedFirewallSubnetId"] = value["expected_firewall_subnet_id"]
    if "actual_firewall_subnet_id" in value:
        out["ActualFirewallSubnetId"] = value["actual_firewall_subnet_id"]
    if "expected_firewall_subnet_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedFirewallSubnetRoutes"] = (
            capo_fms.types.expected_routes.serialize_cbor(
                value["expected_firewall_subnet_routes"]
            )
        )
    if "actual_firewall_subnet_routes" in value:
        import capo_fms.types.routes

        out["ActualFirewallSubnetRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["actual_firewall_subnet_routes"]
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "expected_internet_gateway_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedInternetGatewayRoutes"] = (
            capo_fms.types.expected_routes.serialize_cbor(
                value["expected_internet_gateway_routes"]
            )
        )
    if "actual_internet_gateway_routes" in value:
        import capo_fms.types.routes

        out["ActualInternetGatewayRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["actual_internet_gateway_routes"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallInvalidRouteConfigurationViolation:
    out: NetworkFirewallInvalidRouteConfigurationViolation = {}  # type: ignore[typeddict-item]
    if data.get("AffectedSubnets") is not None:
        import capo_fms.types.resource_id_list

        out["affected_subnets"] = capo_fms.types.resource_id_list.deserialize_cbor(
            data["AffectedSubnets"]
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("IsRouteTableUsedInDifferentAZ") is not None:
        out["is_route_table_used_in_different_az"] = data[
            "IsRouteTableUsedInDifferentAZ"
        ]
    else:
        out["is_route_table_used_in_different_az"] = False
    if data.get("ViolatingRoute") is not None:
        import capo_fms.types.route

        out["violating_route"] = capo_fms.types.route.deserialize_cbor(
            data["ViolatingRoute"]
        )
    if data.get("CurrentFirewallSubnetRouteTable") is not None:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if data.get("ExpectedFirewallEndpoint") is not None:
        out["expected_firewall_endpoint"] = data["ExpectedFirewallEndpoint"]
    if data.get("ActualFirewallEndpoint") is not None:
        out["actual_firewall_endpoint"] = data["ActualFirewallEndpoint"]
    if data.get("ExpectedFirewallSubnetId") is not None:
        out["expected_firewall_subnet_id"] = data["ExpectedFirewallSubnetId"]
    if data.get("ActualFirewallSubnetId") is not None:
        out["actual_firewall_subnet_id"] = data["ActualFirewallSubnetId"]
    if data.get("ExpectedFirewallSubnetRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_firewall_subnet_routes"] = (
            capo_fms.types.expected_routes.deserialize_cbor(
                data["ExpectedFirewallSubnetRoutes"]
            )
        )
    if data.get("ActualFirewallSubnetRoutes") is not None:
        import capo_fms.types.routes

        out["actual_firewall_subnet_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["ActualFirewallSubnetRoutes"]
        )
    if data.get("InternetGatewayId") is not None:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if data.get("CurrentInternetGatewayRouteTable") is not None:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if data.get("ExpectedInternetGatewayRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_internet_gateway_routes"] = (
            capo_fms.types.expected_routes.deserialize_cbor(
                data["ExpectedInternetGatewayRoutes"]
            )
        )
    if data.get("ActualInternetGatewayRoutes") is not None:
        import capo_fms.types.routes

        out["actual_internet_gateway_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["ActualInternetGatewayRoutes"]
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out
