"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Capability``."""

from typing import Literal, TypeAlias, cast

"""Capability granted to the application when booted"""
Capability: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: Capability) -> str:
    return value


def deserialize_json(data: str) -> Capability:
    return cast(Capability, data)
