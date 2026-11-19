"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SecurityGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.security_group_name

SecurityGroupNames: TypeAlias = list[
    "capo_workspaces_instances.types.security_group_name.SecurityGroupName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupNames:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupNames) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SecurityGroupNames:
    return [item for item in data if item is not None]
