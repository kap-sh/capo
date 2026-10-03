"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.add_ipam_operating_region_set
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_metered_account
    import capo_ec2.types.ipam_tier
    import capo_ec2.types.remove_ipam_operating_region_set
    import capo_ec2.types.string


class ModifyIpamRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM you want to modify.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the IPAM you want to modify.</p>"""
    add_operating_regions: NotRequired[
        "capo_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Choose the operating Regions for the IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p> <p>For more information about operating Regions, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html">Create an IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    remove_operating_regions: NotRequired[
        "capo_ec2.types.remove_ipam_operating_region_set.RemoveIpamOperatingRegionSet"
    ]
    """<p>The operating Regions to remove.</p>"""
    tier: NotRequired["capo_ec2.types.ipam_tier.IpamTier"]
    """<p>IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing > IPAM tab</a>.</p>"""
    enable_private_gua: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.</p>"""
    metered_account: NotRequired[
        "capo_ec2.types.ipam_metered_account.IpamMeteredAccount"
    ]
    """<p>A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html">Enable cost distribution</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <p>Possible values:</p> <ul> <li> <p> <code>ipam-owner</code> (default): The Amazon Web Services account which owns the IPAM is charged for all active IP addresses managed in IPAM.</p> </li> <li> <p> <code>resource-owner</code>: The Amazon Web Services account that owns the IP address is charged for the active IP address.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "add_operating_regions" in value:
        import capo_ec2.types.add_ipam_operating_region_set

        capo_ec2.types.add_ipam_operating_region_set.serialize_ec2_query(
            value["add_operating_regions"], pairs, f"{key_prefix}AddOperatingRegion"
        )
    if "remove_operating_regions" in value:
        import capo_ec2.types.remove_ipam_operating_region_set

        capo_ec2.types.remove_ipam_operating_region_set.serialize_ec2_query(
            value["remove_operating_regions"],
            pairs,
            f"{key_prefix}RemoveOperatingRegion",
        )
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


def deserialize_ec2_query(el: Element) -> ModifyIpamRequest:
    out: ModifyIpamRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_add_operating_regions = el.find("AddOperatingRegion")
    if child_add_operating_regions is not None:
        import capo_ec2.types.add_ipam_operating_region_set

        out["add_operating_regions"] = (
            capo_ec2.types.add_ipam_operating_region_set.deserialize_ec2_query(
                child_add_operating_regions
            )
        )
    child_remove_operating_regions = el.find("RemoveOperatingRegion")
    if child_remove_operating_regions is not None:
        import capo_ec2.types.remove_ipam_operating_region_set

        out["remove_operating_regions"] = (
            capo_ec2.types.remove_ipam_operating_region_set.deserialize_ec2_query(
                child_remove_operating_regions
            )
        )
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_ec2.types.ipam_tier

        out["tier"] = capo_ec2.types.ipam_tier.deserialize_ec2_query(child_tier)
    child_enable_private_gua = el.find("EnablePrivateGua")
    if child_enable_private_gua is not None:
        out["enable_private_gua"] = (
            child_enable_private_gua.text or ""
        ).lower() == "true"
    child_metered_account = el.find("MeteredAccount")
    if child_metered_account is not None:
        import capo_ec2.types.ipam_metered_account

        out["metered_account"] = (
            capo_ec2.types.ipam_metered_account.deserialize_ec2_query(
                child_metered_account
            )
        )
    return out
