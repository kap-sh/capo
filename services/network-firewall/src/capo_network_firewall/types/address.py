"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.address_definition


class Address(TypedDict, closed=True):
    address_definition: (
        "capo_network_firewall.types.address_definition.AddressDefinition"
    )
    """<p>Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. </p> <p>Examples: </p> <ul> <li> <p>To configure Network Firewall to inspect for the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Address) -> dict:
    out: dict = {}
    out["AddressDefinition"] = value["address_definition"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("AddressDefinition") is not None:
        out["address_definition"] = data["AddressDefinition"]
    else:
        raise DeserializationError("Address.address_definition required")
    return out
