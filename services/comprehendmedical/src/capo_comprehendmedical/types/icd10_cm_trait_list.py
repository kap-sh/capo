"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMTraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.icd10_cm_trait

ICD10CMTraitList: TypeAlias = list[
    "capo_comprehendmedical.types.icd10_cm_trait.ICD10CMTrait"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMTraitList) -> list:
    import capo_comprehendmedical.types.icd10_cm_trait

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.icd10_cm_trait.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMTraitList:
    import capo_comprehendmedical.types.icd10_cm_trait

    out: ICD10CMTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.icd10_cm_trait.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMTraitList) -> list:
    import capo_comprehendmedical.types.icd10_cm_trait

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.icd10_cm_trait.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ICD10CMTraitList:
    import capo_comprehendmedical.types.icd10_cm_trait

    out: ICD10CMTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.icd10_cm_trait.deserialize_cbor(item))
    return out
