"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecondarySubnetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.boolean
    import capo_ec2.types.secondary_network_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateSecondarySubnetRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensure Idempotency</a>.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone for the secondary subnet. You cannot specify both <code>AvailabilityZone</code> and <code>AvailabilityZoneId</code> in the same request.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone for the secondary subnet. This option is preferred over <code>AvailabilityZone</code> as it provides a consistent identifier across Amazon Web Services accounts. You cannot specify both <code>AvailabilityZone</code> and <code>AvailabilityZoneId</code> in the same request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipv4_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block for the secondary subnet. The CIDR block size must be between /12 and /28.</p>"""
    secondary_network_id: NotRequired[
        "capo_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network in which to create the secondary subnet.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the secondary subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecondarySubnetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipv4_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv4CidrBlock", str(value["ipv4_cidr_block"])))
    if "secondary_network_id" in value:
        pairs.append(
            (f"{key_prefix}SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateSecondarySubnetRequest:
    out: CreateSecondarySubnetRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipv4_cidr_block = el.find("Ipv4CidrBlock")
    if child_ipv4_cidr_block is not None:
        out["ipv4_cidr_block"] = str(child_ipv4_cidr_block.text or "")
    child_secondary_network_id = el.find("SecondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
