"""Generated from Smithy shape ``com.amazonaws.qapps#BatchUpdateCategoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.category_list_input
    import capo_qapps.types.instance_id


class BatchUpdateCategoryInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "capo_qapps.types.category_list_input.CategoryListInput"
    """<p>The list of categories to be updated with their new values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCategoryInput) -> dict:
    out: dict = {}
    import capo_qapps.types.category_list_input

    out["categories"] = capo_qapps.types.category_list_input.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateCategoryInput:
    out: BatchUpdateCategoryInput = {}  # type: ignore[typeddict-item]
    if data.get("categories") is not None:
        import capo_qapps.types.category_list_input

        out["categories"] = capo_qapps.types.category_list_input.deserialize_json(
            data["categories"]
        )
    else:
        out["categories"] = []
    return out
