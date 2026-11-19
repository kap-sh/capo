"""Generated from Smithy shape ``com.amazonaws.fms#MemberAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id

MemberAccounts: TypeAlias = list["capo_fms.types.aws_account_id.AWSAccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MemberAccounts:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MemberAccounts) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MemberAccounts:
    return [item for item in data if item is not None]
