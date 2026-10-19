"""Generated from Smithy shape ``com.amazonaws.cloudfront#CaCertificatesBundleS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class CaCertificatesBundleS3Location(TypedDict, closed=True):
    bucket: "capo_cloudfront.types.string.string"
    """<p>The S3 bucket.</p>"""
    key: "capo_cloudfront.types.string.string"
    """<p>The location's key.</p>"""
    region: "capo_cloudfront.types.string.string"
    """<p>The location's Region.</p>"""
    version: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The location's version.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CaCertificatesBundleS3Location, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Bucket").text = str(value["bucket"])
    SubElement(el, "Key").text = str(value["key"])
    SubElement(el, "Region").text = str(value["region"])
    if "version" in value:
        SubElement(el, "Version").text = str(value["version"])


def deserialize_xml(el: Element) -> CaCertificatesBundleS3Location:
    out: CaCertificatesBundleS3Location = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        out["key"] = ""
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    else:
        out["region"] = ""
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
