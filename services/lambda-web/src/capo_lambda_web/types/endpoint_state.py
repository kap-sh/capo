"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function endpoint. Possible values:</p> <ul> <li> <p> <code>Pending</code> – The endpoint is being created.</p> </li> <li> <p> <code>Active</code> – The endpoint is ready to receive traffic.</p> </li> <li> <p> <code>Failed</code> – Endpoint creation or update failed.</p> </li> <li> <p> <code>Deleting</code> – The endpoint is being deleted.</p> </li> </ul>"""
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
