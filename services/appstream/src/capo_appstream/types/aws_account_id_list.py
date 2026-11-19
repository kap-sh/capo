"""Generated from Smithy shape ``com.amazonaws.appstream#AwsAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id

AwsAccountIdList: TypeAlias = list["capo_appstream.types.aws_account_id.AwsAccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsAccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AwsAccountIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsAccountIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AwsAccountIdList:
    return [item for item in data if item is not None]
