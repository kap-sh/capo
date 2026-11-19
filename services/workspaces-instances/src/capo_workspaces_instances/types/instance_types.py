"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.instance_type_info

InstanceTypes: TypeAlias = list[
    "capo_workspaces_instances.types.instance_type_info.InstanceTypeInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypes) -> list:
    import capo_workspaces_instances.types.instance_type_info

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.instance_type_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceTypes:
    import capo_workspaces_instances.types.instance_type_info

    out: InstanceTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.instance_type_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceTypes) -> list:
    import capo_workspaces_instances.types.instance_type_info

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.instance_type_info.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> InstanceTypes:
    import capo_workspaces_instances.types.instance_type_info

    out: InstanceTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.instance_type_info.deserialize_cbor(item)
        )
    return out
