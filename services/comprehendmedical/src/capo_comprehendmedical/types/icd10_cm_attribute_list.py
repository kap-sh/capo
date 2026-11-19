"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.icd10_cm_attribute

ICD10CMAttributeList: TypeAlias = list[
    "capo_comprehendmedical.types.icd10_cm_attribute.ICD10CMAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMAttributeList) -> list:
    import capo_comprehendmedical.types.icd10_cm_attribute

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.icd10_cm_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMAttributeList:
    import capo_comprehendmedical.types.icd10_cm_attribute

    out: ICD10CMAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.icd10_cm_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMAttributeList) -> list:
    import capo_comprehendmedical.types.icd10_cm_attribute

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.icd10_cm_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ICD10CMAttributeList:
    import capo_comprehendmedical.types.icd10_cm_attribute

    out: ICD10CMAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.icd10_cm_attribute.deserialize_cbor(item)
        )
    return out
