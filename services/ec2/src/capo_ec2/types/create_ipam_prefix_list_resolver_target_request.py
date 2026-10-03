"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_long
    import capo_ec2.types.ipam_prefix_list_resolver_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateIpamPrefixListResolverTargetRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver that will manage the synchronization of CIDRs to the target prefix list.</p>"""
    prefix_list_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the managed prefix list that will be synchronized with CIDRs selected by the IPAM prefix list resolver. This prefix list becomes an IPAM managed prefix list.</p> <p>An IPAM-managed prefix list is a customer-managed prefix list that has been associated with an IPAM prefix list resolver target. When a prefix list becomes IPAM managed, its CIDRs are automatically synchronized based on the IPAM prefix list resolver's CIDR selection rules, and direct CIDR modifications are restricted.</p>"""
    prefix_list_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the prefix list is located. This is required when referencing a prefix list in a different Region.</p>"""
    desired_version: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The specific version of the prefix list to target. If not specified, the resolver will target the latest version.</p>"""
    track_latest_version: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, the target will always synchronize with the most current version of the prefix list.</p> <p>Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the IPAM prefix list resolver target during creation. Tags help you organize and manage your Amazon Web Services resources.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamPrefixListResolverTargetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_prefix_list_resolver_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverId",
                str(value["ipam_prefix_list_resolver_id"]),
            )
        )
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "prefix_list_region" in value:
        pairs.append(
            (f"{key_prefix}PrefixListRegion", str(value["prefix_list_region"]))
        )
    if "desired_version" in value:
        pairs.append((f"{key_prefix}DesiredVersion", str(value["desired_version"])))
    if "track_latest_version" in value:
        pairs.append(
            (
                f"{key_prefix}TrackLatestVersion",
                "true" if value["track_latest_version"] else "false",
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateIpamPrefixListResolverTargetRequest:
    out: CreateIpamPrefixListResolverTargetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_prefix_list_resolver_id = el.find("IpamPrefixListResolverId")
    if child_ipam_prefix_list_resolver_id is not None:
        out["ipam_prefix_list_resolver_id"] = str(
            child_ipam_prefix_list_resolver_id.text or ""
        )
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_prefix_list_region = el.find("PrefixListRegion")
    if child_prefix_list_region is not None:
        out["prefix_list_region"] = str(child_prefix_list_region.text or "")
    child_desired_version = el.find("DesiredVersion")
    if child_desired_version is not None:
        out["desired_version"] = int(child_desired_version.text or "")
    child_track_latest_version = el.find("TrackLatestVersion")
    if child_track_latest_version is not None:
        out["track_latest_version"] = (
            child_track_latest_version.text or ""
        ).lower() == "true"
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
    return out
