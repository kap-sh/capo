"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupInstanceType``."""

from typing import Literal, TypeAlias, cast

GameServerGroupInstanceType: TypeAlias = Literal[
    "c4.large",
    "c4.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c5.large",
    "c5.xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5a.large",
    "c5a.xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c6g.medium",
    "c6g.large",
    "c6g.xlarge",
    "c6g.2xlarge",
    "c6g.4xlarge",
    "c6g.8xlarge",
    "c6g.12xlarge",
    "c6g.16xlarge",
    "r4.large",
    "r4.xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.16xlarge",
    "r5.large",
    "r5.xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5a.large",
    "r5a.xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r6g.medium",
    "r6g.large",
    "r6g.xlarge",
    "r6g.2xlarge",
    "r6g.4xlarge",
    "r6g.8xlarge",
    "r6g.12xlarge",
    "r6g.16xlarge",
    "m4.large",
    "m4.xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.10xlarge",
    "m5.large",
    "m5.xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5a.large",
    "m5a.xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m6g.medium",
    "m6g.large",
    "m6g.xlarge",
    "m6g.2xlarge",
    "m6g.4xlarge",
    "m6g.8xlarge",
    "m6g.12xlarge",
    "m6g.16xlarge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupInstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupInstanceType:
    return cast(GameServerGroupInstanceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerGroupInstanceType) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerGroupInstanceType:
    return cast(GameServerGroupInstanceType, data)
