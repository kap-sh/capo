"""Generated from Smithy shape ``com.amazonaws.opensearch#AddTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.tag_list


class AddTagsRequest(TypedDict, closed=True):
    arn: "capo_opensearch.types.arn.ARN"
    """<p>Amazon Resource Name (ARN) for the OpenSearch Service domain, data source, or application to which you want to attach resource tags.</p>"""
    tag_list: "capo_opensearch.types.tag_list.TagList"
    """<p>List of resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import capo_opensearch.types.tag_list

    out["TagList"] = capo_opensearch.types.tag_list.serialize_json(value["tag_list"])
    return out


def deserialize_json(data: dict) -> AddTagsRequest:
    out: AddTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    if data.get("TagList") is not None:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    else:
        out["tag_list"] = []
    return out
