"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Ipv6Range(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the security group rule that references this IPv6 address range.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*</p>"""
    cidr_ipv6: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.</p> <note> <p> Amazon Web Services <a href="https://en.wikipedia.org/wiki/Canonicalization">canonicalizes</a> IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6Range, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "cidr_ipv6" in value:
        pairs.append((f"{key_prefix}CidrIpv6", str(value["cidr_ipv6"])))


def deserialize_ec2_query(el: Element) -> Ipv6Range:
    out: Ipv6Range = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_cidr_ipv6 = el.find("cidrIpv6")
    if child_cidr_ipv6 is not None:
        out["cidr_ipv6"] = str(child_cidr_ipv6.text or "")
    return out
