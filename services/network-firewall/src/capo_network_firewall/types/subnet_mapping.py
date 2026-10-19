"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SubnetMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string
    import capo_network_firewall.types.ip_address_type


class SubnetMapping(TypedDict, closed=True):
    subnet_id: (
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    )
    """<p>The unique identifier for the subnet. </p>"""
    ip_address_type: NotRequired[
        "capo_network_firewall.types.ip_address_type.IPAddressType"
    ]
    """<p>The subnet's IP address type. You can't change the IP address type after you create the subnet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetMapping) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    if "ip_address_type" in value:
        import capo_network_firewall.types.ip_address_type

        out["IPAddressType"] = (
            capo_network_firewall.types.ip_address_type.serialize_aws_json_1_0(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SubnetMapping:
    out: SubnetMapping = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("IPAddressType") is not None:
        import capo_network_firewall.types.ip_address_type

        out["ip_address_type"] = (
            capo_network_firewall.types.ip_address_type.deserialize_aws_json_1_0(
                data["IPAddressType"]
            )
        )
    return out
