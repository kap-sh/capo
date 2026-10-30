"""Generated from Smithy shape ``com.amazonaws.opensearch#CategoryDiffResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.diff_count
    import capo_opensearch.types.diff_items
    import capo_opensearch.types.diff_status


class CategoryDiffResult(TypedDict, closed=True):
    status: NotRequired["capo_opensearch.types.diff_status.DiffStatus"]
    """<p>Whether the category was compared successfully. <code>compared</code> means the result is complete; <code>error</code> means the category could not be read.</p>"""
    in_sync: "capo_opensearch.types.diff_count.DiffCount"
    """<p>The number of items that are identical on both domains.</p>"""
    source_only: "capo_opensearch.types.diff_count.DiffCount"
    """<p>The number of items that exist only on the source domain.</p>"""
    target_only: "capo_opensearch.types.diff_count.DiffCount"
    """<p>The number of items that exist only on the target domain.</p>"""
    diverged: "capo_opensearch.types.diff_count.DiffCount"
    """<p>The number of items that exist on both domains but differ.</p>"""
    items: NotRequired["capo_opensearch.types.diff_items.DiffItems"]
    """<p>The names of the items that differ, and for diverging items, the fields that differ.</p>"""
    truncated: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether <code>Items</code> omits some differences because the category contained more than the response can carry. The counts remain complete when this is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryDiffResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_opensearch.types.diff_status

        out["Status"] = capo_opensearch.types.diff_status.serialize_json(
            value["status"]
        )
    out["InSync"] = value.get("in_sync", 0)
    out["SourceOnly"] = value.get("source_only", 0)
    out["TargetOnly"] = value.get("target_only", 0)
    out["Diverged"] = value.get("diverged", 0)
    if "items" in value:
        import capo_opensearch.types.diff_items

        out["Items"] = capo_opensearch.types.diff_items.serialize_json(value["items"])
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> CategoryDiffResult:
    out: CategoryDiffResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_opensearch.types.diff_status

        out["status"] = capo_opensearch.types.diff_status.deserialize_json(
            data["Status"]
        )
    if data.get("InSync") is not None:
        out["in_sync"] = data["InSync"]
    else:
        out["in_sync"] = 0
    if data.get("SourceOnly") is not None:
        out["source_only"] = data["SourceOnly"]
    else:
        out["source_only"] = 0
    if data.get("TargetOnly") is not None:
        out["target_only"] = data["TargetOnly"]
    else:
        out["target_only"] = 0
    if data.get("Diverged") is not None:
        out["diverged"] = data["Diverged"]
    else:
        out["diverged"] = 0
    if data.get("Items") is not None:
        import capo_opensearch.types.diff_items

        out["items"] = capo_opensearch.types.diff_items.deserialize_json(data["Items"])
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    return out
