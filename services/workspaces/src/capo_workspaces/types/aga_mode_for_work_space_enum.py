"""Generated from Smithy shape ``com.amazonaws.workspaces#AGAModeForWorkSpaceEnum``."""

from typing import Literal, TypeAlias, cast

AGAModeForWorkSpaceEnum: TypeAlias = Literal[
    "ENABLED_AUTO",
    "DISABLED",
    "INHERITED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AGAModeForWorkSpaceEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AGAModeForWorkSpaceEnum:
    return cast(AGAModeForWorkSpaceEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AGAModeForWorkSpaceEnum) -> str:
    return value


def deserialize_cbor(data: str) -> AGAModeForWorkSpaceEnum:
    return cast(AGAModeForWorkSpaceEnum, data)
