"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

MatchmakingConfigurationStatus: TypeAlias = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PLACING",
    "QUEUED",
    "REQUIRES_ACCEPTANCE",
    "SEARCHING",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MatchmakingConfigurationStatus:
    return cast(MatchmakingConfigurationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MatchmakingConfigurationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> MatchmakingConfigurationStatus:
    return cast(MatchmakingConfigurationStatus, data)
