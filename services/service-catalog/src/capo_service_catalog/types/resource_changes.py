"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.resource_change

ResourceChanges: TypeAlias = list[
    "capo_service_catalog.types.resource_change.ResourceChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChanges) -> list:
    import capo_service_catalog.types.resource_change

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.resource_change.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceChanges:
    import capo_service_catalog.types.resource_change

    out: ResourceChanges = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.resource_change.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceChanges) -> list:
    import capo_service_catalog.types.resource_change

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.resource_change.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceChanges:
    import capo_service_catalog.types.resource_change

    out: ResourceChanges = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.resource_change.deserialize_cbor(item))
    return out
