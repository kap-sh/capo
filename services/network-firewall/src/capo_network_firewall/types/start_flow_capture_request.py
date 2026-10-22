"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartFlowCaptureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.age
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.availability_zone_id
    import capo_network_firewall.types.flow_filters
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.vpc_endpoint_id


class StartFlowCaptureRequest(TypedDict, closed=True):
    firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    availability_zone: NotRequired[
        "capo_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""
    availability_zone_id: NotRequired[
        "capo_network_firewall.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone where the firewall is located. For example, <code>use2-az1</code>. Availability Zone IDs are the same in every Amazon Web Services account, so use this parameter when you coordinate resources across accounts. Specify either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, not both. If you specify both, the request fails.</p>"""
    vpc_endpoint_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>A unique identifier for the primary endpoint associated with a firewall.</p>"""
    minimum_flow_age_in_seconds: NotRequired["capo_network_firewall.types.age.Age"]
    """<p>The reqested <code>FlowOperation</code> ignores flows with an age (in seconds) lower than <code>MinimumFlowAgeInSeconds</code>. You provide this for start commands.</p> <note> <p>We recommend setting this value to at least 1 minute (60 seconds) to reduce chance of capturing flows that are not yet established.</p> </note>"""
    flow_filters: "capo_network_firewall.types.flow_filters.FlowFilters"
    """<p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFlowCaptureRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "minimum_flow_age_in_seconds" in value:
        out["MinimumFlowAgeInSeconds"] = value["minimum_flow_age_in_seconds"]
    import capo_network_firewall.types.flow_filters

    out["FlowFilters"] = (
        capo_network_firewall.types.flow_filters.serialize_aws_json_1_0(
            value["flow_filters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFlowCaptureRequest:
    out: StartFlowCaptureRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        out["firewall_arn"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("MinimumFlowAgeInSeconds") is not None:
        out["minimum_flow_age_in_seconds"] = data["MinimumFlowAgeInSeconds"]
    if data.get("FlowFilters") is not None:
        import capo_network_firewall.types.flow_filters

        out["flow_filters"] = (
            capo_network_firewall.types.flow_filters.deserialize_aws_json_1_0(
                data["FlowFilters"]
            )
        )
    else:
        out["flow_filters"] = []
    return out
