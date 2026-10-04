"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function endpoint. Possible values: <code>Pending</code> (endpoint is being created), <code>Active</code> (endpoint is ready to receive traffic), <code>Failed</code> (endpoint creation or update failed), <code>Deleting</code> (endpoint is being deleted).</p>"""
EndpointState: TypeAlias = Literal[
    "Pending",
    "Active",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointState) -> str:
    return value


def deserialize_json(data: str) -> EndpointState:
    return cast(EndpointState, data)
