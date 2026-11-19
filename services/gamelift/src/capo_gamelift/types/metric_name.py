"""Generated from Smithy shape ``com.amazonaws.gamelift#MetricName``."""

from typing import Literal, TypeAlias, cast

MetricName: TypeAlias = Literal[
    "ActivatingGameSessions",
    "ActiveGameSessions",
    "ActiveInstances",
    "AvailableGameSessions",
    "AvailablePlayerSessions",
    "CurrentPlayerSessions",
    "IdleInstances",
    "PercentAvailableGameSessions",
    "PercentIdleInstances",
    "QueueDepth",
    "WaitTime",
    "ConcurrentActivatableGameSessions",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricName:
    return cast(MetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricName) -> str:
    return value


def deserialize_cbor(data: str) -> MetricName:
    return cast(MetricName, data)
