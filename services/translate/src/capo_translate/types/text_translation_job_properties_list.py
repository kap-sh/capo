"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.text_translation_job_properties

TextTranslationJobPropertiesList: TypeAlias = list[
    "capo_translate.types.text_translation_job_properties.TextTranslationJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobPropertiesList) -> list:
    import capo_translate.types.text_translation_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_translate.types.text_translation_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TextTranslationJobPropertiesList:
    import capo_translate.types.text_translation_job_properties

    out: TextTranslationJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_translate.types.text_translation_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TextTranslationJobPropertiesList) -> list:
    import capo_translate.types.text_translation_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_translate.types.text_translation_job_properties.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> TextTranslationJobPropertiesList:
    import capo_translate.types.text_translation_job_properties

    out: TextTranslationJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_translate.types.text_translation_job_properties.deserialize_cbor(item)
        )
    return out
