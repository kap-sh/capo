"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerEventType``."""

from typing import Literal, TypeAlias, cast

TriggerEventType: TypeAlias = Literal[
    "DeploymentStart",
    "DeploymentSuccess",
    "DeploymentFailure",
    "DeploymentStop",
    "DeploymentRollback",
    "DeploymentReady",
    "InstanceStart",
    "InstanceSuccess",
    "InstanceFailure",
    "InstanceReady",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerEventType:
    return cast(TriggerEventType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TriggerEventType) -> str:
    return value


def deserialize_cbor(data: str) -> TriggerEventType:
    return cast(TriggerEventType, data)
