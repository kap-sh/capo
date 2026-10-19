"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Firewall``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone_mappings
    import capo_network_firewall.types.aws_account_id
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.enabled_analysis_types
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.nat_gateway_mappings_list
    import capo_network_firewall.types.number_of_associations
    import capo_network_firewall.types.proxy_settings
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_id
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.subnet_mappings
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.transit_gateway_id
    import capo_network_firewall.types.vpc_endpoint
    import capo_network_firewall.types.vpc_id


class Firewall(TypedDict, closed=True):
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    firewall_policy_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls. </p>"""
    vpc_id: "capo_network_firewall.types.vpc_id.VpcId"
    """<p>The unique identifier of the VPC where the firewall is in use. </p>"""
    subnet_mappings: "capo_network_firewall.types.subnet_mappings.SubnetMappings"
    """<p>The primary public subnets that Network Firewall is using for the firewall. Network Firewall creates a firewall endpoint in each subnet. Create a subnet mapping for each Availability Zone where you want to use the firewall.</p> <p>These subnets are all defined for a single, primary VPC, and each must belong to a different Availability Zone. Each of these subnets establishes the availability of the firewall in its Availability Zone. </p> <p>In addition to these subnets, you can define other endpoints for the firewall in <code>VpcEndpointAssociation</code> resources. You can define these additional endpoints for any VPC, and for any of the Availability Zones where the firewall resource already has a subnet mapping. VPC endpoint associations give you the ability to protect multiple VPCs using a single firewall, and to define multiple firewall endpoints for a VPC in a single Availability Zone. </p>"""
    delete_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A flag indicating whether it is possible to delete the firewall. A setting of <code>TRUE</code> indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to <code>TRUE</code>.</p>"""
    subnet_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>"""
    firewall_policy_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall.</p>"""
    firewall_id: "capo_network_firewall.types.resource_id.ResourceId"
    """<p>The unique identifier for the firewall. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p></p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your firewall.</p>"""
    number_of_associations: NotRequired[
        "capo_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of <code>VpcEndpointAssociation</code> resources that use this firewall. </p>"""
    enabled_analysis_types: NotRequired[
        "capo_network_firewall.types.enabled_analysis_types.EnabledAnalysisTypes"
    ]
    """<p>An optional setting indicating the specific traffic analysis types to enable on the firewall. </p>"""
    transit_gateway_id: NotRequired[
        "capo_network_firewall.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The unique identifier of the transit gateway associated with this firewall. This field is only present for transit gateway-attached firewalls.</p>"""
    transit_gateway_owner_account_id: NotRequired[
        "capo_network_firewall.types.aws_account_id.AWSAccountId"
    ]
    """<p>The Amazon Web Services account ID that owns the transit gateway. This may be different from the firewall owner's account ID when using a shared transit gateway.</p>"""
    availability_zone_mappings: NotRequired[
        "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings"
    ]
    """<p>The Availability Zones where the firewall endpoints are created for a transit gateway-attached firewall. Each mapping specifies an Availability Zone where the firewall processes traffic.</p>"""
    availability_zone_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to <code>TRUE</code>, you must first disable this protection before adding or removing Availability Zones.</p>"""
    nat_gateway_mappings: NotRequired[
        "capo_network_firewall.types.nat_gateway_mappings_list.NatGatewayMappingsList"
    ]
    """<p>The NAT gateways that the firewall uses to proxy traffic. This is set for proxy mode firewalls, where <code>NoSourcePreservation</code> is <code>TRUE</code>. </p>"""
    proxy_settings: NotRequired[
        "capo_network_firewall.types.proxy_settings.ProxySettings"
    ]
    """<p>The listener configuration for the firewall's proxy. This is set for proxy mode firewalls, where <code>NoSourcePreservation</code> is <code>TRUE</code>. </p>"""
    no_source_preservation: "capo_network_firewall.types.boolean.Boolean"
    """<p>Indicates whether the firewall operates in proxy mode, in which the source IP address of the traffic is not preserved. When this value is <code>TRUE</code>, the firewall proxies traffic through a NAT gateway and uses the NAT gateway's IP address as the source for traffic reaching the destination. </p>"""
    vpc_endpoint: NotRequired["capo_network_firewall.types.vpc_endpoint.VpcEndpoint"]
    """<p>The VPC and subnets for the firewall endpoint. This is set for proxy mode firewalls, where <code>NoSourcePreservation</code> is <code>TRUE</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Firewall) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    out["VpcId"] = value["vpc_id"]
    import capo_network_firewall.types.subnet_mappings

    out["SubnetMappings"] = (
        capo_network_firewall.types.subnet_mappings.serialize_aws_json_1_0(
            value["subnet_mappings"]
        )
    )
    out["DeleteProtection"] = value.get("delete_protection", False)
    out["SubnetChangeProtection"] = value.get("subnet_change_protection", False)
    out["FirewallPolicyChangeProtection"] = value.get(
        "firewall_policy_change_protection", False
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["FirewallId"] = value["firewall_id"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
    if "enabled_analysis_types" in value:
        import capo_network_firewall.types.enabled_analysis_types

        out["EnabledAnalysisTypes"] = (
            capo_network_firewall.types.enabled_analysis_types.serialize_aws_json_1_0(
                value["enabled_analysis_types"]
            )
        )
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
    if "transit_gateway_owner_account_id" in value:
        out["TransitGatewayOwnerAccountId"] = value["transit_gateway_owner_account_id"]
    if "availability_zone_mappings" in value:
        import capo_network_firewall.types.availability_zone_mappings

        out["AvailabilityZoneMappings"] = (
            capo_network_firewall.types.availability_zone_mappings.serialize_aws_json_1_0(
                value["availability_zone_mappings"]
            )
        )
    out["AvailabilityZoneChangeProtection"] = value.get(
        "availability_zone_change_protection", False
    )
    if "nat_gateway_mappings" in value:
        import capo_network_firewall.types.nat_gateway_mappings_list

        out["NatGatewayMappings"] = (
            capo_network_firewall.types.nat_gateway_mappings_list.serialize_aws_json_1_0(
                value["nat_gateway_mappings"]
            )
        )
    if "proxy_settings" in value:
        import capo_network_firewall.types.proxy_settings

        out["ProxySettings"] = (
            capo_network_firewall.types.proxy_settings.serialize_aws_json_1_0(
                value["proxy_settings"]
            )
        )
    out["NoSourcePreservation"] = value.get("no_source_preservation", False)
    if "vpc_endpoint" in value:
        import capo_network_firewall.types.vpc_endpoint

        out["VpcEndpoint"] = (
            capo_network_firewall.types.vpc_endpoint.serialize_aws_json_1_0(
                value["vpc_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Firewall:
    out: Firewall = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    else:
        out["firewall_policy_arn"] = ""
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetMappings") is not None:
        import capo_network_firewall.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_network_firewall.types.subnet_mappings.deserialize_aws_json_1_0(
                data["SubnetMappings"]
            )
        )
    else:
        out["subnet_mappings"] = []
    if data.get("DeleteProtection") is not None:
        out["delete_protection"] = data["DeleteProtection"]
    else:
        out["delete_protection"] = False
    if data.get("SubnetChangeProtection") is not None:
        out["subnet_change_protection"] = data["SubnetChangeProtection"]
    else:
        out["subnet_change_protection"] = False
    if data.get("FirewallPolicyChangeProtection") is not None:
        out["firewall_policy_change_protection"] = data[
            "FirewallPolicyChangeProtection"
        ]
    else:
        out["firewall_policy_change_protection"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FirewallId") is not None:
        out["firewall_id"] = data["FirewallId"]
    else:
        out["firewall_id"] = ""
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("NumberOfAssociations") is not None:
        out["number_of_associations"] = data["NumberOfAssociations"]
    if data.get("EnabledAnalysisTypes") is not None:
        import capo_network_firewall.types.enabled_analysis_types

        out["enabled_analysis_types"] = (
            capo_network_firewall.types.enabled_analysis_types.deserialize_aws_json_1_0(
                data["EnabledAnalysisTypes"]
            )
        )
    if data.get("TransitGatewayId") is not None:
        out["transit_gateway_id"] = data["TransitGatewayId"]
    if data.get("TransitGatewayOwnerAccountId") is not None:
        out["transit_gateway_owner_account_id"] = data["TransitGatewayOwnerAccountId"]
    if data.get("AvailabilityZoneMappings") is not None:
        import capo_network_firewall.types.availability_zone_mappings

        out["availability_zone_mappings"] = (
            capo_network_firewall.types.availability_zone_mappings.deserialize_aws_json_1_0(
                data["AvailabilityZoneMappings"]
            )
        )
    if data.get("AvailabilityZoneChangeProtection") is not None:
        out["availability_zone_change_protection"] = data[
            "AvailabilityZoneChangeProtection"
        ]
    else:
        out["availability_zone_change_protection"] = False
    if data.get("NatGatewayMappings") is not None:
        import capo_network_firewall.types.nat_gateway_mappings_list

        out["nat_gateway_mappings"] = (
            capo_network_firewall.types.nat_gateway_mappings_list.deserialize_aws_json_1_0(
                data["NatGatewayMappings"]
            )
        )
    if data.get("ProxySettings") is not None:
        import capo_network_firewall.types.proxy_settings

        out["proxy_settings"] = (
            capo_network_firewall.types.proxy_settings.deserialize_aws_json_1_0(
                data["ProxySettings"]
            )
        )
    if data.get("NoSourcePreservation") is not None:
        out["no_source_preservation"] = data["NoSourcePreservation"]
    else:
        out["no_source_preservation"] = False
    if data.get("VpcEndpoint") is not None:
        import capo_network_firewall.types.vpc_endpoint

        out["vpc_endpoint"] = (
            capo_network_firewall.types.vpc_endpoint.deserialize_aws_json_1_0(
                data["VpcEndpoint"]
            )
        )
    return out
