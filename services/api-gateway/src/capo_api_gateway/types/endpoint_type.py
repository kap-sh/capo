"""Generated from Smithy shape ``com.amazonaws.apigateway#EndpointType``."""

from typing import Literal, TypeAlias, cast

"""<p>The endpoint type. The valid values are <code>EDGE</code> for edge-optimized API setup, most suitable for mobile applications; <code>REGIONAL</code> for regional API endpoint setup, most suitable for calling from Amazon Web Services Region; and <code>PRIVATE</code> for private APIs.</p>"""
EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "EDGE",
    "PRIVATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    return cast(EndpointType, data)
