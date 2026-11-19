"""Generated from Smithy shape ``com.amazonaws.codedeploy#LifecycleErrorCode``."""

from typing import Literal, TypeAlias, cast

LifecycleErrorCode: TypeAlias = Literal[
    "Success",
    "ScriptMissing",
    "ScriptNotExecutable",
    "ScriptTimedOut",
    "ScriptFailed",
    "UnknownError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleErrorCode:
    return cast(LifecycleErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LifecycleErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> LifecycleErrorCode:
    return cast(LifecycleErrorCode, data)
