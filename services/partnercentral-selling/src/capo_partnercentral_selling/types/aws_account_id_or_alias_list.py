"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsAccountIdOrAliasList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account

AwsAccountIdOrAliasList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_account.AwsAccount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsAccountIdOrAliasList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsAccountIdOrAliasList:
    return [item for item in data if item is not None]


def redact_sensitive(value: AwsAccountIdOrAliasList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
