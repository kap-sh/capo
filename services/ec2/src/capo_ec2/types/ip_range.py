"""Generated from Smithy shape ``com.amazonaws.ec2#IpRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class IpRange(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the security group rule that references this IPv4 address range.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*</p>"""
    cidr_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.</p> <note> <p> Amazon Web Services <a href="https://en.wikipedia.org/wiki/Canonicalization">canonicalizes</a> IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "cidr_ip" in value:
        pairs.append((f"{key_prefix}CidrIp", str(value["cidr_ip"])))


def deserialize_ec2_query(el: Element) -> IpRange:
    out: IpRange = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_cidr_ip = el.find("cidrIp")
    if child_cidr_ip is not None:
        out["cidr_ip"] = str(child_cidr_ip.text or "")
    return out
