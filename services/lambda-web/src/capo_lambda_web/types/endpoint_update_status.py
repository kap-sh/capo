"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointUpdateStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the most recent update to an endpoint. Possible values: <code>InProgress</code> (update is in progress), <code>Successful</code> (update completed successfully), <code>Failed</code> (update failed).</p>"""
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
