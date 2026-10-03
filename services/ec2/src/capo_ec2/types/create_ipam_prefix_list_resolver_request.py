"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_family
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_prefix_list_resolver_rule_request_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateIpamPrefixListResolverRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that will serve as the source of the IP address database for CIDR selection. The IPAM must be in the Advanced tier to use this feature.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the IPAM prefix list resolver to help you identify its purpose and configuration.</p>"""
    address_family: NotRequired["capo_ec2.types.address_family.AddressFamily"]
    """<p>The address family for the IPAM prefix list resolver. Valid values are <code>ipv4</code> and <code>ipv6</code>. You must create separate resolvers for IPv4 and IPv6 CIDRs as they cannot be mixed in the same resolver.</p>"""
    rules: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_rule_request_set.IpamPrefixListResolverRuleRequestSet"
    ]
    """<p>The CIDR selection rules for the resolver.</p> <p>CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the IPAM prefix list resolver during creation. Tags help you organize and manage your Amazon Web Services resources.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamPrefixListResolverRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "address_family" in value:
        import capo_ec2.types.address_family

        capo_ec2.types.address_family.serialize_ec2_query(
            value["address_family"], pairs, f"{key_prefix}AddressFamily"
        )
    if "rules" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_request_set

        capo_ec2.types.ipam_prefix_list_resolver_rule_request_set.serialize_ec2_query(
            value["rules"], pairs, f"{key_prefix}Rule"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateIpamPrefixListResolverRequest:
    out: CreateIpamPrefixListResolverRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_address_family = el.find("AddressFamily")
    if child_address_family is not None:
        import capo_ec2.types.address_family

        out["address_family"] = capo_ec2.types.address_family.deserialize_ec2_query(
            child_address_family
        )
    child_rules = el.find("Rule")
    if child_rules is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_request_set

        out["rules"] = (
            capo_ec2.types.ipam_prefix_list_resolver_rule_request_set.deserialize_ec2_query(
                child_rules
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
    return out
