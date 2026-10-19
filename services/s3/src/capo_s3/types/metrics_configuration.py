"""Generated from Smithy shape ``com.amazonaws.s3#MetricsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.metrics_filter
    import capo_s3.types.metrics_id


class MetricsConfiguration(TypedDict, closed=True):
    id: "capo_s3.types.metrics_id.MetricsId"
    """<p>The ID used to identify the metrics configuration. The ID has a 64 character limit and can only contain letters, numbers, periods, dashes, and underscores.</p>"""
    filter: NotRequired["capo_s3.types.metrics_filter.MetricsFilter"]
    """<p>Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction (MetricsAndOperator).</p> <note> <p>Metrics configurations for directory buckets do not support tag filters.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: MetricsConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    if "filter" in value:
        import capo_s3.types.metrics_filter

        capo_s3.types.metrics_filter.serialize_xml(value["filter"], el, "Filter")


def deserialize_xml(el: Element) -> MetricsConfiguration:
    out: MetricsConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.metrics_filter

        out["filter"] = capo_s3.types.metrics_filter.deserialize_xml(child_filter)
    return out
