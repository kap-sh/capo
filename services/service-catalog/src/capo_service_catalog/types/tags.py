"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.tag

Tags: TypeAlias = list["capo_service_catalog.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import capo_service_catalog.types.tag

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import capo_service_catalog.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.tag.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tags) -> list:
    import capo_service_catalog.types.tag

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Tags:
    import capo_service_catalog.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.tag.deserialize_cbor(item))
    return out
