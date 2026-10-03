"""Generated from Smithy shape ``com.amazonaws.ec2#Ipam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_metered_account
    import capo_ec2.types.ipam_operating_region_set
    import capo_ec2.types.ipam_resource_discovery_association_id
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.ipam_state
    import capo_ec2.types.ipam_tier
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class Ipam(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM.</p>"""
    ipam_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM.</p>"""
    ipam_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM.</p>"""
    public_default_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM's default public scope.</p>"""
    private_default_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM's default private scope.</p>"""
    scope_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of scopes in the IPAM. The scope quota is 5. For more information on quotas, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html">Quotas in IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the IPAM.</p>"""
    operating_regions: NotRequired[
        "capo_ec2.types.ipam_operating_region_set.IpamOperatingRegionSet"
    ]
    """<p>The operating Regions for an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p> <p>For more information about operating Regions, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html">Create an IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    state: NotRequired["capo_ec2.types.ipam_state.IpamState"]
    """<p>The state of the IPAM.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    default_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The IPAM's default resource discovery ID.</p>"""
    default_resource_discovery_association_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_association_id.IpamResourceDiscoveryAssociationId"
    ]
    """<p>The IPAM's default resource discovery association ID.</p>"""
    resource_discovery_association_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The IPAM's resource discovery association count.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The state message.</p>"""
    tier: NotRequired["capo_ec2.types.ipam_tier.IpamTier"]
    """<p>IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing > IPAM tab</a>.</p>"""
    enable_private_gua: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.</p>"""
    metered_account: NotRequired[
        "capo_ec2.types.ipam_metered_account.IpamMeteredAccount"
    ]
    """<p>A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html">Enable cost distribution</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <p>Possible values:</p> <ul> <li> <p> <code>ipam-owner</code> (default): The Amazon Web Services account which owns the IPAM is charged for all active IP addresses managed in IPAM.</p> </li> <li> <p> <code>resource-owner</code>: The Amazon Web Services account that owns the IP address is charged for the active IP address.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(value: Ipam, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "ipam_arn" in value:
        pairs.append((f"{key_prefix}IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{key_prefix}IpamRegion", str(value["ipam_region"])))
    if "public_default_scope_id" in value:
        pairs.append(
            (f"{key_prefix}PublicDefaultScopeId", str(value["public_default_scope_id"]))
        )
    if "private_default_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}PrivateDefaultScopeId",
                str(value["private_default_scope_id"]),
            )
        )
    if "scope_count" in value:
        pairs.append((f"{key_prefix}ScopeCount", str(value["scope_count"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "operating_regions" in value:
        import capo_ec2.types.ipam_operating_region_set

        capo_ec2.types.ipam_operating_region_set.serialize_ec2_query(
            value["operating_regions"], pairs, f"{key_prefix}OperatingRegionSet"
        )
    if "state" in value:
        import capo_ec2.types.ipam_state

        capo_ec2.types.ipam_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "default_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultResourceDiscoveryId",
                str(value["default_resource_discovery_id"]),
            )
        )
    if "default_resource_discovery_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultResourceDiscoveryAssociationId",
                str(value["default_resource_discovery_association_id"]),
            )
        )
    if "resource_discovery_association_count" in value:
        pairs.append(
            (
                f"{key_prefix}ResourceDiscoveryAssociationCount",
                str(value["resource_discovery_association_count"]),
            )
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "tier" in value:
        import capo_ec2.types.ipam_tier

        capo_ec2.types.ipam_tier.serialize_ec2_query(
            value["tier"], pairs, f"{key_prefix}Tier"
        )
    if "enable_private_gua" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePrivateGua",
                "true" if value["enable_private_gua"] else "false",
            )
        )
    if "metered_account" in value:
        import capo_ec2.types.ipam_metered_account

        capo_ec2.types.ipam_metered_account.serialize_ec2_query(
            value["metered_account"], pairs, f"{key_prefix}MeteredAccount"
        )


def deserialize_ec2_query(el: Element) -> Ipam:
    out: Ipam = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_id = el.find("ipamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_arn = el.find("ipamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("ipamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_public_default_scope_id = el.find("publicDefaultScopeId")
    if child_public_default_scope_id is not None:
        out["public_default_scope_id"] = str(child_public_default_scope_id.text or "")
    child_private_default_scope_id = el.find("privateDefaultScopeId")
    if child_private_default_scope_id is not None:
        out["private_default_scope_id"] = str(child_private_default_scope_id.text or "")
    child_scope_count = el.find("scopeCount")
    if child_scope_count is not None:
        out["scope_count"] = int(child_scope_count.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_operating_regions = el.find("operatingRegionSet")
    if child_operating_regions is not None:
        import capo_ec2.types.ipam_operating_region_set

        out["operating_regions"] = (
            capo_ec2.types.ipam_operating_region_set.deserialize_ec2_query(
                child_operating_regions
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_state

        out["state"] = capo_ec2.types.ipam_state.deserialize_ec2_query(child_state)
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_default_resource_discovery_id = el.find("defaultResourceDiscoveryId")
    if child_default_resource_discovery_id is not None:
        out["default_resource_discovery_id"] = str(
            child_default_resource_discovery_id.text or ""
        )
    child_default_resource_discovery_association_id = el.find(
        "defaultResourceDiscoveryAssociationId"
    )
    if child_default_resource_discovery_association_id is not None:
        out["default_resource_discovery_association_id"] = str(
            child_default_resource_discovery_association_id.text or ""
        )
    child_resource_discovery_association_count = el.find(
        "resourceDiscoveryAssociationCount"
    )
    if child_resource_discovery_association_count is not None:
        out["resource_discovery_association_count"] = int(
            child_resource_discovery_association_count.text or ""
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_tier = el.find("tier")
    if child_tier is not None:
        import capo_ec2.types.ipam_tier

        out["tier"] = capo_ec2.types.ipam_tier.deserialize_ec2_query(child_tier)
    child_enable_private_gua = el.find("enablePrivateGua")
    if child_enable_private_gua is not None:
        out["enable_private_gua"] = (
            child_enable_private_gua.text or ""
        ).lower() == "true"
    child_metered_account = el.find("meteredAccount")
    if child_metered_account is not None:
        import capo_ec2.types.ipam_metered_account

        out["metered_account"] = (
            capo_ec2.types.ipam_metered_account.deserialize_ec2_query(
                child_metered_account
            )
        )
    return out
