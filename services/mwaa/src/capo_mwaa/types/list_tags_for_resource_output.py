"""Generated from Smithy shape ``com.amazonaws.mwaa#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_mwaa.types.tag_map.TagMap"]
    """<p>The key-value tag pairs associated to your environment. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mwaa.types.tag_map

        out["Tags"] = capo_mwaa.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_mwaa.types.tag_map

        out["tags"] = capo_mwaa.types.tag_map.deserialize_json(data["Tags"])
    return out
