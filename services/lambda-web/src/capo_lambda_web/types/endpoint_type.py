"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a web function endpoint. Possible values: <code>HomeRegion</code> (serves from the Region where the function was created), <code>MultiRegion</code> (replicates across chosen Regions and routes to the nearest), <code>PerRegion</code> (separate endpoint per Region).</p>"""
EndpointType: TypeAlias = Literal[
    "HomeRegion",
    "MultiRegion",
    "PerRegion",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    return cast(EndpointType, data)
