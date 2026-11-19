"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTConceptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.snomedct_concept

SNOMEDCTConceptList: TypeAlias = list[
    "capo_comprehendmedical.types.snomedct_concept.SNOMEDCTConcept"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTConceptList) -> list:
    import capo_comprehendmedical.types.snomedct_concept

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.snomedct_concept.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTConceptList:
    import capo_comprehendmedical.types.snomedct_concept

    out: SNOMEDCTConceptList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.snomedct_concept.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTConceptList) -> list:
    import capo_comprehendmedical.types.snomedct_concept

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.snomedct_concept.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SNOMEDCTConceptList:
    import capo_comprehendmedical.types.snomedct_concept

    out: SNOMEDCTConceptList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.snomedct_concept.deserialize_cbor(item))
    return out
