"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollingAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.account_id

PollingAccountList: TypeAlias = list["capo_codepipeline.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollingAccountList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PollingAccountList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PollingAccountList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PollingAccountList:
    return [item for item in data if item is not None]
