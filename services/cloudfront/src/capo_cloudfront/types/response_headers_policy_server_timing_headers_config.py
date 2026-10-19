"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyServerTimingHeadersConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.sampling_rate


class ResponseHeadersPolicyServerTimingHeadersConfig(TypedDict, closed=True):
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront adds the <code>Server-Timing</code> header to HTTP responses that it sends in response to requests that match a cache behavior that's associated with this response headers policy.</p>"""
    sampling_rate: NotRequired["capo_cloudfront.types.sampling_rate.SamplingRate"]
    """<p>A number 0–100 (inclusive) that specifies the percentage of responses that you want CloudFront to add the <code>Server-Timing</code> header to. When you set the sampling rate to 100, CloudFront adds the <code>Server-Timing</code> header to the HTTP response for every request that matches the cache behavior that this response headers policy is attached to. When you set it to 50, CloudFront adds the header to 50% of the responses for requests that match the cache behavior. You can set the sampling rate to any number 0–100 with up to four decimal places.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyServerTimingHeadersConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "sampling_rate" in value:
        SubElement(el, "SamplingRate").text = (
            "NaN"
            if value["sampling_rate"] != value["sampling_rate"]
            else "Infinity"
            if value["sampling_rate"] == float("inf")
            else "-Infinity"
            if value["sampling_rate"] == float("-inf")
            else str(value["sampling_rate"])
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyServerTimingHeadersConfig:
    out: ResponseHeadersPolicyServerTimingHeadersConfig = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_sampling_rate = el.find("SamplingRate")
    if child_sampling_rate is not None:
        out["sampling_rate"] = float(child_sampling_rate.text or "")
    return out
