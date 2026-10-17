"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a network connector. <code>VPC_EGRESS</code> provides VPC egress connectivity.</p>"""
NetworkConnectorType: TypeAlias = Literal["VPC_EGRESS",]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorType) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorType:
    return cast(NetworkConnectorType, data)
