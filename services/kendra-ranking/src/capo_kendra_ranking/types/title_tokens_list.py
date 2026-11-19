"""Generated from Smithy shape ``com.amazonaws.kendraranking#TitleTokensList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra_ranking.types.tokens

TitleTokensList: TypeAlias = list["capo_kendra_ranking.types.tokens.Tokens"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TitleTokensList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TitleTokensList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TitleTokensList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TitleTokensList:
    return [item for item in data if item is not None]
