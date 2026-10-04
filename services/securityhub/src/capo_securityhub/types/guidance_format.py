"""Generated from Smithy shape ``com.amazonaws.securityhub#GuidanceFormat``."""

from typing import Literal, TypeAlias, cast

GuidanceFormat: TypeAlias = Literal[
    "All",
    "AwsCli",
    "Cli",
    "Python",
    "Terraform",
    "Cdk",
    "CloudFormation",
    "IaC",
    "Template",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuidanceFormat) -> str:
    return value


def deserialize_json(data: str) -> GuidanceFormat:
    return cast(GuidanceFormat, data)
