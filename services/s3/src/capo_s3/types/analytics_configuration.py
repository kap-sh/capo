"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.analytics_filter
    import capo_s3.types.analytics_id
    import capo_s3.types.storage_class_analysis


class AnalyticsConfiguration(TypedDict, closed=True):
    id: "capo_s3.types.analytics_id.AnalyticsId"
    """<p>The ID that identifies the analytics configuration.</p>"""
    filter: NotRequired["capo_s3.types.analytics_filter.AnalyticsFilter"]
    """<p>The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.</p>"""
    storage_class_analysis: "capo_s3.types.storage_class_analysis.StorageClassAnalysis"
    """<p> Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    if "filter" in value:
        import capo_s3.types.analytics_filter

        capo_s3.types.analytics_filter.serialize_xml(value["filter"], el, "Filter")
    import capo_s3.types.storage_class_analysis

    capo_s3.types.storage_class_analysis.serialize_xml(
        value["storage_class_analysis"], el, "StorageClassAnalysis"
    )


def deserialize_xml(el: Element) -> AnalyticsConfiguration:
    out: AnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.analytics_filter

        out["filter"] = capo_s3.types.analytics_filter.deserialize_xml(child_filter)
    child_storage_class_analysis = el.find("StorageClassAnalysis")
    if child_storage_class_analysis is not None:
        import capo_s3.types.storage_class_analysis

        out["storage_class_analysis"] = (
            capo_s3.types.storage_class_analysis.deserialize_xml(
                child_storage_class_analysis
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.storage_class_analysis required"
        )
    return out
