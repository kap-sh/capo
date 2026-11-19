"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoRollbackEvent``."""

from typing import Literal, TypeAlias, cast

AutoRollbackEvent: TypeAlias = Literal[
    "DEPLOYMENT_FAILURE",
    "DEPLOYMENT_STOP_ON_ALARM",
    "DEPLOYMENT_STOP_ON_REQUEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRollbackEvent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoRollbackEvent:
    return cast(AutoRollbackEvent, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoRollbackEvent) -> str:
    return value


def deserialize_cbor(data: str) -> AutoRollbackEvent:
    return cast(AutoRollbackEvent, data)
