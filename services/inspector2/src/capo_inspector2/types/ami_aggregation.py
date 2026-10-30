"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_sort_by
    import capo_inspector2.types.scan_source_list
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class AmiAggregation(TypedDict, closed=True):
    amis: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The IDs of AMIs to aggregate findings for.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["capo_inspector2.types.ami_sort_by.AmiSortBy"]
    """<p>The value to sort results by.</p>"""
    scan_sources: NotRequired["capo_inspector2.types.scan_source_list.ScanSourceList"]
    """<p>The scan sources to filter the aggregation results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiAggregation) -> dict:
    out: dict = {}
    if "amis" in value:
        import capo_inspector2.types.string_filter_list

        out["amis"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["amis"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "scan_sources" in value:
        import capo_inspector2.types.scan_source_list

        out["scanSources"] = capo_inspector2.types.scan_source_list.serialize_json(
            value["scan_sources"]
        )
    return out


def deserialize_json(data: dict) -> AmiAggregation:
    out: AmiAggregation = {}  # type: ignore[typeddict-item]
    if data.get("amis") is not None:
        import capo_inspector2.types.string_filter_list

        out["amis"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["amis"]
        )
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    if data.get("scanSources") is not None:
        import capo_inspector2.types.scan_source_list

        out["scan_sources"] = capo_inspector2.types.scan_source_list.deserialize_json(
            data["scanSources"]
        )
    return out
