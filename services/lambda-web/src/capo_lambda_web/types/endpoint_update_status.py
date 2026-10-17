"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointUpdateStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the most recent update to an endpoint. Possible values:</p> <ul> <li> <p> <code>InProgress</code> – The update is in progress.</p> </li> <li> <p> <code>Successful</code> – The update completed successfully.</p> </li> <li> <p> <code>Failed</code> – The update failed.</p> </li> </ul>"""
EndpointUpdateStatus: TypeAlias = Literal[
    "InProgress",
    "Successful",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointUpdateStatus:
    return cast(EndpointUpdateStatus, data)
