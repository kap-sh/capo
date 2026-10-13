"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BlockDeviceMappings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.block_device_mapping_request

BlockDeviceMappings: TypeAlias = list[
    "capo_workspaces_instances.types.block_device_mapping_request.BlockDeviceMappingRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockDeviceMappings) -> list:
    import capo_workspaces_instances.types.block_device_mapping_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.block_device_mapping_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BlockDeviceMappings:
    import capo_workspaces_instances.types.block_device_mapping_request

    out: BlockDeviceMappings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.block_device_mapping_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BlockDeviceMappings) -> list[Any]:
    import capo_workspaces_instances.types.block_device_mapping_request

    return [
        capo_workspaces_instances.types.block_device_mapping_request.redact_sensitive(
            item
        )
        for item in value
    ]
