"""Generated from Smithy shape ``com.amazonaws.route53#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dimension_field


class Dimension(TypedDict, closed=True):
    name: "capo_route_53.types.dimension_field.DimensionField"
    """<p>For the metric that the CloudWatch alarm is associated with, the name of one dimension.</p>"""
    value: "capo_route_53.types.dimension_field.DimensionField"
    """<p>For the metric that the CloudWatch alarm is associated with, the value of one dimension.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Dimension, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        out["value"] = ""
    return out
