"""Generated from Smithy shape ``com.amazonaws.health#awsAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_id

awsAccountIdsList: TypeAlias = list["capo_health.types.account_id.accountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: awsAccountIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> awsAccountIdsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: awsAccountIdsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> awsAccountIdsList:
    return [item for item in data if item is not None]
