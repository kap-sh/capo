"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormTraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.rx_norm_trait

RxNormTraitList: TypeAlias = list[
    "capo_comprehendmedical.types.rx_norm_trait.RxNormTrait"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormTraitList) -> list:
    import capo_comprehendmedical.types.rx_norm_trait

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.rx_norm_trait.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormTraitList:
    import capo_comprehendmedical.types.rx_norm_trait

    out: RxNormTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.rx_norm_trait.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormTraitList) -> list:
    import capo_comprehendmedical.types.rx_norm_trait

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.rx_norm_trait.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RxNormTraitList:
    import capo_comprehendmedical.types.rx_norm_trait

    out: RxNormTraitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.rx_norm_trait.deserialize_cbor(item))
    return out
