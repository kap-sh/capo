"""Generated from Smithy shape ``com.amazonaws.memorydb#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.availability_zone
    import capo_memorydb.types.network_type_list
    import capo_memorydb.types.string


class Subnet(TypedDict, closed=True):
    identifier: NotRequired["capo_memorydb.types.string.String"]
    """<p>The unique identifier for the subnet.</p>"""
    availability_zone: NotRequired[
        "capo_memorydb.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone where the subnet resides</p>"""
    supported_network_types: NotRequired[
        "capo_memorydb.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network types supported by this subnet. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating whether the subnet supports IPv4 only, IPv6 only, or dual-stack deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnet) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "availability_zone" in value:
        import capo_memorydb.types.availability_zone

        out["AvailabilityZone"] = (
            capo_memorydb.types.availability_zone.serialize_aws_json_1_1(
                value["availability_zone"]
            )
        )
    if "supported_network_types" in value:
        import capo_memorydb.types.network_type_list

        out["SupportedNetworkTypes"] = (
            capo_memorydb.types.network_type_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("AvailabilityZone") is not None:
        import capo_memorydb.types.availability_zone

        out["availability_zone"] = (
            capo_memorydb.types.availability_zone.deserialize_aws_json_1_1(
                data["AvailabilityZone"]
            )
        )
    if data.get("SupportedNetworkTypes") is not None:
        import capo_memorydb.types.network_type_list

        out["supported_network_types"] = (
            capo_memorydb.types.network_type_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Subnet) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "availability_zone" in value:
        import capo_memorydb.types.availability_zone

        out["AvailabilityZone"] = capo_memorydb.types.availability_zone.serialize_cbor(
            value["availability_zone"]
        )
    if "supported_network_types" in value:
        import capo_memorydb.types.network_type_list

        out["SupportedNetworkTypes"] = (
            capo_memorydb.types.network_type_list.serialize_cbor(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("AvailabilityZone") is not None:
        import capo_memorydb.types.availability_zone

        out["availability_zone"] = (
            capo_memorydb.types.availability_zone.deserialize_cbor(
                data["AvailabilityZone"]
            )
        )
    if data.get("SupportedNetworkTypes") is not None:
        import capo_memorydb.types.network_type_list

        out["supported_network_types"] = (
            capo_memorydb.types.network_type_list.deserialize_cbor(
                data["SupportedNetworkTypes"]
            )
        )
    return out
