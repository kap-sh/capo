"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CIDRSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.cidr_count
    import capo_network_firewall.types.ip_set_metadata_map


class CIDRSummary(TypedDict, closed=True):
    available_cidr_count: NotRequired[
        "capo_network_firewall.types.cidr_count.CIDRCount"
    ]
    """<p>The number of CIDR blocks available for use by the IP set references in a firewall.</p>"""
    utilized_cidr_count: NotRequired["capo_network_firewall.types.cidr_count.CIDRCount"]
    """<p>The number of CIDR blocks used by the IP set references in a firewall.</p>"""
    ip_set_references: NotRequired[
        "capo_network_firewall.types.ip_set_metadata_map.IPSetMetadataMap"
    ]
    """<p>The list of the IP set references used by a firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CIDRSummary) -> dict:
    out: dict = {}
    if "available_cidr_count" in value:
        out["AvailableCIDRCount"] = value["available_cidr_count"]
    if "utilized_cidr_count" in value:
        out["UtilizedCIDRCount"] = value["utilized_cidr_count"]
    if "ip_set_references" in value:
        import capo_network_firewall.types.ip_set_metadata_map

        out["IPSetReferences"] = (
            capo_network_firewall.types.ip_set_metadata_map.serialize_aws_json_1_0(
                value["ip_set_references"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CIDRSummary:
    out: CIDRSummary = {}  # type: ignore[typeddict-item]
    if data.get("AvailableCIDRCount") is not None:
        out["available_cidr_count"] = data["AvailableCIDRCount"]
    if data.get("UtilizedCIDRCount") is not None:
        out["utilized_cidr_count"] = data["UtilizedCIDRCount"]
    if data.get("IPSetReferences") is not None:
        import capo_network_firewall.types.ip_set_metadata_map

        out["ip_set_references"] = (
            capo_network_firewall.types.ip_set_metadata_map.deserialize_aws_json_1_0(
                data["IPSetReferences"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CIDRSummary) -> dict:
    out: dict = {}
    if "available_cidr_count" in value:
        out["AvailableCIDRCount"] = value["available_cidr_count"]
    if "utilized_cidr_count" in value:
        out["UtilizedCIDRCount"] = value["utilized_cidr_count"]
    if "ip_set_references" in value:
        import capo_network_firewall.types.ip_set_metadata_map

        out["IPSetReferences"] = (
            capo_network_firewall.types.ip_set_metadata_map.serialize_cbor(
                value["ip_set_references"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CIDRSummary:
    out: CIDRSummary = {}  # type: ignore[typeddict-item]
    if data.get("AvailableCIDRCount") is not None:
        out["available_cidr_count"] = data["AvailableCIDRCount"]
    if data.get("UtilizedCIDRCount") is not None:
        out["utilized_cidr_count"] = data["UtilizedCIDRCount"]
    if data.get("IPSetReferences") is not None:
        import capo_network_firewall.types.ip_set_metadata_map

        out["ip_set_references"] = (
            capo_network_firewall.types.ip_set_metadata_map.deserialize_cbor(
                data["IPSetReferences"]
            )
        )
    return out
