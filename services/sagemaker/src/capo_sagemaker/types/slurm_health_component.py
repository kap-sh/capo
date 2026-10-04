"""Generated from Smithy shape ``com.amazonaws.sagemaker#SlurmHealthComponent``."""

from typing import Literal, TypeAlias, cast

SlurmHealthComponent: TypeAlias = Literal["Slurmdbd",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlurmHealthComponent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SlurmHealthComponent:
    return cast(SlurmHealthComponent, data)
