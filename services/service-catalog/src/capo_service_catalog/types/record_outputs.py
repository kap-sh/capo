"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.record_output

RecordOutputs: TypeAlias = list["capo_service_catalog.types.record_output.RecordOutput"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordOutputs) -> list:
    import capo_service_catalog.types.record_output

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.record_output.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordOutputs:
    import capo_service_catalog.types.record_output

    out: RecordOutputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.record_output.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordOutputs) -> list:
    import capo_service_catalog.types.record_output

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.record_output.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RecordOutputs:
    import capo_service_catalog.types.record_output

    out: RecordOutputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.record_output.deserialize_cbor(item))
    return out
