"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AvailabilityZoneMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.ip_address_type


class AvailabilityZoneMetadata(TypedDict, closed=True):
    ip_address_type: NotRequired[
        "capo_network_firewall.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type of the Firewall subnet in the Availability Zone. You can't change the IP address type after you create the subnet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AvailabilityZoneMetadata) -> dict:
    out: dict = {}
    if "ip_address_type" in value:
        import capo_network_firewall.types.ip_address_type

        out["IPAddressType"] = (
            capo_network_firewall.types.ip_address_type.serialize_aws_json_1_0(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AvailabilityZoneMetadata:
    out: AvailabilityZoneMetadata = {}  # type: ignore[typeddict-item]
    if data.get("IPAddressType") is not None:
        import capo_network_firewall.types.ip_address_type

        out["ip_address_type"] = (
            capo_network_firewall.types.ip_address_type.deserialize_aws_json_1_0(
                data["IPAddressType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AvailabilityZoneMetadata) -> dict:
    out: dict = {}
    if "ip_address_type" in value:
        import capo_network_firewall.types.ip_address_type

        out["IPAddressType"] = (
            capo_network_firewall.types.ip_address_type.serialize_cbor(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AvailabilityZoneMetadata:
    out: AvailabilityZoneMetadata = {}  # type: ignore[typeddict-item]
    if data.get("IPAddressType") is not None:
        import capo_network_firewall.types.ip_address_type

        out["ip_address_type"] = (
            capo_network_firewall.types.ip_address_type.deserialize_cbor(
                data["IPAddressType"]
            )
        )
    return out
