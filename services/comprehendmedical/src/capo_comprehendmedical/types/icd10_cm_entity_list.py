"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.icd10_cm_entity

ICD10CMEntityList: TypeAlias = list[
    "capo_comprehendmedical.types.icd10_cm_entity.ICD10CMEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntityList) -> list:
    import capo_comprehendmedical.types.icd10_cm_entity

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.icd10_cm_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMEntityList:
    import capo_comprehendmedical.types.icd10_cm_entity

    out: ICD10CMEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.icd10_cm_entity.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMEntityList) -> list:
    import capo_comprehendmedical.types.icd10_cm_entity

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.icd10_cm_entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ICD10CMEntityList:
    import capo_comprehendmedical.types.icd10_cm_entity

    out: ICD10CMEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.icd10_cm_entity.deserialize_cbor(item))
    return out
