"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationFindingCode``."""

from typing import Literal, TypeAlias, cast

ValidationFindingCode: TypeAlias = Literal[
    "TargetInaccessible",
    "TargetUnusable",
    "TargetMissingPermissions",
    "TargetApiDisabled",
    "TargetStateWarning",
    "AwsRoleAssumptionFailed",
    "WebIdentityTokenFailed",
    "OutboundWebIdentityFederationDisabled",
    "ProviderCredentialCreationFailed",
    "TenantSummary",
    "SubscriptionAccessible",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationFindingCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationFindingCode:
    return cast(ValidationFindingCode, data)
