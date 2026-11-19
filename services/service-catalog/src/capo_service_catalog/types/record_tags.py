"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.record_tag

RecordTags: TypeAlias = list["capo_service_catalog.types.record_tag.RecordTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordTags) -> list:
    import capo_service_catalog.types.record_tag

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecordTags:
    import capo_service_catalog.types.record_tag

    out: RecordTags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.record_tag.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordTags) -> list:
    import capo_service_catalog.types.record_tag

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RecordTags:
    import capo_service_catalog.types.record_tag

    out: RecordTags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.record_tag.deserialize_cbor(item))
    return out
