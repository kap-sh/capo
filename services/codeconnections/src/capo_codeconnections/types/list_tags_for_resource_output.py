"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_codeconnections.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_cbor(data["Tags"])
    return out
