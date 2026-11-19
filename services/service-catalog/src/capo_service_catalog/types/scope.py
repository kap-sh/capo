"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Scope``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.resource_attribute

Scope: TypeAlias = list[
    "capo_service_catalog.types.resource_attribute.ResourceAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scope) -> list:
    import capo_service_catalog.types.resource_attribute

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.resource_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Scope:
    import capo_service_catalog.types.resource_attribute

    out: Scope = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.resource_attribute.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Scope) -> list:
    import capo_service_catalog.types.resource_attribute

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.resource_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Scope:
    import capo_service_catalog.types.resource_attribute

    out: Scope = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.resource_attribute.deserialize_cbor(item))
    return out
