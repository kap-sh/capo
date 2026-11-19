"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.terminology_properties

TerminologyPropertiesList: TypeAlias = list[
    "capo_translate.types.terminology_properties.TerminologyProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyPropertiesList) -> list:
    import capo_translate.types.terminology_properties

    out: list = []
    for item in value:
        out.append(
            capo_translate.types.terminology_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TerminologyPropertiesList:
    import capo_translate.types.terminology_properties

    out: TerminologyPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_translate.types.terminology_properties.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminologyPropertiesList) -> list:
    import capo_translate.types.terminology_properties

    out: list = []
    for item in value:
        out.append(capo_translate.types.terminology_properties.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TerminologyPropertiesList:
    import capo_translate.types.terminology_properties

    out: TerminologyPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_translate.types.terminology_properties.deserialize_cbor(item))
    return out
