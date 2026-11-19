"""Generated from Smithy shape ``com.amazonaws.memorydb#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.user

UserList: TypeAlias = list["capo_memorydb.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserList) -> list:
    import capo_memorydb.types.user

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserList:
    import capo_memorydb.types.user

    out: UserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.user.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserList) -> list:
    import capo_memorydb.types.user

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.user.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UserList:
    import capo_memorydb.types.user

    out: UserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.user.deserialize_cbor(item))
    return out
