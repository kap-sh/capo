"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSetMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.ip_set_arn
    import capo_network_firewall.types.ip_set_metadata

IPSetMetadataMap: TypeAlias = dict[
    "capo_network_firewall.types.ip_set_arn.IPSetArn",
    "capo_network_firewall.types.ip_set_metadata.IPSetMetadata",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: IPSetMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set_metadata

        out[key] = capo_network_firewall.types.ip_set_metadata.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSetMetadataMap:
    out: IPSetMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set_metadata

        out[key] = capo_network_firewall.types.ip_set_metadata.deserialize_aws_json_1_0(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: IPSetMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set_metadata

        out[key] = capo_network_firewall.types.ip_set_metadata.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> IPSetMetadataMap:
    out: IPSetMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set_metadata

        out[key] = capo_network_firewall.types.ip_set_metadata.deserialize_cbor(value)
    return out
