"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorState``."""

from typing import Literal, TypeAlias, cast

NetworkConnectorState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorState) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorState:
    return cast(NetworkConnectorState, data)
