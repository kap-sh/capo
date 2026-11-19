"""Generated from Smithy shape ``com.amazonaws.health#OrganizationAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_id

OrganizationAccountIdsList: TypeAlias = list["capo_health.types.account_id.accountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationAccountIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationAccountIdsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationAccountIdsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OrganizationAccountIdsList:
    return [item for item in data if item is not None]
