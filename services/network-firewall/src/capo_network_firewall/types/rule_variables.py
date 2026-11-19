"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleVariables``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.context_sets
    import capo_network_firewall.types.ip_sets
    import capo_network_firewall.types.port_sets


class RuleVariables(TypedDict, closed=True):
    ip_sets: NotRequired["capo_network_firewall.types.ip_sets.IPSets"]
    """<p>A list of IP addresses and address ranges, in CIDR notation. </p>"""
    port_sets: NotRequired["capo_network_firewall.types.port_sets.PortSets"]
    """<p>A list of port ranges. </p>"""
    context_sets: NotRequired["capo_network_firewall.types.context_sets.ContextSets"]
    """<p>A list of context sets. Each context set lists resources from the context store that is associated with the firewall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVariables) -> dict:
    out: dict = {}
    if "ip_sets" in value:
        import capo_network_firewall.types.ip_sets

        out["IPSets"] = capo_network_firewall.types.ip_sets.serialize_aws_json_1_0(
            value["ip_sets"]
        )
    if "port_sets" in value:
        import capo_network_firewall.types.port_sets

        out["PortSets"] = capo_network_firewall.types.port_sets.serialize_aws_json_1_0(
            value["port_sets"]
        )
    if "context_sets" in value:
        import capo_network_firewall.types.context_sets

        out["ContextSets"] = (
            capo_network_firewall.types.context_sets.serialize_aws_json_1_0(
                value["context_sets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleVariables:
    out: RuleVariables = {}  # type: ignore[typeddict-item]
    if data.get("IPSets") is not None:
        import capo_network_firewall.types.ip_sets

        out["ip_sets"] = capo_network_firewall.types.ip_sets.deserialize_aws_json_1_0(
            data["IPSets"]
        )
    if data.get("PortSets") is not None:
        import capo_network_firewall.types.port_sets

        out["port_sets"] = (
            capo_network_firewall.types.port_sets.deserialize_aws_json_1_0(
                data["PortSets"]
            )
        )
    if data.get("ContextSets") is not None:
        import capo_network_firewall.types.context_sets

        out["context_sets"] = (
            capo_network_firewall.types.context_sets.deserialize_aws_json_1_0(
                data["ContextSets"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleVariables) -> dict:
    out: dict = {}
    if "ip_sets" in value:
        import capo_network_firewall.types.ip_sets

        out["IPSets"] = capo_network_firewall.types.ip_sets.serialize_cbor(
            value["ip_sets"]
        )
    if "port_sets" in value:
        import capo_network_firewall.types.port_sets

        out["PortSets"] = capo_network_firewall.types.port_sets.serialize_cbor(
            value["port_sets"]
        )
    if "context_sets" in value:
        import capo_network_firewall.types.context_sets

        out["ContextSets"] = capo_network_firewall.types.context_sets.serialize_cbor(
            value["context_sets"]
        )
    return out


def deserialize_cbor(data: dict) -> RuleVariables:
    out: RuleVariables = {}  # type: ignore[typeddict-item]
    if data.get("IPSets") is not None:
        import capo_network_firewall.types.ip_sets

        out["ip_sets"] = capo_network_firewall.types.ip_sets.deserialize_cbor(
            data["IPSets"]
        )
    if data.get("PortSets") is not None:
        import capo_network_firewall.types.port_sets

        out["port_sets"] = capo_network_firewall.types.port_sets.deserialize_cbor(
            data["PortSets"]
        )
    if data.get("ContextSets") is not None:
        import capo_network_firewall.types.context_sets

        out["context_sets"] = capo_network_firewall.types.context_sets.deserialize_cbor(
            data["ContextSets"]
        )
    return out
