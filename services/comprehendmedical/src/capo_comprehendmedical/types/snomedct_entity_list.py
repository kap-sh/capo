"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.snomedct_entity

SNOMEDCTEntityList: TypeAlias = list[
    "capo_comprehendmedical.types.snomedct_entity.SNOMEDCTEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTEntityList) -> list:
    import capo_comprehendmedical.types.snomedct_entity

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.snomedct_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTEntityList:
    import capo_comprehendmedical.types.snomedct_entity

    out: SNOMEDCTEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.snomedct_entity.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTEntityList) -> list:
    import capo_comprehendmedical.types.snomedct_entity

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.snomedct_entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SNOMEDCTEntityList:
    import capo_comprehendmedical.types.snomedct_entity

    out: SNOMEDCTEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.snomedct_entity.deserialize_cbor(item))
    return out
