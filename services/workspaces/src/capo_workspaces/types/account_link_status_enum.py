"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLinkStatusEnum``."""

from typing import Literal, TypeAlias, cast

AccountLinkStatusEnum: TypeAlias = Literal[
    "LINKED",
    "LINKING_FAILED",
    "LINK_NOT_FOUND",
    "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLinkStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountLinkStatusEnum:
    return cast(AccountLinkStatusEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountLinkStatusEnum) -> str:
    return value


def deserialize_cbor(data: str) -> AccountLinkStatusEnum:
    return cast(AccountLinkStatusEnum, data)
