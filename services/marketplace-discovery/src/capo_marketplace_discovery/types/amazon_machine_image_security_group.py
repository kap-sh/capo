"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list


class AmazonMachineImageSecurityGroup(TypedDict, closed=True):
    protocol: "str"
    """<p>The IP protocol name, such as <code>tcp</code>.</p>"""
    from_port: "int"
    """<p>The start of the port range.</p>"""
    to_port: "int"
    """<p>The end of the port range.</p>"""
    cidr_ip_addresses: "capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list.AmazonMachineImageCidrIpAddressList"
    """<p>The IP address ranges in CIDR format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageSecurityGroup) -> dict:
    out: dict = {}
    out["protocol"] = value["protocol"]
    out["fromPort"] = value["from_port"]
    out["toPort"] = value["to_port"]
    import capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list

    out["cidrIpAddresses"] = (
        capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list.serialize_json(
            value["cidr_ip_addresses"]
        )
    )
    return out


def deserialize_json(data: dict) -> AmazonMachineImageSecurityGroup:
    out: AmazonMachineImageSecurityGroup = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    else:
        out["protocol"] = ""
    if data.get("fromPort") is not None:
        out["from_port"] = data["fromPort"]
    else:
        out["from_port"] = 0
    if data.get("toPort") is not None:
        out["to_port"] = data["toPort"]
    else:
        out["to_port"] = 0
    if data.get("cidrIpAddresses") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list

        out["cidr_ip_addresses"] = (
            capo_marketplace_discovery.types.amazon_machine_image_cidr_ip_address_list.deserialize_json(
                data["cidrIpAddresses"]
            )
        )
    else:
        out["cidr_ip_addresses"] = []
    return out
