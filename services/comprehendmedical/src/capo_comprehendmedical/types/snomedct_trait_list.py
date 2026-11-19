"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTTraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.snomedct_trait

SNOMEDCTTraitList: TypeAlias = list[
    "capo_comprehendmedical.types.snomedct_trait.SNOMEDCTTrait"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTTraitList) -> list:
    import capo_comprehendmedical.types.snomedct_trait

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.snomedct_trait.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTTraitList:
    import capo_comprehendmedical.types.snomedct_trait

    out: SNOMEDCTTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.snomedct_trait.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTTraitList) -> list:
    import capo_comprehendmedical.types.snomedct_trait

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.snomedct_trait.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SNOMEDCTTraitList:
    import capo_comprehendmedical.types.snomedct_trait

    out: SNOMEDCTTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.snomedct_trait.deserialize_cbor(item))
    return out
