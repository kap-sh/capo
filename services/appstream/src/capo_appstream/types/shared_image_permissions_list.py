"""Generated from Smithy shape ``com.amazonaws.appstream#SharedImagePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.shared_image_permissions

SharedImagePermissionsList: TypeAlias = list[
    "capo_appstream.types.shared_image_permissions.SharedImagePermissions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedImagePermissionsList) -> list:
    import capo_appstream.types.shared_image_permissions

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.shared_image_permissions.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SharedImagePermissionsList:
    import capo_appstream.types.shared_image_permissions

    out: SharedImagePermissionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.shared_image_permissions.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SharedImagePermissionsList) -> list:
    import capo_appstream.types.shared_image_permissions

    out: list = []
    for item in value:
        out.append(capo_appstream.types.shared_image_permissions.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SharedImagePermissionsList:
    import capo_appstream.types.shared_image_permissions

    out: SharedImagePermissionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.shared_image_permissions.deserialize_cbor(item))
    return out
