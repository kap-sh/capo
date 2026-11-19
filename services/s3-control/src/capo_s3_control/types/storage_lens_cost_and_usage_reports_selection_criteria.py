"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensCostAndUsageReportsSelectionCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_cost_and_usage_reports_max_depth
    import capo_s3_control.types.storage_lens_cost_and_usage_reports_min_depth


class StorageLensCostAndUsageReportsSelectionCriteria(TypedDict, closed=True):
    min_depth: NotRequired[
        "capo_s3_control.types.storage_lens_cost_and_usage_reports_min_depth.StorageLensCostAndUsageReportsMinDepth"
    ]
    """<p>The minimum prefix depth (inclusive) for which cost data is published to Amazon Web Services CUR. You must provide both <code>MinDepth</code> and <code>MaxDepth</code> together, or neither. If neither is provided, <code>MinDepth</code> defaults to <code>1</code>.</p>"""
    max_depth: NotRequired[
        "capo_s3_control.types.storage_lens_cost_and_usage_reports_max_depth.StorageLensCostAndUsageReportsMaxDepth"
    ]
    """<p>The maximum prefix depth (inclusive) for which cost data is published to Amazon Web Services CUR. You must provide both <code>MinDepth</code> and <code>MaxDepth</code> together, or neither. If neither is provided, <code>MaxDepth</code> defaults to <code>3</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensCostAndUsageReportsSelectionCriteria, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "min_depth" in value:
        SubElement(el, "MinDepth").text = str(value["min_depth"])
    if "max_depth" in value:
        SubElement(el, "MaxDepth").text = str(value["max_depth"])


def deserialize_xml(el: Element) -> StorageLensCostAndUsageReportsSelectionCriteria:
    out: StorageLensCostAndUsageReportsSelectionCriteria = {}  # type: ignore[typeddict-item]
    child_min_depth = el.find("MinDepth")
    if child_min_depth is not None:
        out["min_depth"] = int(child_min_depth.text or "")
    child_max_depth = el.find("MaxDepth")
    if child_max_depth is not None:
        out["max_depth"] = int(child_max_depth.text or "")
    return out
