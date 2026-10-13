"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PrivateIpAddresses``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.private_ip_address_specification

PrivateIpAddresses: TypeAlias = list[
    "capo_workspaces_instances.types.private_ip_address_specification.PrivateIpAddressSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateIpAddresses) -> list:
    import capo_workspaces_instances.types.private_ip_address_specification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.private_ip_address_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PrivateIpAddresses:
    import capo_workspaces_instances.types.private_ip_address_specification

    out: PrivateIpAddresses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.private_ip_address_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: PrivateIpAddresses) -> list[Any]:
    import capo_workspaces_instances.types.private_ip_address_specification

    return [
        capo_workspaces_instances.types.private_ip_address_specification.redact_sensitive(
            item
        )
        for item in value
    ]
