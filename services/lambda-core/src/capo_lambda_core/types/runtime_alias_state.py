"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeAliasState``."""

from typing import Literal, TypeAlias, cast

"""The state of a runtime alias."""
RuntimeAliasState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeAliasState) -> str:
    return value


def deserialize_json(data: str) -> RuntimeAliasState:
    return cast(RuntimeAliasState, data)
