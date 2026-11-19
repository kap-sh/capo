"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_properties

ParallelDataPropertiesList: TypeAlias = list[
    "capo_translate.types.parallel_data_properties.ParallelDataProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataPropertiesList) -> list:
    import capo_translate.types.parallel_data_properties

    out: list = []
    for item in value:
        out.append(
            capo_translate.types.parallel_data_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParallelDataPropertiesList:
    import capo_translate.types.parallel_data_properties

    out: ParallelDataPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_translate.types.parallel_data_properties.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParallelDataPropertiesList) -> list:
    import capo_translate.types.parallel_data_properties

    out: list = []
    for item in value:
        out.append(capo_translate.types.parallel_data_properties.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ParallelDataPropertiesList:
    import capo_translate.types.parallel_data_properties

    out: ParallelDataPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_translate.types.parallel_data_properties.deserialize_cbor(item))
    return out
