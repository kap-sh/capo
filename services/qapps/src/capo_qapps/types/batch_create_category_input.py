"""Generated from Smithy shape ``com.amazonaws.qapps#BatchCreateCategoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.batch_create_category_input_category_list
    import capo_qapps.types.instance_id


class BatchCreateCategoryInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "capo_qapps.types.batch_create_category_input_category_list.BatchCreateCategoryInputCategoryList"
    """<p>The list of category objects to be created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateCategoryInput) -> dict:
    out: dict = {}
    import capo_qapps.types.batch_create_category_input_category_list

    out["categories"] = (
        capo_qapps.types.batch_create_category_input_category_list.serialize_json(
            value["categories"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateCategoryInput:
    out: BatchCreateCategoryInput = {}  # type: ignore[typeddict-item]
    if data.get("categories") is not None:
        import capo_qapps.types.batch_create_category_input_category_list

        out["categories"] = (
            capo_qapps.types.batch_create_category_input_category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    return out
