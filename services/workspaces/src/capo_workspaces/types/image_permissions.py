"""Generated from Smithy shape ``com.amazonaws.workspaces#ImagePermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.image_permission

ImagePermissions: TypeAlias = list[
    "capo_workspaces.types.image_permission.ImagePermission"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImagePermissions) -> list:
    import capo_workspaces.types.image_permission

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.image_permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImagePermissions:
    import capo_workspaces.types.image_permission

    out: ImagePermissions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.image_permission.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImagePermissions) -> list:
    import capo_workspaces.types.image_permission

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.image_permission.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ImagePermissions:
    import capo_workspaces.types.image_permission

    out: ImagePermissions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.image_permission.deserialize_cbor(item))
    return out
