"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.record_detail

RecordDetails: TypeAlias = list["capo_service_catalog.types.record_detail.RecordDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordDetails) -> list:
    import capo_service_catalog.types.record_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.record_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordDetails:
    import capo_service_catalog.types.record_detail

    out: RecordDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.record_detail.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordDetails) -> list:
    import capo_service_catalog.types.record_detail

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RecordDetails:
    import capo_service_catalog.types.record_detail

    out: RecordDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.record_detail.deserialize_cbor(item))
    return out
