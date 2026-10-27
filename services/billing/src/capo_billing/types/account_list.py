"""Generated from Smithy shape ``com.amazonaws.billing#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.account_id

AccountList: TypeAlias = list["capo_billing.types.account_id.AccountId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AccountList:
    return [item for item in data if item is not None]
