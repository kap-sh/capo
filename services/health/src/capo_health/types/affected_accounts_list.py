"""Generated from Smithy shape ``com.amazonaws.health#affectedAccountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_id

affectedAccountsList: TypeAlias = list["capo_health.types.account_id.accountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: affectedAccountsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> affectedAccountsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: affectedAccountsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> affectedAccountsList:
    return [item for item in data if item is not None]
