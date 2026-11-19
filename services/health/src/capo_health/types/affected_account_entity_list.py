"""Generated from Smithy shape ``com.amazonaws.health#AffectedAccountEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_entity

AffectedAccountEntityList: TypeAlias = list[
    "capo_health.types.account_entity.AccountEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AffectedAccountEntityList) -> list:
    import capo_health.types.account_entity

    out: list = []
    for item in value:
        out.append(capo_health.types.account_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AffectedAccountEntityList:
    import capo_health.types.account_entity

    out: AffectedAccountEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.account_entity.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AffectedAccountEntityList) -> list:
    import capo_health.types.account_entity

    out: list = []
    for item in value:
        out.append(capo_health.types.account_entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AffectedAccountEntityList:
    import capo_health.types.account_entity

    out: AffectedAccountEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.account_entity.deserialize_cbor(item))
    return out
