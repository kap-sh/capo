"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#LossFnName``."""

from typing import Literal, TypeAlias, cast

LossFnName: TypeAlias = Literal[
    "cross_entropy",
    "importance_sampling",
    "ppo",
    "cispo",
]


# --- restJson1 ser/de ---
def serialize_json(value: LossFnName) -> str:
    return value


def deserialize_json(data: str) -> LossFnName:
    return cast(LossFnName, data)
