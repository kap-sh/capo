"""Generated from Smithy shape ``com.amazonaws.opensearch#DiffItems``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.diff_item_name_list
    import capo_opensearch.types.divergent_item_list


class DiffItems(TypedDict, closed=True):
    source_only: NotRequired[
        "capo_opensearch.types.diff_item_name_list.DiffItemNameList"
    ]
    """<p>The names of items that exist only on the source domain.</p>"""
    target_only: NotRequired[
        "capo_opensearch.types.diff_item_name_list.DiffItemNameList"
    ]
    """<p>The names of items that exist only on the target domain.</p>"""
    diverged: NotRequired["capo_opensearch.types.divergent_item_list.DivergentItemList"]
    """<p>The items that exist on both domains but differ, with the diverging fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiffItems) -> dict:
    out: dict = {}
    if "source_only" in value:
        import capo_opensearch.types.diff_item_name_list

        out["SourceOnly"] = capo_opensearch.types.diff_item_name_list.serialize_json(
            value["source_only"]
        )
    if "target_only" in value:
        import capo_opensearch.types.diff_item_name_list

        out["TargetOnly"] = capo_opensearch.types.diff_item_name_list.serialize_json(
            value["target_only"]
        )
    if "diverged" in value:
        import capo_opensearch.types.divergent_item_list

        out["Diverged"] = capo_opensearch.types.divergent_item_list.serialize_json(
            value["diverged"]
        )
    return out


def deserialize_json(data: dict) -> DiffItems:
    out: DiffItems = {}  # type: ignore[typeddict-item]
    if data.get("SourceOnly") is not None:
        import capo_opensearch.types.diff_item_name_list

        out["source_only"] = capo_opensearch.types.diff_item_name_list.deserialize_json(
            data["SourceOnly"]
        )
    if data.get("TargetOnly") is not None:
        import capo_opensearch.types.diff_item_name_list

        out["target_only"] = capo_opensearch.types.diff_item_name_list.deserialize_json(
            data["TargetOnly"]
        )
    if data.get("Diverged") is not None:
        import capo_opensearch.types.divergent_item_list

        out["diverged"] = capo_opensearch.types.divergent_item_list.deserialize_json(
            data["Diverged"]
        )
    return out
