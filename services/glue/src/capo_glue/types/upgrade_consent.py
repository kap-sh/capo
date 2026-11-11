"""Generated from Smithy shape ``com.amazonaws.glue#UpgradeConsent``."""

from typing import Literal, TypeAlias, cast

UpgradeConsent: TypeAlias = Literal[
    "APPROVE",
    "DECLINE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpgradeConsent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpgradeConsent:
    return cast(UpgradeConsent, data)
