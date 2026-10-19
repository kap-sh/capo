"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentSingleHeaderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class ContinuousDeploymentSingleHeaderConfig(TypedDict, closed=True):
    header: "capo_cloudfront.types.string.string"
    """<p>The request header name that you want CloudFront to send to your staging distribution. The header must contain the prefix <code>aws-cf-cd-</code>.</p>"""
    value: "capo_cloudfront.types.string.string"
    """<p>The request header value.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ContinuousDeploymentSingleHeaderConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Header").text = str(value["header"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> ContinuousDeploymentSingleHeaderConfig:
    out: ContinuousDeploymentSingleHeaderConfig = {}  # type: ignore[typeddict-item]
    child_header = el.find("Header")
    if child_header is not None:
        out["header"] = str(child_header.text or "")
    else:
        out["header"] = ""
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        out["value"] = ""
    return out
