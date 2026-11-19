"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.record_error

RecordErrors: TypeAlias = list["capo_service_catalog.types.record_error.RecordError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordErrors) -> list:
    import capo_service_catalog.types.record_error

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecordErrors:
    import capo_service_catalog.types.record_error

    out: RecordErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.record_error.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordErrors) -> list:
    import capo_service_catalog.types.record_error

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_error.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RecordErrors:
    import capo_service_catalog.types.record_error

    out: RecordErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.record_error.deserialize_cbor(item))
    return out
