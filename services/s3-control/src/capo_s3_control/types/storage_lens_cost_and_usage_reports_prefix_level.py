"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensCostAndUsageReportsPrefixLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.is_enabled
    import capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria


class StorageLensCostAndUsageReportsPrefixLevel(TypedDict, closed=True):
    is_enabled: "capo_s3_control.types.is_enabled.IsEnabled"
    """<p>Indicates whether prefix-level cost data publishing to Amazon Web Services CUR is enabled.</p>"""
    selection_criteria: NotRequired[
        "capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria.StorageLensCostAndUsageReportsSelectionCriteria"
    ]
    """<p>A container for the selection criteria that determines the prefix depths for which cost data is published to Amazon Web Services CUR.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensCostAndUsageReportsPrefixLevel, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IsEnabled").text = (
        "true" if value.get("is_enabled", False) else "false"
    )
    if "selection_criteria" in value:
        import capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria

        capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria.serialize_xml(
            value["selection_criteria"], el, "SelectionCriteria"
        )


def deserialize_xml(el: Element) -> StorageLensCostAndUsageReportsPrefixLevel:
    out: StorageLensCostAndUsageReportsPrefixLevel = {}  # type: ignore[typeddict-item]
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    child_selection_criteria = el.find("SelectionCriteria")
    if child_selection_criteria is not None:
        import capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria

        out["selection_criteria"] = (
            capo_s3_control.types.storage_lens_cost_and_usage_reports_selection_criteria.deserialize_xml(
                child_selection_criteria
            )
        )
    return out
