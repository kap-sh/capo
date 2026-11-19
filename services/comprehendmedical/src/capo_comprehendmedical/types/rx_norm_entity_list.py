"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.rx_norm_entity

RxNormEntityList: TypeAlias = list[
    "capo_comprehendmedical.types.rx_norm_entity.RxNormEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntityList) -> list:
    import capo_comprehendmedical.types.rx_norm_entity

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.rx_norm_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormEntityList:
    import capo_comprehendmedical.types.rx_norm_entity

    out: RxNormEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.rx_norm_entity.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormEntityList) -> list:
    import capo_comprehendmedical.types.rx_norm_entity

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.rx_norm_entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RxNormEntityList:
    import capo_comprehendmedical.types.rx_norm_entity

    out: RxNormEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.rx_norm_entity.deserialize_cbor(item))
    return out
