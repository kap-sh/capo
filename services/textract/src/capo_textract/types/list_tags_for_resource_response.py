"""Generated from Smithy shape ``com.amazonaws.textract#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that are part of the requested resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_cbor(data["Tags"])
    return out
