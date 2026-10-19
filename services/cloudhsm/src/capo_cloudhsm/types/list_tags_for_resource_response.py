"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tag_list: "capo_cloudhsm.types.tag_list.TagList"
    """<p>One or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_cloudhsm.types.tag_list

    out["TagList"] = capo_cloudhsm.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("TagList") is not None:
        import capo_cloudhsm.types.tag_list

        out["tag_list"] = capo_cloudhsm.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        out["tag_list"] = []
    return out
