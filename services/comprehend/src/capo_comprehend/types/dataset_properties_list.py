"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.dataset_properties

DatasetPropertiesList: TypeAlias = list[
    "capo_comprehend.types.dataset_properties.DatasetProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetPropertiesList) -> list:
    import capo_comprehend.types.dataset_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.dataset_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetPropertiesList:
    import capo_comprehend.types.dataset_properties

    out: DatasetPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.dataset_properties.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetPropertiesList) -> list:
    import capo_comprehend.types.dataset_properties

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.dataset_properties.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DatasetPropertiesList:
    import capo_comprehend.types.dataset_properties

    out: DatasetPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.dataset_properties.deserialize_cbor(item))
    return out
