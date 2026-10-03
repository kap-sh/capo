"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_family
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ipam_netmask_length
    import capo_ec2.types.ipam_pool_aws_service
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipam_pool_public_ip_source
    import capo_ec2.types.ipam_pool_source_resource
    import capo_ec2.types.ipam_pool_state
    import capo_ec2.types.ipam_resource_tag_list
    import capo_ec2.types.ipam_scope_type
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamPool(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM pool.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool.</p>"""
    source_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the source IPAM pool. You can use this option to create an IPAM pool within an existing source pool.</p>"""
    ipam_pool_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM pool.</p>"""
    ipam_scope_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the scope of the IPAM pool.</p>"""
    ipam_scope_type: NotRequired["capo_ec2.types.ipam_scope_type.IpamScopeType"]
    """<p>In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.</p>"""
    ipam_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the IPAM.</p>"""
    ipam_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM pool.</p>"""
    locale: NotRequired["capo_ec2.types.string.String"]
    """<p>The locale of the IPAM pool.</p> <p>The locale for the pool should be one of the following:</p> <ul> <li> <p>An Amazon Web Services Region where you want this IPAM pool to be available for allocations.</p> </li> <li> <p>The network border group for an Amazon Web Services Local Zone where you want this IPAM pool to be available for allocations (<a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail">supported Local Zones</a>). This option is only available for IPAM IPv4 pools in the public scope.</p> </li> </ul> <p>If you choose an Amazon Web Services Region for locale that has not been configured as an operating Region for the IPAM, you'll get an error.</p>"""
    pool_depth: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The depth of pools in your IPAM pool. The pool depth quota is 10. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html">Quotas in IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    state: NotRequired["capo_ec2.types.ipam_pool_state.IpamPoolState"]
    """<p>The state of the IPAM pool.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The state message.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the IPAM pool.</p>"""
    auto_import: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. </p> <p>A locale must be set on the pool for this feature to work.</p>"""
    publicly_advertisable: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Determines if a pool is publicly advertisable. This option is not available for pools with AddressFamily set to <code>ipv4</code>.</p>"""
    address_family: NotRequired["capo_ec2.types.address_family.AddressFamily"]
    """<p>The address family of the pool.</p>"""
    allocation_min_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    allocation_max_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    allocation_default_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.</p>"""
    allocation_resource_tags: NotRequired[
        "capo_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    aws_service: NotRequired["capo_ec2.types.ipam_pool_aws_service.IpamPoolAwsService"]
    """<p>Limits which service in Amazon Web Services that the pool can be used in. "ec2", for example, allows users to use space for Elastic IP addresses and VPCs.</p>"""
    public_ip_source: NotRequired[
        "capo_ec2.types.ipam_pool_public_ip_source.IpamPoolPublicIpSource"
    ]
    """<p>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is <code>BYOIP</code>. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html">Create IPv6 pools</a> in the <i>Amazon VPC IPAM User Guide</i>. By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool. For information on increasing the default limit, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    source_resource: NotRequired[
        "capo_ec2.types.ipam_pool_source_resource.IpamPoolSourceResource"
    ]
    """<p>The resource used to provision CIDRs to a resource planning pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "source_ipam_pool_id" in value:
        pairs.append(
            (f"{key_prefix}SourceIpamPoolId", str(value["source_ipam_pool_id"]))
        )
    if "ipam_pool_arn" in value:
        pairs.append((f"{key_prefix}IpamPoolArn", str(value["ipam_pool_arn"])))
    if "ipam_scope_arn" in value:
        pairs.append((f"{key_prefix}IpamScopeArn", str(value["ipam_scope_arn"])))
    if "ipam_scope_type" in value:
        import capo_ec2.types.ipam_scope_type

        capo_ec2.types.ipam_scope_type.serialize_ec2_query(
            value["ipam_scope_type"], pairs, f"{key_prefix}IpamScopeType"
        )
    if "ipam_arn" in value:
        pairs.append((f"{key_prefix}IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{key_prefix}IpamRegion", str(value["ipam_region"])))
    if "locale" in value:
        pairs.append((f"{key_prefix}Locale", str(value["locale"])))
    if "pool_depth" in value:
        pairs.append((f"{key_prefix}PoolDepth", str(value["pool_depth"])))
    if "state" in value:
        import capo_ec2.types.ipam_pool_state

        capo_ec2.types.ipam_pool_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "auto_import" in value:
        pairs.append(
            (f"{key_prefix}AutoImport", "true" if value["auto_import"] else "false")
        )
    if "publicly_advertisable" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAdvertisable",
                "true" if value["publicly_advertisable"] else "false",
            )
        )
    if "address_family" in value:
        import capo_ec2.types.address_family

        capo_ec2.types.address_family.serialize_ec2_query(
            value["address_family"], pairs, f"{key_prefix}AddressFamily"
        )
    if "allocation_min_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationMinNetmaskLength",
                str(value["allocation_min_netmask_length"]),
            )
        )
    if "allocation_max_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationMaxNetmaskLength",
                str(value["allocation_max_netmask_length"]),
            )
        )
    if "allocation_default_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationDefaultNetmaskLength",
                str(value["allocation_default_netmask_length"]),
            )
        )
    if "allocation_resource_tags" in value:
        import capo_ec2.types.ipam_resource_tag_list

        capo_ec2.types.ipam_resource_tag_list.serialize_ec2_query(
            value["allocation_resource_tags"],
            pairs,
            f"{key_prefix}AllocationResourceTagSet",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "aws_service" in value:
        import capo_ec2.types.ipam_pool_aws_service

        capo_ec2.types.ipam_pool_aws_service.serialize_ec2_query(
            value["aws_service"], pairs, f"{key_prefix}AwsService"
        )
    if "public_ip_source" in value:
        import capo_ec2.types.ipam_pool_public_ip_source

        capo_ec2.types.ipam_pool_public_ip_source.serialize_ec2_query(
            value["public_ip_source"], pairs, f"{key_prefix}PublicIpSource"
        )
    if "source_resource" in value:
        import capo_ec2.types.ipam_pool_source_resource

        capo_ec2.types.ipam_pool_source_resource.serialize_ec2_query(
            value["source_resource"], pairs, f"{key_prefix}SourceResource"
        )


def deserialize_ec2_query(el: Element) -> IpamPool:
    out: IpamPool = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_pool_id = el.find("ipamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_source_ipam_pool_id = el.find("sourceIpamPoolId")
    if child_source_ipam_pool_id is not None:
        out["source_ipam_pool_id"] = str(child_source_ipam_pool_id.text or "")
    child_ipam_pool_arn = el.find("ipamPoolArn")
    if child_ipam_pool_arn is not None:
        out["ipam_pool_arn"] = str(child_ipam_pool_arn.text or "")
    child_ipam_scope_arn = el.find("ipamScopeArn")
    if child_ipam_scope_arn is not None:
        out["ipam_scope_arn"] = str(child_ipam_scope_arn.text or "")
    child_ipam_scope_type = el.find("ipamScopeType")
    if child_ipam_scope_type is not None:
        import capo_ec2.types.ipam_scope_type

        out["ipam_scope_type"] = capo_ec2.types.ipam_scope_type.deserialize_ec2_query(
            child_ipam_scope_type
        )
    child_ipam_arn = el.find("ipamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("ipamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_locale = el.find("locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_pool_depth = el.find("poolDepth")
    if child_pool_depth is not None:
        out["pool_depth"] = int(child_pool_depth.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_pool_state

        out["state"] = capo_ec2.types.ipam_pool_state.deserialize_ec2_query(child_state)
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_auto_import = el.find("autoImport")
    if child_auto_import is not None:
        out["auto_import"] = (child_auto_import.text or "").lower() == "true"
    child_publicly_advertisable = el.find("publiclyAdvertisable")
    if child_publicly_advertisable is not None:
        out["publicly_advertisable"] = (
            child_publicly_advertisable.text or ""
        ).lower() == "true"
    child_address_family = el.find("addressFamily")
    if child_address_family is not None:
        import capo_ec2.types.address_family

        out["address_family"] = capo_ec2.types.address_family.deserialize_ec2_query(
            child_address_family
        )
    child_allocation_min_netmask_length = el.find("allocationMinNetmaskLength")
    if child_allocation_min_netmask_length is not None:
        out["allocation_min_netmask_length"] = int(
            child_allocation_min_netmask_length.text or ""
        )
    child_allocation_max_netmask_length = el.find("allocationMaxNetmaskLength")
    if child_allocation_max_netmask_length is not None:
        out["allocation_max_netmask_length"] = int(
            child_allocation_max_netmask_length.text or ""
        )
    child_allocation_default_netmask_length = el.find("allocationDefaultNetmaskLength")
    if child_allocation_default_netmask_length is not None:
        out["allocation_default_netmask_length"] = int(
            child_allocation_default_netmask_length.text or ""
        )
    child_allocation_resource_tags = el.find("allocationResourceTagSet")
    if child_allocation_resource_tags is not None:
        import capo_ec2.types.ipam_resource_tag_list

        out["allocation_resource_tags"] = (
            capo_ec2.types.ipam_resource_tag_list.deserialize_ec2_query(
                child_allocation_resource_tags
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_aws_service = el.find("awsService")
    if child_aws_service is not None:
        import capo_ec2.types.ipam_pool_aws_service

        out["aws_service"] = capo_ec2.types.ipam_pool_aws_service.deserialize_ec2_query(
            child_aws_service
        )
    child_public_ip_source = el.find("publicIpSource")
    if child_public_ip_source is not None:
        import capo_ec2.types.ipam_pool_public_ip_source

        out["public_ip_source"] = (
            capo_ec2.types.ipam_pool_public_ip_source.deserialize_ec2_query(
                child_public_ip_source
            )
        )
    child_source_resource = el.find("sourceResource")
    if child_source_resource is not None:
        import capo_ec2.types.ipam_pool_source_resource

        out["source_resource"] = (
            capo_ec2.types.ipam_pool_source_resource.deserialize_ec2_query(
                child_source_resource
            )
        )
    return out
