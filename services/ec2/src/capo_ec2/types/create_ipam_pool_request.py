"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_family
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_netmask_length
    import capo_ec2.types.ipam_pool_aws_service
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipam_pool_public_ip_source
    import capo_ec2.types.ipam_pool_source_resource_request
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.request_ipam_resource_tag_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateIpamPoolRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope in which you would like to create the IPAM pool.</p>"""
    locale: NotRequired["capo_ec2.types.string.String"]
    """<p>The locale for the pool should be one of the following:</p> <ul> <li> <p>An Amazon Web Services Region where you want this IPAM pool to be available for allocations.</p> </li> <li> <p>The network border group for an Amazon Web Services Local Zone where you want this IPAM pool to be available for allocations (<a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail">supported Local Zones</a>). This option is only available for IPAM IPv4 pools in the public scope.</p> </li> </ul> <p>Possible values: Any Amazon Web Services Region or supported Amazon Web Services Local Zone. Default is <code>none</code> and means any locale.</p>"""
    source_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the source IPAM pool. Use this option to create a pool within an existing pool. Note that the CIDR you provision for the pool within the source pool must be available in the source pool's CIDR range.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the IPAM pool.</p>"""
    address_family: NotRequired["capo_ec2.types.address_family.AddressFamily"]
    """<p>The IP protocol assigned to this IPAM pool. You must choose either IPv4 or IPv6 protocol for a pool.</p>"""
    auto_import: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. </p> <p>A locale must be set on the pool for this feature to work.</p>"""
    publicly_advertisable: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Determines if the pool is publicly advertisable. The request can only contain <code>PubliclyAdvertisable</code> if <code>AddressFamily</code> is <code>ipv6</code> and <code>PublicIpSource</code> is <code>byoip</code>.</p>"""
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
        "capo_ec2.types.request_ipam_resource_tag_list.RequestIpamResourceTagList"
    ]
    """<p>Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    aws_service: NotRequired["capo_ec2.types.ipam_pool_aws_service.IpamPoolAwsService"]
    """<p>Limits which service in Amazon Web Services that the pool can be used in. "ec2", for example, allows users to use space for Elastic IP addresses and VPCs.</p>"""
    public_ip_source: NotRequired[
        "capo_ec2.types.ipam_pool_public_ip_source.IpamPoolPublicIpSource"
    ]
    """<p>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is <code>byoip</code>. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html">Create IPv6 pools</a> in the <i>Amazon VPC IPAM User Guide</i>. By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool if PublicIpSource is <code>amazon</code>. For information on increasing the default limit, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html"> Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    source_resource: NotRequired[
        "capo_ec2.types.ipam_pool_source_resource_request.IpamPoolSourceResourceRequest"
    ]
    """<p>The resource used to provision CIDRs to a resource planning pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamPoolRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_scope_id" in value:
        pairs.append((f"{key_prefix}IpamScopeId", str(value["ipam_scope_id"])))
    if "locale" in value:
        pairs.append((f"{key_prefix}Locale", str(value["locale"])))
    if "source_ipam_pool_id" in value:
        pairs.append(
            (f"{key_prefix}SourceIpamPoolId", str(value["source_ipam_pool_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "address_family" in value:
        import capo_ec2.types.address_family

        capo_ec2.types.address_family.serialize_ec2_query(
            value["address_family"], pairs, f"{key_prefix}AddressFamily"
        )
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
        import capo_ec2.types.request_ipam_resource_tag_list

        capo_ec2.types.request_ipam_resource_tag_list.serialize_ec2_query(
            value["allocation_resource_tags"],
            pairs,
            f"{key_prefix}AllocationResourceTag",
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
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
        import capo_ec2.types.ipam_pool_source_resource_request

        capo_ec2.types.ipam_pool_source_resource_request.serialize_ec2_query(
            value["source_resource"], pairs, f"{key_prefix}SourceResource"
        )


def deserialize_ec2_query(el: Element) -> CreateIpamPoolRequest:
    out: CreateIpamPoolRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_source_ipam_pool_id = el.find("SourceIpamPoolId")
    if child_source_ipam_pool_id is not None:
        out["source_ipam_pool_id"] = str(child_source_ipam_pool_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_address_family = el.find("AddressFamily")
    if child_address_family is not None:
        import capo_ec2.types.address_family

        out["address_family"] = capo_ec2.types.address_family.deserialize_ec2_query(
            child_address_family
        )
    child_auto_import = el.find("AutoImport")
    if child_auto_import is not None:
        out["auto_import"] = (child_auto_import.text or "").lower() == "true"
    child_publicly_advertisable = el.find("PubliclyAdvertisable")
    if child_publicly_advertisable is not None:
        out["publicly_advertisable"] = (
            child_publicly_advertisable.text or ""
        ).lower() == "true"
    child_allocation_min_netmask_length = el.find("AllocationMinNetmaskLength")
    if child_allocation_min_netmask_length is not None:
        out["allocation_min_netmask_length"] = int(
            child_allocation_min_netmask_length.text or ""
        )
    child_allocation_max_netmask_length = el.find("AllocationMaxNetmaskLength")
    if child_allocation_max_netmask_length is not None:
        out["allocation_max_netmask_length"] = int(
            child_allocation_max_netmask_length.text or ""
        )
    child_allocation_default_netmask_length = el.find("AllocationDefaultNetmaskLength")
    if child_allocation_default_netmask_length is not None:
        out["allocation_default_netmask_length"] = int(
            child_allocation_default_netmask_length.text or ""
        )
    child_allocation_resource_tags = el.find("AllocationResourceTag")
    if child_allocation_resource_tags is not None:
        import capo_ec2.types.request_ipam_resource_tag_list

        out["allocation_resource_tags"] = (
            capo_ec2.types.request_ipam_resource_tag_list.deserialize_ec2_query(
                child_allocation_resource_tags
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_aws_service = el.find("AwsService")
    if child_aws_service is not None:
        import capo_ec2.types.ipam_pool_aws_service

        out["aws_service"] = capo_ec2.types.ipam_pool_aws_service.deserialize_ec2_query(
            child_aws_service
        )
    child_public_ip_source = el.find("PublicIpSource")
    if child_public_ip_source is not None:
        import capo_ec2.types.ipam_pool_public_ip_source

        out["public_ip_source"] = (
            capo_ec2.types.ipam_pool_public_ip_source.deserialize_ec2_query(
                child_public_ip_source
            )
        )
    child_source_resource = el.find("SourceResource")
    if child_source_resource is not None:
        import capo_ec2.types.ipam_pool_source_resource_request

        out["source_resource"] = (
            capo_ec2.types.ipam_pool_source_resource_request.deserialize_ec2_query(
                child_source_resource
            )
        )
    return out
