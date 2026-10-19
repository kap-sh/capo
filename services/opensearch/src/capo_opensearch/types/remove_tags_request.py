"""Generated from Smithy shape ``com.amazonaws.opensearch#RemoveTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.string_list


class RemoveTagsRequest(TypedDict, closed=True):
    arn: "capo_opensearch.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the domain, data source, or application from which you want to delete the specified tags.</p>"""
    tag_keys: "capo_opensearch.types.string_list.StringList"
    """<p>The list of tag keys to remove from the domain, data source, or application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import capo_opensearch.types.string_list

    out["TagKeys"] = capo_opensearch.types.string_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> RemoveTagsRequest:
    out: RemoveTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_opensearch.types.string_list

        out["tag_keys"] = capo_opensearch.types.string_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
