"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.cidr_count


class IPSetMetadata(TypedDict, closed=True):
    resolved_cidr_count: NotRequired["capo_network_firewall.types.cidr_count.CIDRCount"]
    """<p>Describes the total number of CIDR blocks currently in use by the IP set references in a firewall. To determine how many CIDR blocks are available for you to use in a firewall, you can call <code>AvailableCIDRCount</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPSetMetadata) -> dict:
    out: dict = {}
    if "resolved_cidr_count" in value:
        out["ResolvedCIDRCount"] = value["resolved_cidr_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSetMetadata:
    out: IPSetMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ResolvedCIDRCount") is not None:
        out["resolved_cidr_count"] = data["ResolvedCIDRCount"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IPSetMetadata) -> dict:
    out: dict = {}
    if "resolved_cidr_count" in value:
        out["ResolvedCIDRCount"] = value["resolved_cidr_count"]
    return out


def deserialize_cbor(data: dict) -> IPSetMetadata:
    out: IPSetMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ResolvedCIDRCount") is not None:
        out["resolved_cidr_count"] = data["ResolvedCIDRCount"]
    return out
