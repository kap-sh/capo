"""Generated from Smithy shape ``com.amazonaws.cloudfront#GrpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean


class GrpcConfig(TypedDict, closed=True):
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GrpcConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> GrpcConfig:
    out: GrpcConfig = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
