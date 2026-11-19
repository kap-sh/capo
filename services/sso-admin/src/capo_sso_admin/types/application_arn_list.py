"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.first_or_third_party_application_arn_type

ApplicationArnList: TypeAlias = list[
    "capo_sso_admin.types.first_or_third_party_application_arn_type.FirstOrThirdPartyApplicationArnType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApplicationArnList:
    return [item for item in data if item is not None]
