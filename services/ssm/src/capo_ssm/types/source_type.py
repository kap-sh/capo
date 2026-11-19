"""Generated from Smithy shape ``com.amazonaws.ssm#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "AWS::EC2::Instance",
    "AWS::IoT::Thing",
    "AWS::SSM::ManagedInstance",
    "Microsoft.Compute/virtualMachines",
    "compute.googleapis.com/Instance",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    return cast(SourceType, data)
