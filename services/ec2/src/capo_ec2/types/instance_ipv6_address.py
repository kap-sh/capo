"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class InstanceIpv6Address(TypedDict, closed=True):
    ipv6_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 address.</p>"""
    is_primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6Address, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_address" in value:
        pairs.append((f"{key_prefix}Ipv6Address", str(value["ipv6_address"])))
    if "is_primary_ipv6" in value:
        pairs.append(
            (
                f"{key_prefix}IsPrimaryIpv6",
                "true" if value["is_primary_ipv6"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> InstanceIpv6Address:
    out: InstanceIpv6Address = {}  # type: ignore[typeddict-item]
    child_ipv6_address = el.find("ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    child_is_primary_ipv6 = el.find("isPrimaryIpv6")
    if child_is_primary_ipv6 is not None:
        out["is_primary_ipv6"] = (child_is_primary_ipv6.text or "").lower() == "true"
    return out
