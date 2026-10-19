"""Generated from Smithy shape ``com.amazonaws.cloudfront#SessionStickinessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer


class SessionStickinessConfig(TypedDict, closed=True):
    idle_ttl: "capo_cloudfront.types.integer.integer"
    """<p>The amount of time after which you want sessions to cease if no requests are received. Allowed values are 300–3600 seconds (5–60 minutes).</p> <p>The value must be less than or equal to <code>MaximumTTL</code>.</p>"""
    maximum_ttl: "capo_cloudfront.types.integer.integer"
    """<p>The maximum amount of time to consider requests from the viewer as being part of the same session. Allowed values are 300–3600 seconds (5–60 minutes).</p> <p>The value must be greater than or equal to <code>IdleTTL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SessionStickinessConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IdleTTL").text = str(value["idle_ttl"])
    SubElement(el, "MaximumTTL").text = str(value["maximum_ttl"])


def deserialize_xml(el: Element) -> SessionStickinessConfig:
    out: SessionStickinessConfig = {}  # type: ignore[typeddict-item]
    child_idle_ttl = el.find("IdleTTL")
    if child_idle_ttl is not None:
        out["idle_ttl"] = int(child_idle_ttl.text or "")
    else:
        out["idle_ttl"] = 0
    child_maximum_ttl = el.find("MaximumTTL")
    if child_maximum_ttl is not None:
        out["maximum_ttl"] = int(child_maximum_ttl.text or "")
    else:
        out["maximum_ttl"] = 0
    return out
