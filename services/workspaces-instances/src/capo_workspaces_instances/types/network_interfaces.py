"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#NetworkInterfaces``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.instance_network_interface_specification

NetworkInterfaces: TypeAlias = list[
    "capo_workspaces_instances.types.instance_network_interface_specification.InstanceNetworkInterfaceSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterfaces) -> list:
    import capo_workspaces_instances.types.instance_network_interface_specification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.instance_network_interface_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkInterfaces:
    import capo_workspaces_instances.types.instance_network_interface_specification

    out: NetworkInterfaces = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.instance_network_interface_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: NetworkInterfaces) -> list[Any]:
    import capo_workspaces_instances.types.instance_network_interface_specification

    return [
        capo_workspaces_instances.types.instance_network_interface_specification.redact_sensitive(
            item
        )
        for item in value
    ]
