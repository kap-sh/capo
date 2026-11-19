"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CapacityUsageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.cidr_summary


class CapacityUsageSummary(TypedDict, closed=True):
    cid_rs: NotRequired["capo_network_firewall.types.cidr_summary.CIDRSummary"]
    """<p>Describes the capacity usage of the CIDR blocks used by the IP set references in a firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityUsageSummary) -> dict:
    out: dict = {}
    if "cid_rs" in value:
        import capo_network_firewall.types.cidr_summary

        out["CIDRs"] = capo_network_firewall.types.cidr_summary.serialize_aws_json_1_0(
            value["cid_rs"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityUsageSummary:
    out: CapacityUsageSummary = {}  # type: ignore[typeddict-item]
    if data.get("CIDRs") is not None:
        import capo_network_firewall.types.cidr_summary

        out["cid_rs"] = (
            capo_network_firewall.types.cidr_summary.deserialize_aws_json_1_0(
                data["CIDRs"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CapacityUsageSummary) -> dict:
    out: dict = {}
    if "cid_rs" in value:
        import capo_network_firewall.types.cidr_summary

        out["CIDRs"] = capo_network_firewall.types.cidr_summary.serialize_cbor(
            value["cid_rs"]
        )
    return out


def deserialize_cbor(data: dict) -> CapacityUsageSummary:
    out: CapacityUsageSummary = {}  # type: ignore[typeddict-item]
    if data.get("CIDRs") is not None:
        import capo_network_firewall.types.cidr_summary

        out["cid_rs"] = capo_network_firewall.types.cidr_summary.deserialize_cbor(
            data["CIDRs"]
        )
    return out
