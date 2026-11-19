"""Generated from Smithy shape ``com.amazonaws.health#TagsOnboardingStatusForOrganization``."""

from typing import Literal, TypeAlias, cast

TagsOnboardingStatusForOrganization: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsOnboardingStatusForOrganization) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagsOnboardingStatusForOrganization:
    return cast(TagsOnboardingStatusForOrganization, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagsOnboardingStatusForOrganization) -> str:
    return value


def deserialize_cbor(data: str) -> TagsOnboardingStatusForOrganization:
    return cast(TagsOnboardingStatusForOrganization, data)
