"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.dns_entry_set
    import capo_ec2.types.dns_options
    import capo_ec2.types.group_identifier_set
    import capo_ec2.types.ip_address_type
    import capo_ec2.types.last_error
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.payer_responsibility_set
    import capo_ec2.types.resource_configuration_arn
    import capo_ec2.types.service_network_arn
    import capo_ec2.types.state
    import capo_ec2.types.string
    import capo_ec2.types.subnet_ip_prefixes_list
    import capo_ec2.types.tag_list
    import capo_ec2.types.value_string_list
    import capo_ec2.types.vpc_endpoint_type


class VpcEndpoint(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the endpoint.</p>"""
    vpc_endpoint_type: NotRequired["capo_ec2.types.vpc_endpoint_type.VpcEndpointType"]
    """<p>The type of endpoint.</p> <p>For more information about the types of VPC endpoints, see <a href="https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html#concepts-vpc-endpoints">VPC endpoints</a> in the <i>Amazon Web Services PrivateLink User Guide</i>.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC to which the endpoint is associated.</p>"""
    service_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the service to which the endpoint is associated.</p>"""
    state: NotRequired["capo_ec2.types.state.State"]
    """<p>The state of the endpoint.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The policy document associated with the endpoint, if applicable.</p>"""
    route_table_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>(Gateway endpoint) The IDs of the route tables associated with the endpoint.</p>"""
    subnet_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>(Interface, Gateway Load Balancer endpoints, Resource, ServiceNetwork, and Tunnel endpoints only) The subnets for the endpoint.</p>"""
    groups: NotRequired["capo_ec2.types.group_identifier_set.GroupIdentifierSet"]
    """<p>(Interface, Resource, ServiceNetwork, and Tunnel endpoints only) Information about the security groups that are associated with the network interface.</p>"""
    ip_address_type: NotRequired["capo_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    dns_options: NotRequired["capo_ec2.types.dns_options.DnsOptions"]
    """<p>The DNS options for the endpoint.</p>"""
    private_dns_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.</p>"""
    requester_managed: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the endpoint is being managed by its service.</p>"""
    network_interface_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>(Interface, Gateway Load Balancer endpoints, Resource, ServiceNetwork, and Tunnel endpoints only) The network interfaces for the endpoint.</p>"""
    dns_entries: NotRequired["capo_ec2.types.dns_entry_set.DnsEntrySet"]
    """<p>(Interface endpoint) The DNS entries for the endpoint.</p>"""
    creation_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the endpoint was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the endpoint.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the endpoint.</p>"""
    last_error: NotRequired["capo_ec2.types.last_error.LastError"]
    """<p>The last error that occurred for endpoint.</p>"""
    ipv4_prefixes: NotRequired[
        "capo_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv4 prefixes.</p>"""
    ipv6_prefixes: NotRequired[
        "capo_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv6 prefixes.</p>"""
    failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>Reason for the failure.</p>"""
    service_network_arn: NotRequired[
        "capo_ec2.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    resource_configuration_arn: NotRequired[
        "capo_ec2.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    service_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""
    payer_responsibilities: NotRequired[
        "capo_ec2.types.payer_responsibility_set.PayerResponsibilitySet"
    ]
    """<p>The payer responsibility settings for the endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "vpc_endpoint_type" in value:
        import capo_ec2.types.vpc_endpoint_type

        capo_ec2.types.vpc_endpoint_type.serialize_ec2_query(
            value["vpc_endpoint_type"], pairs, f"{key_prefix}VpcEndpointType"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "service_name" in value:
        pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "state" in value:
        import capo_ec2.types.state

        capo_ec2.types.state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "route_table_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["route_table_ids"], pairs, f"{key_prefix}RouteTableIdSet"
        )
    if "subnet_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIdSet"
        )
    if "groups" in value:
        import capo_ec2.types.group_identifier_set

        capo_ec2.types.group_identifier_set.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "ip_address_type" in value:
        import capo_ec2.types.ip_address_type

        capo_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )
    if "dns_options" in value:
        import capo_ec2.types.dns_options

        capo_ec2.types.dns_options.serialize_ec2_query(
            value["dns_options"], pairs, f"{key_prefix}DnsOptions"
        )
    if "private_dns_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PrivateDnsEnabled",
                "true" if value["private_dns_enabled"] else "false",
            )
        )
    if "requester_managed" in value:
        pairs.append(
            (
                f"{key_prefix}RequesterManaged",
                "true" if value["requester_managed"] else "false",
            )
        )
    if "network_interface_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["network_interface_ids"], pairs, f"{key_prefix}NetworkInterfaceIdSet"
        )
    if "dns_entries" in value:
        import capo_ec2.types.dns_entry_set

        capo_ec2.types.dns_entry_set.serialize_ec2_query(
            value["dns_entries"], pairs, f"{key_prefix}DnsEntrySet"
        )
    if "creation_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_timestamp"], pairs, f"{key_prefix}CreationTimestamp"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "last_error" in value:
        import capo_ec2.types.last_error

        capo_ec2.types.last_error.serialize_ec2_query(
            value["last_error"], pairs, f"{key_prefix}LastError"
        )
    if "ipv4_prefixes" in value:
        import capo_ec2.types.subnet_ip_prefixes_list

        capo_ec2.types.subnet_ip_prefixes_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4PrefixSet"
        )
    if "ipv6_prefixes" in value:
        import capo_ec2.types.subnet_ip_prefixes_list

        capo_ec2.types.subnet_ip_prefixes_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6PrefixSet"
        )
    if "failure_reason" in value:
        pairs.append((f"{key_prefix}FailureReason", str(value["failure_reason"])))
    if "service_network_arn" in value:
        pairs.append(
            (f"{key_prefix}ServiceNetworkArn", str(value["service_network_arn"]))
        )
    if "resource_configuration_arn" in value:
        pairs.append(
            (
                f"{key_prefix}ResourceConfigurationArn",
                str(value["resource_configuration_arn"]),
            )
        )
    if "service_region" in value:
        pairs.append((f"{key_prefix}ServiceRegion", str(value["service_region"])))
    if "payer_responsibilities" in value:
        import capo_ec2.types.payer_responsibility_set

        capo_ec2.types.payer_responsibility_set.serialize_ec2_query(
            value["payer_responsibilities"],
            pairs,
            f"{key_prefix}PayerResponsibilitySet",
        )


def deserialize_ec2_query(el: Element) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    child_vpc_endpoint_id = el.find("vpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_vpc_endpoint_type = el.find("vpcEndpointType")
    if child_vpc_endpoint_type is not None:
        import capo_ec2.types.vpc_endpoint_type

        out["vpc_endpoint_type"] = (
            capo_ec2.types.vpc_endpoint_type.deserialize_ec2_query(
                child_vpc_endpoint_type
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_service_name = el.find("serviceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.state

        out["state"] = capo_ec2.types.state.deserialize_ec2_query(child_state)
    child_policy_document = el.find("policyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_route_table_ids = el.find("routeTableIdSet")
    if child_route_table_ids is not None:
        import capo_ec2.types.value_string_list

        out["route_table_ids"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_route_table_ids
        )
    child_subnet_ids = el.find("subnetIdSet")
    if child_subnet_ids is not None:
        import capo_ec2.types.value_string_list

        out["subnet_ids"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_subnet_ids
        )
    child_groups = el.find("groupSet")
    if child_groups is not None:
        import capo_ec2.types.group_identifier_set

        out["groups"] = capo_ec2.types.group_identifier_set.deserialize_ec2_query(
            child_groups
        )
    child_ip_address_type = el.find("ipAddressType")
    if child_ip_address_type is not None:
        import capo_ec2.types.ip_address_type

        out["ip_address_type"] = capo_ec2.types.ip_address_type.deserialize_ec2_query(
            child_ip_address_type
        )
    child_dns_options = el.find("dnsOptions")
    if child_dns_options is not None:
        import capo_ec2.types.dns_options

        out["dns_options"] = capo_ec2.types.dns_options.deserialize_ec2_query(
            child_dns_options
        )
    child_private_dns_enabled = el.find("privateDnsEnabled")
    if child_private_dns_enabled is not None:
        out["private_dns_enabled"] = (
            child_private_dns_enabled.text or ""
        ).lower() == "true"
    child_requester_managed = el.find("requesterManaged")
    if child_requester_managed is not None:
        out["requester_managed"] = (
            child_requester_managed.text or ""
        ).lower() == "true"
    child_network_interface_ids = el.find("networkInterfaceIdSet")
    if child_network_interface_ids is not None:
        import capo_ec2.types.value_string_list

        out["network_interface_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_network_interface_ids
            )
        )
    child_dns_entries = el.find("dnsEntrySet")
    if child_dns_entries is not None:
        import capo_ec2.types.dns_entry_set

        out["dns_entries"] = capo_ec2.types.dns_entry_set.deserialize_ec2_query(
            child_dns_entries
        )
    child_creation_timestamp = el.find("creationTimestamp")
    if child_creation_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_timestamp
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_last_error = el.find("lastError")
    if child_last_error is not None:
        import capo_ec2.types.last_error

        out["last_error"] = capo_ec2.types.last_error.deserialize_ec2_query(
            child_last_error
        )
    child_ipv4_prefixes = el.find("ipv4PrefixSet")
    if child_ipv4_prefixes is not None:
        import capo_ec2.types.subnet_ip_prefixes_list

        out["ipv4_prefixes"] = (
            capo_ec2.types.subnet_ip_prefixes_list.deserialize_ec2_query(
                child_ipv4_prefixes
            )
        )
    child_ipv6_prefixes = el.find("ipv6PrefixSet")
    if child_ipv6_prefixes is not None:
        import capo_ec2.types.subnet_ip_prefixes_list

        out["ipv6_prefixes"] = (
            capo_ec2.types.subnet_ip_prefixes_list.deserialize_ec2_query(
                child_ipv6_prefixes
            )
        )
    child_failure_reason = el.find("failureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    child_service_network_arn = el.find("serviceNetworkArn")
    if child_service_network_arn is not None:
        out["service_network_arn"] = str(child_service_network_arn.text or "")
    child_resource_configuration_arn = el.find("resourceConfigurationArn")
    if child_resource_configuration_arn is not None:
        out["resource_configuration_arn"] = str(
            child_resource_configuration_arn.text or ""
        )
    child_service_region = el.find("serviceRegion")
    if child_service_region is not None:
        out["service_region"] = str(child_service_region.text or "")
    child_payer_responsibilities = el.find("payerResponsibilitySet")
    if child_payer_responsibilities is not None:
        import capo_ec2.types.payer_responsibility_set

        out["payer_responsibilities"] = (
            capo_ec2.types.payer_responsibility_set.deserialize_ec2_query(
                child_payer_responsibilities
            )
        )
    return out
