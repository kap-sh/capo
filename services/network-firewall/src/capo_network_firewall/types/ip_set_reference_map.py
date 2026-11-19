"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSetReferenceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.ip_set_reference
    import capo_network_firewall.types.ip_set_reference_name

IPSetReferenceMap: TypeAlias = dict[
    "capo_network_firewall.types.ip_set_reference_name.IPSetReferenceName",
    "capo_network_firewall.types.ip_set_reference.IPSetReference",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: IPSetReferenceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set_reference

        out[key] = capo_network_firewall.types.ip_set_reference.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSetReferenceMap:
    out: IPSetReferenceMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set_reference

        out[key] = (
            capo_network_firewall.types.ip_set_reference.deserialize_aws_json_1_0(value)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: IPSetReferenceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set_reference

        out[key] = capo_network_firewall.types.ip_set_reference.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> IPSetReferenceMap:
    out: IPSetReferenceMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set_reference

        out[key] = capo_network_firewall.types.ip_set_reference.deserialize_cbor(value)
    return out
