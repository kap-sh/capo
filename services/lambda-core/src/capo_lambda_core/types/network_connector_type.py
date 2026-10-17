"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorType``."""

from typing import Literal, TypeAlias, cast

NetworkConnectorType: TypeAlias = Literal["VPC_EGRESS",]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorType) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorType:
    return cast(NetworkConnectorType, data)
