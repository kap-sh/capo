"""Generated from Smithy shape ``com.amazonaws.opensearch#DivergentItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.diff_item_name
    import capo_opensearch.types.divergent_field_list


class DivergentItem(TypedDict, closed=True):
    name: NotRequired["capo_opensearch.types.diff_item_name.DiffItemName"]
    """<p>The name of the item.</p>"""
    fields: NotRequired["capo_opensearch.types.divergent_field_list.DivergentFieldList"]
    """<p>The fields of the item that differ.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DivergentItem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "fields" in value:
        import capo_opensearch.types.divergent_field_list

        out["Fields"] = capo_opensearch.types.divergent_field_list.serialize_json(
            value["fields"]
        )
    return out


def deserialize_json(data: dict) -> DivergentItem:
    out: DivergentItem = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Fields") is not None:
        import capo_opensearch.types.divergent_field_list

        out["fields"] = capo_opensearch.types.divergent_field_list.deserialize_json(
            data["Fields"]
        )
    return out
