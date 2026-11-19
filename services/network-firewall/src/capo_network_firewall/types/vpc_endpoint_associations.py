"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.vpc_endpoint_association_metadata

VpcEndpointAssociations: TypeAlias = list[
    "capo_network_firewall.types.vpc_endpoint_association_metadata.VpcEndpointAssociationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociations) -> list:
    import capo_network_firewall.types.vpc_endpoint_association_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.vpc_endpoint_association_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointAssociations:
    import capo_network_firewall.types.vpc_endpoint_association_metadata

    out: VpcEndpointAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.vpc_endpoint_association_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcEndpointAssociations) -> list:
    import capo_network_firewall.types.vpc_endpoint_association_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.vpc_endpoint_association_metadata.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> VpcEndpointAssociations:
    import capo_network_firewall.types.vpc_endpoint_association_metadata

    out: VpcEndpointAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.vpc_endpoint_association_metadata.deserialize_cbor(
                item
            )
        )
    return out
