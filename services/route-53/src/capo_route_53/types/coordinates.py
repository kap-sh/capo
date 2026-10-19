"""Generated from Smithy shape ``com.amazonaws.route53#Coordinates``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.latitude
    import capo_route_53.types.longitude


class Coordinates(TypedDict, closed=True):
    latitude: "capo_route_53.types.latitude.Latitude"
    """<p> Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90). </p>"""
    longitude: "capo_route_53.types.longitude.Longitude"
    """<p> Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180). </p>"""


# --- restXml ser/de ---
def serialize_xml(value: Coordinates, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Latitude").text = str(value["latitude"])
    SubElement(el, "Longitude").text = str(value["longitude"])


def deserialize_xml(el: Element) -> Coordinates:
    out: Coordinates = {}  # type: ignore[typeddict-item]
    child_latitude = el.find("Latitude")
    if child_latitude is not None:
        out["latitude"] = str(child_latitude.text or "")
    else:
        out["latitude"] = ""
    child_longitude = el.find("Longitude")
    if child_longitude is not None:
        out["longitude"] = str(child_longitude.text or "")
    else:
        out["longitude"] = ""
    return out
