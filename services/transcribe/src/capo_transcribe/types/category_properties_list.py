"""Generated from Smithy shape ``com.amazonaws.transcribe#CategoryPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.category_properties

CategoryPropertiesList: TypeAlias = list[
    "capo_transcribe.types.category_properties.CategoryProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryPropertiesList) -> list:
    import capo_transcribe.types.category_properties

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.category_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CategoryPropertiesList:
    import capo_transcribe.types.category_properties

    out: CategoryPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.category_properties.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CategoryPropertiesList) -> list:
    import capo_transcribe.types.category_properties

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.category_properties.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> CategoryPropertiesList:
    import capo_transcribe.types.category_properties

    out: CategoryPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.category_properties.deserialize_cbor(item))
    return out
