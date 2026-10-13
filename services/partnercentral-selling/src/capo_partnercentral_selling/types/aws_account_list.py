"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsAccountList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account

AwsAccountList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_account.AwsAccount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsAccountList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsAccountList:
    return [item for item in data if item is not None]


def redact_sensitive(value: AwsAccountList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
