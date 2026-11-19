"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConnectorProvider``."""

from typing import Literal, TypeAlias, cast

ConnectorProvider: TypeAlias = Literal["AZURE",]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProvider) -> str:
    return value


def deserialize_json(data: str) -> ConnectorProvider:
    return cast(ConnectorProvider, data)
