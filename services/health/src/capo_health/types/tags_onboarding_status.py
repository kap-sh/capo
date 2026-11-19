"""Generated from Smithy shape ``com.amazonaws.health#TagsOnboardingStatus``."""

from typing import Literal, TypeAlias, cast

TagsOnboardingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsOnboardingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagsOnboardingStatus:
    return cast(TagsOnboardingStatus, data)
