"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EndpointType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a web function endpoint.</p> <p>Valid values:</p> <ul> <li> <p> <code>HomeRegion</code> – Serves traffic from the Region where you created the web function.</p> </li> <li> <p> <code>MultiRegion</code> – Replicates across the Regions that you choose and routes each request to the nearest one.</p> </li> <li> <p> <code>PerRegion</code> – Creates a separate endpoint in each Region that you choose.</p> </li> </ul>"""
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
