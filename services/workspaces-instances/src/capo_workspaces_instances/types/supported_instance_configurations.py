"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SupportedInstanceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.supported_instance_configuration

SupportedInstanceConfigurations: TypeAlias = list[
    "capo_workspaces_instances.types.supported_instance_configuration.SupportedInstanceConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedInstanceConfigurations) -> list:
    import capo_workspaces_instances.types.supported_instance_configuration

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.supported_instance_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SupportedInstanceConfigurations:
    import capo_workspaces_instances.types.supported_instance_configuration

    out: SupportedInstanceConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.supported_instance_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SupportedInstanceConfigurations) -> list:
    import capo_workspaces_instances.types.supported_instance_configuration

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.supported_instance_configuration.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> SupportedInstanceConfigurations:
    import capo_workspaces_instances.types.supported_instance_configuration

    out: SupportedInstanceConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.supported_instance_configuration.deserialize_cbor(
                item
            )
        )
    return out
