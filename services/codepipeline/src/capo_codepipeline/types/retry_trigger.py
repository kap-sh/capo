"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryTrigger``."""

from typing import Literal, TypeAlias, cast

RetryTrigger: TypeAlias = Literal[
    "AutomatedStageRetry",
    "ManualStageRetry",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryTrigger) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetryTrigger:
    return cast(RetryTrigger, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryTrigger) -> str:
    return value


def deserialize_cbor(data: str) -> RetryTrigger:
    return cast(RetryTrigger, data)
