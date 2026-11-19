"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TagSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.tag_specification

TagSpecifications: TypeAlias = list[
    "capo_workspaces_instances.types.tag_specification.TagSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagSpecifications) -> list:
    import capo_workspaces_instances.types.tag_specification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.tag_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TagSpecifications:
    import capo_workspaces_instances.types.tag_specification

    out: TagSpecifications = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.tag_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagSpecifications) -> list:
    import capo_workspaces_instances.types.tag_specification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.tag_specification.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> TagSpecifications:
    import capo_workspaces_instances.types.tag_specification

    out: TagSpecifications = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.tag_specification.deserialize_cbor(item)
        )
    return out
