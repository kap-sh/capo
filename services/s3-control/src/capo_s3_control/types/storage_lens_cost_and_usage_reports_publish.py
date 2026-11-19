"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensCostAndUsageReportsPublish``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level


class StorageLensCostAndUsageReportsPublish(TypedDict, closed=True):
    prefix_level: NotRequired[
        "capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level.StorageLensCostAndUsageReportsPrefixLevel"
    ]
    """<p>A container for the prefix-level configuration that determines the prefixes for which S3 Storage Lens publishes cost data to Amazon Web Services CUR.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensCostAndUsageReportsPublish, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "prefix_level" in value:
        import capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level

        capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level.serialize_xml(
            value["prefix_level"], el, "PrefixLevel"
        )


def deserialize_xml(el: Element) -> StorageLensCostAndUsageReportsPublish:
    out: StorageLensCostAndUsageReportsPublish = {}  # type: ignore[typeddict-item]
    child_prefix_level = el.find("PrefixLevel")
    if child_prefix_level is not None:
        import capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level

        out["prefix_level"] = (
            capo_s3_control.types.storage_lens_cost_and_usage_reports_prefix_level.deserialize_xml(
                child_prefix_level
            )
        )
    return out
