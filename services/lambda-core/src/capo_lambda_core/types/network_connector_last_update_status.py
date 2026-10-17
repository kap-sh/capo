"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorLastUpdateStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the most recent update operation on a network connector: <code>Successful</code>, <code>Failed</code>, or <code>InProgress</code>.</p>"""
NetworkConnectorLastUpdateStatus: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorLastUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorLastUpdateStatus:
    return cast(NetworkConnectorLastUpdateStatus, data)
