"""Generated from Smithy shape ``com.amazonaws.qapps#BatchDeleteCategoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.delete_category_input_list
    import capo_qapps.types.instance_id


class BatchDeleteCategoryInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "capo_qapps.types.delete_category_input_list.DeleteCategoryInputList"
    """<p>The list of IDs of the categories to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteCategoryInput) -> dict:
    out: dict = {}
    import capo_qapps.types.delete_category_input_list

    out["categories"] = capo_qapps.types.delete_category_input_list.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteCategoryInput:
    out: BatchDeleteCategoryInput = {}  # type: ignore[typeddict-item]
    if data.get("categories") is not None:
        import capo_qapps.types.delete_category_input_list

        out["categories"] = (
            capo_qapps.types.delete_category_input_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    return out
