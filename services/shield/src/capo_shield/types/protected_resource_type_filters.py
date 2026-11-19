"""Generated from Smithy shape ``com.amazonaws.shield#ProtectedResourceTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protected_resource_type

ProtectedResourceTypeFilters: TypeAlias = list[
    "capo_shield.types.protected_resource_type.ProtectedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedResourceTypeFilters) -> list:
    import capo_shield.types.protected_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_shield.types.protected_resource_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectedResourceTypeFilters:
    import capo_shield.types.protected_resource_type

    out: ProtectedResourceTypeFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.protected_resource_type.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectedResourceTypeFilters) -> list:
    import capo_shield.types.protected_resource_type

    out: list = []
    for item in value:
        out.append(capo_shield.types.protected_resource_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtectedResourceTypeFilters:
    import capo_shield.types.protected_resource_type

    out: ProtectedResourceTypeFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protected_resource_type.deserialize_cbor(item))
    return out
