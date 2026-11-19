"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_kendra_ranking.types.tag_list.TagList"]
    """<p>A list of tags associated with the rescore execution plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_kendra_ranking.types.tag_list

        out["Tags"] = capo_kendra_ranking.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_kendra_ranking.types.tag_list

        out["tags"] = capo_kendra_ranking.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_kendra_ranking.types.tag_list

        out["Tags"] = capo_kendra_ranking.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_kendra_ranking.types.tag_list

        out["tags"] = capo_kendra_ranking.types.tag_list.deserialize_cbor(data["Tags"])
    return out
