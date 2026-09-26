"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.tags


class ListTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_lambda_microvms.types.tags.Tags"]
    """<p>The key-value pairs of tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_lambda_microvms.types.tags

        out["Tags"] = capo_lambda_microvms.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.deserialize_json(data["Tags"])
    return out
