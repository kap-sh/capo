"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecondaryNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.secondary_network_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateSecondaryNetworkRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensure Idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipv4_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block for the secondary network. The CIDR block size must be between /12 and /28.</p>"""
    network_type: NotRequired[
        "capo_ec2.types.secondary_network_type.SecondaryNetworkType"
    ]
    """<p>The type of secondary network.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the secondary network.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecondaryNetworkRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipv4_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv4CidrBlock", str(value["ipv4_cidr_block"])))
    if "network_type" in value:
        import capo_ec2.types.secondary_network_type

        capo_ec2.types.secondary_network_type.serialize_ec2_query(
            value["network_type"], pairs, f"{key_prefix}NetworkType"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateSecondaryNetworkRequest:
    out: CreateSecondaryNetworkRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipv4_cidr_block = el.find("Ipv4CidrBlock")
    if child_ipv4_cidr_block is not None:
        out["ipv4_cidr_block"] = str(child_ipv4_cidr_block.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        import capo_ec2.types.secondary_network_type

        out["network_type"] = (
            capo_ec2.types.secondary_network_type.deserialize_ec2_query(
                child_network_type
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
    return out
