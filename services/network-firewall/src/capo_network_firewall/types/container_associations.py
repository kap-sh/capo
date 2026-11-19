"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.container_association_summary

ContainerAssociations: TypeAlias = list[
    "capo_network_firewall.types.container_association_summary.ContainerAssociationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerAssociations) -> list:
    import capo_network_firewall.types.container_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.container_association_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContainerAssociations:
    import capo_network_firewall.types.container_association_summary

    out: ContainerAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.container_association_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerAssociations) -> list:
    import capo_network_firewall.types.container_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.container_association_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ContainerAssociations:
    import capo_network_firewall.types.container_association_summary

    out: ContainerAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.container_association_summary.deserialize_cbor(
                item
            )
        )
    return out
