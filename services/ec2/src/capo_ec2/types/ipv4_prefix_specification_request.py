"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Ipv4PrefixSpecificationRequest(TypedDict, closed=True):
    ipv4_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 prefix. For information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html"> Assigning prefixes to network interfaces</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv4PrefixSpecificationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv4_prefix" in value:
        pairs.append((f"{key_prefix}Ipv4Prefix", str(value["ipv4_prefix"])))


def deserialize_ec2_query(el: Element) -> Ipv4PrefixSpecificationRequest:
    out: Ipv4PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_ipv4_prefix = el.find("Ipv4Prefix")
    if child_ipv4_prefix is not None:
        out["ipv4_prefix"] = str(child_ipv4_prefix.text or "")
    return out
