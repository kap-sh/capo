"""Generated from Smithy shape ``com.amazonaws.voiceid#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_voice_id.types.tag_list.TagList"]
    """<p>The list of tags associated with the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_voice_id.types.tag_list

        out["Tags"] = capo_voice_id.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_voice_id.types.tag_list

        out["tags"] = capo_voice_id.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_voice_id.types.tag_list

        out["tags"] = capo_voice_id.types.tag_list.redact_sensitive(value["tags"])
    return out
