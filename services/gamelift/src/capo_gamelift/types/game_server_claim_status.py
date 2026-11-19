"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerClaimStatus``."""

from typing import Literal, TypeAlias, cast

GameServerClaimStatus: TypeAlias = Literal["CLAIMED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerClaimStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerClaimStatus:
    return cast(GameServerClaimStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerClaimStatus) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerClaimStatus:
    return cast(GameServerClaimStatus, data)
