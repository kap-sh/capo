"""Generated from Smithy shape ``com.amazonaws.acmpca#PermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.permission

PermissionList: TypeAlias = list["capo_acm_pca.types.permission.Permission"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionList) -> list:
    import capo_acm_pca.types.permission

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionList:
    import capo_acm_pca.types.permission

    out: PermissionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.permission.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PermissionList) -> list:
    import capo_acm_pca.types.permission

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.permission.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PermissionList:
    import capo_acm_pca.types.permission

    out: PermissionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.permission.deserialize_cbor(item))
    return out
