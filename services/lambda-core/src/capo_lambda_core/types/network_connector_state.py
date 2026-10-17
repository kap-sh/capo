"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorState``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle state of a network connector. A connector is <code>PENDING</code> while resources provision, <code>ACTIVE</code> when ready for use, <code>INACTIVE</code> when temporarily unavailable, <code>FAILED</code> when creation or update fails, <code>DELETING</code> while resources are cleaned up, and <code>DELETE_FAILED</code> when deletion fails.</p>"""
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
