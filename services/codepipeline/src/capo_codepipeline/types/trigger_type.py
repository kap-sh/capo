"""Generated from Smithy shape ``com.amazonaws.codepipeline#TriggerType``."""

from typing import Literal, TypeAlias, cast

TriggerType: TypeAlias = Literal[
    "CreatePipeline",
    "StartPipelineExecution",
    "PollForSourceChanges",
    "Webhook",
    "CloudWatchEvent",
    "PutActionRevision",
    "WebhookV2",
    "ManualRollback",
    "AutomatedRollback",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerType:
    return cast(TriggerType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TriggerType) -> str:
    return value


def deserialize_cbor(data: str) -> TriggerType:
    return cast(TriggerType, data)
