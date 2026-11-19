"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ReferenceSets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.ip_set_reference_map


class ReferenceSets(TypedDict, closed=True):
    ip_set_references: NotRequired[
        "capo_network_firewall.types.ip_set_reference_map.IPSetReferenceMap"
    ]
    """<p>The list of IP set references.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReferenceSets) -> dict:
    out: dict = {}
    if "ip_set_references" in value:
        import capo_network_firewall.types.ip_set_reference_map

        out["IPSetReferences"] = (
            capo_network_firewall.types.ip_set_reference_map.serialize_aws_json_1_0(
                value["ip_set_references"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReferenceSets:
    out: ReferenceSets = {}  # type: ignore[typeddict-item]
    if data.get("IPSetReferences") is not None:
        import capo_network_firewall.types.ip_set_reference_map

        out["ip_set_references"] = (
            capo_network_firewall.types.ip_set_reference_map.deserialize_aws_json_1_0(
                data["IPSetReferences"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReferenceSets) -> dict:
    out: dict = {}
    if "ip_set_references" in value:
        import capo_network_firewall.types.ip_set_reference_map

        out["IPSetReferences"] = (
            capo_network_firewall.types.ip_set_reference_map.serialize_cbor(
                value["ip_set_references"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ReferenceSets:
    out: ReferenceSets = {}  # type: ignore[typeddict-item]
    if data.get("IPSetReferences") is not None:
        import capo_network_firewall.types.ip_set_reference_map

        out["ip_set_references"] = (
            capo_network_firewall.types.ip_set_reference_map.deserialize_cbor(
                data["IPSetReferences"]
            )
        )
    return out
