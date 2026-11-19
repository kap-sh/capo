"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv4Prefixes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv4_prefix_specification_request

Ipv4Prefixes: TypeAlias = list[
    "capo_workspaces_instances.types.ipv4_prefix_specification_request.Ipv4PrefixSpecificationRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv4Prefixes) -> list:
    import capo_workspaces_instances.types.ipv4_prefix_specification_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.ipv4_prefix_specification_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Ipv4Prefixes:
    import capo_workspaces_instances.types.ipv4_prefix_specification_request

    out: Ipv4Prefixes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.ipv4_prefix_specification_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ipv4Prefixes) -> list:
    import capo_workspaces_instances.types.ipv4_prefix_specification_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.ipv4_prefix_specification_request.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> Ipv4Prefixes:
    import capo_workspaces_instances.types.ipv4_prefix_specification_request

    out: Ipv4Prefixes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.ipv4_prefix_specification_request.deserialize_cbor(
                item
            )
        )
    return out
